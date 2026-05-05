#!/usr/bin/env python3
"""Migrate existing daily research-report HTMLs into structured JSON.

Reads HTML files from the iCloud daily_reports_research directory and emits
two JSON files into docs/data/:

  - papers.json : flat array of unique papers, with merged metadata across
                  every report each paper appears in
  - reports.json: per-report metadata (date, theme, type, paper_ids, ...)

The script is idempotent and can be re-run as new reports are added.

Notes on input variants
-----------------------
1. Modern reports (>= 2026-04-22) embed each paper as a <div> carrying
   data-paper-id plus data-title/authors/journal/design/url/summary/...
   (Either class="card ..." for regular reports or class="paper" for the
   "_詳細分析" variant.)
2. Legacy March-2026 reports use class="paper-card rankN" (or "topN") and
   carry NO data-* attributes; we fall back to parsing the inner HTML
   structure (card-title, card-meta, h4 sections, idea-box, ...).
3. The PD-focused Thursday report uses class="paper-card ... taskN"
   with the modern data-* attribute set.
"""

from __future__ import annotations

import hashlib
import html
import json
import os
import re
import sys
from pathlib import Path
from typing import Optional

try:
    from bs4 import BeautifulSoup
except ImportError:
    print(
        "ERROR: BeautifulSoup4 is required. Install with `pip install beautifulsoup4`.",
        file=sys.stderr,
    )
    sys.exit(1)


SOURCE_ROOT = Path(
    "/Users/asanoyuujiro/Library/Mobile Documents/com~apple~CloudDocs/Claude/daily_reports_research"
)
DEST_DIR = Path("/Users/asanoyuujiro/github/research-dashboard/docs/data")

# Map subdirectory name -> (weekday-en, theme-jp, theme-en).
THEME_DIRS: dict[str, tuple[str, str, str]] = {
    "月曜日_老年医学・健康寿命": ("monday", "老年医学・健康寿命", "geriatrics-healthspan"),
    "火曜日_身体活動・運動疫学": ("tuesday", "身体活動・運動疫学", "physical-activity-epidemiology"),
    "水曜日_筋質・体組成": ("wednesday", "筋質・体組成", "muscle-body-composition"),
    "木曜日_脳・認知": ("thursday", "脳・認知", "brain-cognition"),
    "金曜日_疫学方法論": ("friday", "疫学方法論", "epidemiology-methods"),
    "土曜日_AI・データ科学": ("saturday", "AI・データ科学", "ai-data-science"),
    "日曜日_遺伝子・オミクス": ("sunday", "遺伝子・オミクス", "genetics-omics"),
}

PD_KEYWORDS = ("pd", "parkinson", "パーキンソン")

# Fields that the *_詳細分析 report tends to fill out more fully and that
# should win when merging duplicates.
DETAIL_PRIORITY_FIELDS = (
    "novelty",
    "background",
    "result",
    "impact",
    "keywords",
    "methodology",
    "limitation",
    "implication",
    "idea",
)

# All scalar fields stored on a paper record (besides id, source_reports,
# is_pd_related, first_seen_date, tags).
SCALAR_FIELDS = (
    "title",
    "authors",
    "journal",
    "design",
    "url",
    "summary",
    "methodology",
    "limitation",
    "implication",
    "idea",
    "novelty",
    "background",
    "result",
    "impact",
    "keywords",
)


# ---------------------------------------------------------------------------
# Filename / report-id helpers
# ---------------------------------------------------------------------------


def classify_report(filename: str) -> str:
    """Return one of: 'pd_focused' | 'detail' | 'regular'."""
    stem = Path(filename).stem
    if "PD研究特化" in stem:
        return "pd_focused"
    if "詳細分析" in stem:
        return "detail"
    return "regular"


def build_report_id(date_str: str, weekday_en: str, report_type: str) -> str:
    """Stable per-report id, e.g. '20260427_monday' or '20260427_monday_detail'."""
    if report_type == "regular":
        return f"{date_str}_{weekday_en}"
    return f"{date_str}_{weekday_en}_{report_type}"


def parse_filename(filename: str) -> Optional[str]:
    """Extract the 8-digit YYYYMMDD prefix; return None if not found."""
    m = re.match(r"^(\d{8})_", filename)
    return m.group(1) if m else None


def stable_paper_id(title: str, journal: str) -> str:
    base = f"{(title or '').strip()}|{(journal or '').strip()}"
    return hashlib.sha1(base.encode("utf-8")).hexdigest()[:12]


def normalize_text(value: Optional[str]) -> str:
    if not value:
        return ""
    text = html.unescape(value)
    text = re.sub(r"\s+", " ", text).strip()
    return text


def parse_tags(raw: Optional[str]) -> list[str]:
    if not raw:
        return []
    return [t.strip() for t in raw.split("|") if t and t.strip()]


def is_pd_paper(*, tags: list[str], text_blobs: list[str], report_type: str) -> bool:
    """Decide whether the paper is PD-related.

    Rules (from the spec):
      * report_type == 'pd_focused' → True
      * any tag contains 'PD'/'parkinson'/'パーキンソン' → True
      * any of methodology/idea/keywords/title/etc. text contains those tokens → True
    """
    if report_type == "pd_focused":
        return True
    haystack = " ".join(tags + text_blobs).lower()
    for kw in PD_KEYWORDS:
        if kw in haystack:
            return True
    return False


# ---------------------------------------------------------------------------
# Card extraction
# ---------------------------------------------------------------------------


# Selector that matches every variant we care about.
CARD_SELECTOR = "div.paper-card, div.card[data-paper-id], div.paper[data-paper-id]"


def extract_paper_from_modern_card(card) -> Optional[dict]:
    """Pull data-* attributes off a card. Falls back to legacy parsing if no
    data-paper-id and no data-title are present."""
    if not card.has_attr("data-paper-id") and not card.has_attr("data-title"):
        return None

    record = {
        "data_paper_id": (card.get("data-paper-id") or "").strip(),
        "title": normalize_text(card.get("data-title")),
        "authors": normalize_text(card.get("data-authors")),
        "journal": normalize_text(card.get("data-journal")),
        "design": normalize_text(card.get("data-design")),
        "url": normalize_text(card.get("data-url")),
        "summary": normalize_text(card.get("data-summary"))
        or normalize_text(card.get("data-overview")),
        # data-importance is the modern equivalent of the "重要な点" highlight.
        # We keep it on `summary` if `summary` is empty, else fold into `impact`.
        "methodology": normalize_text(card.get("data-methodology")),
        "limitation": normalize_text(card.get("data-limitation")),
        "implication": normalize_text(card.get("data-implication")),
        "idea": normalize_text(card.get("data-idea")),
        "novelty": normalize_text(card.get("data-novelty")),
        "background": normalize_text(card.get("data-background")),
        "result": normalize_text(card.get("data-result")),
        "impact": normalize_text(card.get("data-impact"))
        or normalize_text(card.get("data-importance")),
        "keywords": normalize_text(card.get("data-keywords")),
        "tags": parse_tags(card.get("data-tags")),
    }
    return record


# Heading -> field mapping. Used for legacy reports where each section is
# introduced by a <h3>/<h4>/<div class="section-label"> heading.
HEADING_TO_FIELD: dict[str, str] = {
    "一言要約": "summary",
    "要約": "summary",
    "要旨": "summary",
    "研究概要": "background",
    "背景・経緯": "background",
    "背景": "background",
    "重要な点": "impact",
    "応用可能性": "impact",
    "方法論評価": "methodology",
    "方法論": "methodology",
    "限界": "limitation",
    "研究への示唆": "implication",
    "示唆": "implication",
    "研究アイデア": "idea",
    "研究アイデアと応用可能性": "idea",
    "新規性・革新性": "novelty",
    "新規性": "novelty",
    "革新性": "novelty",
    "詳細結果と考察": "result",
    "結果": "result",
    "考察": "result",
    "キーワード": "keywords",
    "核心キーワード分析": "keywords",
    "論文の核心になるキーワード分析": "keywords",
    "研究への示唆・研究アイデア": "implication",
}


def _heading_to_field(text: str) -> Optional[str]:
    """Match a heading text to one of our canonical fields. Tolerant of
    leading numbering ('1. ', '1: ', '1) ', etc.) and punctuation."""
    cleaned = re.sub(r"^[0-9]+[\.\):：]\s*", "", text).strip()
    cleaned = re.sub(r"[（(].*?[）)]\s*$", "", cleaned).strip()
    if cleaned in HEADING_TO_FIELD:
        return HEADING_TO_FIELD[cleaned]
    # Substring fallback.
    for key, value in HEADING_TO_FIELD.items():
        if key in cleaned:
            return value
    return None


def _collect_sections_by_heading(card) -> dict[str, str]:
    """Walk through the card and, for each heading element we recognise,
    join the text up to the next heading. Works with <h2>/<h3>/<h4> as
    well as <div class="section-label"> / <div class="section-title-row">.
    """
    headings = card.find_all(
        ["h2", "h3", "h4", "div", "span"],
        class_=lambda c: c
        and any(
            tok in c
            for tok in (
                "section-label",
                "section-title",
                "section-title-row",
                "label",
            )
        ),
    )
    # Also include literal <h3>/<h4> with no class.
    plain_headings = [
        h for h in card.find_all(["h3", "h4"]) if h not in headings
    ]
    all_headings = list(headings) + plain_headings

    out: dict[str, str] = {}
    for heading in all_headings:
        text = normalize_text(heading.get_text(" ", strip=True))
        if not text:
            continue
        field = _heading_to_field(text)
        if not field:
            continue
        # The body text follows in the *next sibling* container or as
        # later siblings until the next recognised heading.
        chunks: list[str] = []
        # If the heading is inside a wrapper (like section-block), its
        # sibling provides content.
        # Strategy: walk parent's children starting after the heading.
        parent = heading.parent
        if parent is None:
            continue
        started = False
        for child in parent.children:
            if child is heading:
                started = True
                continue
            if not started:
                continue
            if getattr(child, "name", None) in ("h2", "h3", "h4"):
                break
            child_class = " ".join(getattr(child, "get", lambda *a: [])("class") or [])
            if child_class and any(
                tok in child_class for tok in ("section-label", "section-title-row")
            ):
                break
            if hasattr(child, "get_text"):
                chunks.append(child.get_text(" ", strip=True))
            elif isinstance(child, str):
                chunks.append(child)
        joined = normalize_text(" ".join(c for c in chunks if c))
        if joined and not out.get(field):
            out[field] = joined
    return out


def _extract_url(card) -> str:
    """First http(s) <a href> we can find inside the card."""
    a = card.find("a", href=re.compile(r"^https?://"))
    return a.get("href", "").strip() if a else ""


def _extract_title(card) -> str:
    """Try a series of selectors that have appeared across versions."""
    for selector in (
        ".card-title",
        ".paper-title-main",
        ".paper-title",
    ):
        node = card.select_one(selector)
        if node:
            text = normalize_text(node.get_text(" ", strip=True))
            if text:
                return text
    # Plain h2/h3 inside.
    h = card.find(["h2", "h3"])
    if h:
        return normalize_text(h.get_text(" ", strip=True))
    return ""


def _extract_meta(card) -> tuple[str, str, str]:
    """(authors, journal, design) — best-effort across formats."""
    authors = ""
    journal = ""
    design = ""

    # Pattern A: <span class="tag tag-journal">, tag-design ...
    for span in card.select(".card-meta .tag, .tag"):
        classes = " ".join(span.get("class") or [])
        text = normalize_text(span.get_text(" ", strip=True))
        if not text:
            continue
        if "tag-journal" in classes and not journal:
            journal = text
        elif "tag-design" in classes and not design:
            design = text

    # Pattern B: 20260505 layout — div.meta-line / meta-block / meta-row.
    for line in card.select(".meta-line, .meta-block > div, .meta-row .meta-item"):
        text = normalize_text(line.get_text(" ", strip=True))
        if not text:
            continue
        m = re.match(r"^(著者|ジャーナル(?:・年)?|研究デザイン|原本URL)[:：]\s*(.*)$", text)
        if m:
            label, value = m.group(1), m.group(2).strip()
            if label == "著者" and not authors:
                authors = value
            elif label.startswith("ジャーナル") and not journal:
                journal = value
            elif label == "研究デザイン" and not design:
                design = value

    # Pattern C: .meta-badge spans (20260422_詳細分析): typically
    # [journal+year], [design], [extra]
    if not journal or not design:
        badges = [normalize_text(b.get_text(" ", strip=True)) for b in card.select(".meta-badge, .meta-tag")]
        badges = [b for b in badges if b]
        if badges:
            if not journal:
                journal = badges[0]
            if not design and len(badges) >= 2:
                design = badges[1]

    return authors, journal, design


def _extract_tags(card) -> list[str]:
    """Aggregate tag-style spans from any of the known layouts."""
    tags: list[str] = []
    seen: set[str] = set()
    for span in card.select(".tags-row .tag, .tags .tag, .tag"):
        # Skip the meta tags handled by _extract_meta (they aren't
        # semantic tags about content).
        classes = " ".join(span.get("class") or [])
        if any(c in classes for c in ("tag-journal", "tag-design", "tag-relevance")):
            continue
        if "meta-tag" in classes or "meta-badge" in classes:
            continue
        text = normalize_text(span.get_text(" ", strip=True))
        if text and text not in seen:
            tags.append(text)
            seen.add(text)
    return tags


def extract_paper_from_legacy_card(card) -> Optional[dict]:
    """Fallback parser for reports without data-paper-id / data-title.

    Handles a number of structural variants:
      * March-2026 cards with .card-title / .card-meta .tag-journal /
        h4 headings (research-aging style).
      * 20260422 cards with .paper-title link / .meta-row / detail-grid.
      * 20260422_詳細分析 multi-section blocks (paper-section, section-block).
      * 20260505 cards with .meta-line / .section.summary etc.
      * 20260505_詳細分析 cards with class "paper top1" and .sec.s1 sections.
      * 20260424_詳細分析 cards inside .paper-wrapper with .paper-header
        and .sections-container.
    """
    title = _extract_title(card)
    if not title:
        return None

    authors, journal, design = _extract_meta(card)
    url = _extract_url(card)

    # Heading-based extraction is the workhorse for legacy formats.
    sections = _collect_sections_by_heading(card)

    # Some 20260505 / 20260422 layouts use class="section <field>" wrappers
    # carrying their own canonical name in the class itself.
    SECTION_CLASS_TO_FIELD = {
        "summary": "summary",
        "overview": "background",
        "importance": "impact",
        "method": "methodology",
        "limit": "limitation",
        "implication": "implication",
        "idea": "idea",
    }
    for div in card.find_all("div", class_=True):
        classes = div.get("class") or []
        if "section" not in classes:
            continue
        for cls in classes:
            field = SECTION_CLASS_TO_FIELD.get(cls)
            if field and not sections.get(field):
                # Strip the leading "label" line (e.g. "<span class='label'>研究概要</span>").
                text = div.get_text(" ", strip=True)
                # The section often opens with the heading label; remove it.
                # E.g. "一言要約 オーストラリア女性..." -> drop the heading.
                for label in (
                    "一言要約",
                    "研究概要",
                    "重要な点",
                    "方法論評価",
                    "限界",
                    "研究への示唆",
                    "研究アイデア",
                ):
                    if text.startswith(label):
                        text = text[len(label):]
                        break
                sections[field] = normalize_text(text)

    # idea-box separate from heading list.
    idea = sections.get("idea", "")
    idea_node = card.select_one(".idea-box")
    if idea_node and not idea:
        idea_text = idea_node.get_text(" ", strip=True)
        idea = normalize_text(re.sub(r"^研究アイデア[:：]\s*", "", idea_text))

    # detail-grid (20260422 layout): each .detail-item holds .detail-label + .detail-content.
    for item in card.select(".detail-item"):
        label_node = item.select_one(".detail-label")
        content_node = item.select_one(".detail-content")
        if not label_node or not content_node:
            continue
        label = normalize_text(label_node.get_text(" ", strip=True))
        field = _heading_to_field(label)
        if not field:
            continue
        text = normalize_text(content_node.get_text(" ", strip=True))
        if text and not sections.get(field):
            sections[field] = text

    record = {
        "data_paper_id": "",
        "title": title,
        "authors": authors,
        "journal": journal,
        "design": design,
        "url": url,
        "summary": sections.get("summary", ""),
        "methodology": sections.get("methodology", ""),
        "limitation": sections.get("limitation", ""),
        "implication": sections.get("implication", ""),
        "idea": idea,
        "novelty": sections.get("novelty", ""),
        "background": sections.get("background", ""),
        "result": sections.get("result", ""),
        "impact": sections.get("impact", ""),
        "keywords": sections.get("keywords", ""),
        "tags": _extract_tags(card),
    }
    return record


# Selector for legacy/specialized container variants, evaluated when the
# modern selector finds nothing.
LEGACY_SELECTORS = (
    "div.paper-card",            # most legacy regular reports
    "div.paper-wrapper",         # 20260424_詳細分析
    "div.paper-section",         # 20260422_詳細分析, 20260423_詳細分析
    "div.paper",                 # 20260505 / 20260505_詳細分析
)


def extract_papers(html_text: str) -> list[dict]:
    soup = BeautifulSoup(html_text, "html.parser")
    seen_ids: set[int] = set()
    out: list[dict] = []

    # Pass 1: modern data-attribute cards.
    for card in soup.select(CARD_SELECTOR):
        rec = extract_paper_from_modern_card(card)
        if rec and rec.get("title"):
            out.append(rec)
            seen_ids.add(id(card))

    if out:
        return out

    # Pass 2: legacy variants. Prefer the most specific selector that
    # matches; we deduplicate by container identity to avoid catching
    # both an outer wrapper and an inner card.
    for selector in LEGACY_SELECTORS:
        cards = soup.select(selector)
        if not cards:
            continue
        # Skip if any matched card is nested inside another already-seen card.
        for card in cards:
            if id(card) in seen_ids:
                continue
            # Also skip cards that are descendants of another match.
            ancestor = card.parent
            ancestor_match = False
            while ancestor is not None:
                if id(ancestor) in seen_ids:
                    ancestor_match = True
                    break
                ancestor = ancestor.parent
            if ancestor_match:
                continue
            rec = extract_paper_from_legacy_card(card)
            if rec and rec.get("title"):
                out.append(rec)
                seen_ids.add(id(card))
        if out:
            break

    return out


# ---------------------------------------------------------------------------
# Merge logic
# ---------------------------------------------------------------------------


def merge_paper(existing: dict, new: dict, *, prefer_new_priority: bool) -> dict:
    """Merge `new` into `existing`. If prefer_new_priority is True (i.e. new
    came from a *_詳細分析 report) the priority fields from `new` win even
    when `existing` has a value."""
    merged = dict(existing)
    for field in SCALAR_FIELDS:
        new_val = new.get(field, "")
        old_val = existing.get(field, "")
        if not new_val:
            continue
        if not old_val:
            merged[field] = new_val
        elif prefer_new_priority and field in DETAIL_PRIORITY_FIELDS:
            merged[field] = new_val
    # Tags: union, preserving order.
    seen = set(merged.get("tags") or [])
    out_tags = list(merged.get("tags") or [])
    for t in new.get("tags") or []:
        if t not in seen:
            out_tags.append(t)
            seen.add(t)
    merged["tags"] = out_tags
    return merged


# ---------------------------------------------------------------------------
# Driver
# ---------------------------------------------------------------------------


def date_iso(yyyymmdd: str) -> str:
    return f"{yyyymmdd[0:4]}-{yyyymmdd[4:6]}-{yyyymmdd[6:8]}"


def main() -> int:
    if not SOURCE_ROOT.exists():
        print(f"Source not found: {SOURCE_ROOT}", file=sys.stderr)
        return 1
    DEST_DIR.mkdir(parents=True, exist_ok=True)

    # Gather all (filepath, theme metadata) pairs deterministically.
    work: list[tuple[Path, str, str, str]] = []  # (path, weekday, theme_jp, theme_en)
    for sub, (weekday, theme_jp, theme_en) in THEME_DIRS.items():
        sub_dir = SOURCE_ROOT / sub
        if not sub_dir.is_dir():
            continue
        for path in sorted(sub_dir.glob("*.html")):
            if path.name.startswith("."):
                continue
            work.append((path, weekday, theme_jp, theme_en))

    papers: dict[str, dict] = {}
    reports: list[dict] = []

    for path, weekday, theme_jp, theme_en in work:
        date_str = parse_filename(path.name)
        if not date_str:
            print(f"  skip (no date prefix): {path.name}", file=sys.stderr)
            continue

        report_type = classify_report(path.name)
        report_id = build_report_id(date_str, weekday, report_type)

        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            text = path.read_text(encoding="utf-8", errors="ignore")

        if len(text.strip()) < 10:
            # Empty / placeholder file (e.g. 20260501_詳細分析).
            print(f"  skip (empty): {path.name}", file=sys.stderr)
            continue

        paper_records = extract_papers(text)
        if not paper_records:
            print(f"  warn  (no papers found): {path.name}", file=sys.stderr)

        rel_html_path = str(path.relative_to(SOURCE_ROOT))
        report_paper_ids: list[str] = []

        for rec in paper_records:
            data_pid = rec.get("data_paper_id") or ""
            title = rec.get("title", "")
            journal = rec.get("journal", "")
            paper_id = data_pid if data_pid else stable_paper_id(title, journal)

            text_blobs = [
                rec.get(f, "") for f in (
                    "title",
                    "summary",
                    "methodology",
                    "idea",
                    "keywords",
                    "background",
                    "novelty",
                    "result",
                    "impact",
                )
            ]
            pd_flag = is_pd_paper(
                tags=rec.get("tags", []),
                text_blobs=text_blobs,
                report_type=report_type,
            )

            if paper_id not in papers:
                papers[paper_id] = {
                    "id": paper_id,
                    **{f: rec.get(f, "") for f in SCALAR_FIELDS},
                    "tags": list(rec.get("tags") or []),
                    "source_reports": [report_id],
                    "is_pd_related": pd_flag,
                    "first_seen_date": date_iso(date_str),
                }
            else:
                merged = merge_paper(
                    papers[paper_id],
                    rec,
                    prefer_new_priority=(report_type == "detail"),
                )
                if report_id not in merged["source_reports"]:
                    merged["source_reports"].append(report_id)
                merged["is_pd_related"] = bool(merged["is_pd_related"]) or pd_flag
                # Earliest first_seen_date wins.
                merged["first_seen_date"] = min(
                    merged.get("first_seen_date") or date_iso(date_str),
                    date_iso(date_str),
                )
                papers[paper_id] = merged

            report_paper_ids.append(paper_id)

        reports.append({
            "id": report_id,
            "date": date_iso(date_str),
            "weekday": weekday,
            "theme_jp": theme_jp,
            "theme_en": theme_en,
            "report_type": report_type,
            "source_html_path": rel_html_path,
            "paper_ids": report_paper_ids,
            "paper_count": len(report_paper_ids),
        })

    # Stable, deterministic ordering for outputs.
    papers_list = sorted(
        papers.values(),
        key=lambda p: (p["first_seen_date"], p["id"]),
    )
    reports.sort(key=lambda r: (r["date"], r["weekday"], r["report_type"]))

    papers_path = DEST_DIR / "papers.json"
    reports_path = DEST_DIR / "reports.json"

    papers_path.write_text(
        json.dumps(papers_list, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    reports_path.write_text(
        json.dumps(reports, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )

    # Summary to stderr.
    by_theme: dict[str, int] = {}
    for r in reports:
        by_theme[r["theme_jp"]] = by_theme.get(r["theme_jp"], 0) + 1
    pd_count = sum(1 for p in papers_list if p.get("is_pd_related"))
    dates = [r["date"] for r in reports]
    print(
        f"Wrote {len(papers_list)} papers ({pd_count} PD-related) "
        f"and {len(reports)} reports.",
        file=sys.stderr,
    )
    if dates:
        print(f"Date range: {min(dates)} .. {max(dates)}", file=sys.stderr)
    print("Reports per theme:", file=sys.stderr)
    for k, v in sorted(by_theme.items()):
        print(f"  {k}: {v}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
