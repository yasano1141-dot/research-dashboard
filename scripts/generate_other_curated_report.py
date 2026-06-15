#!/usr/bin/env python3
"""
「その他」カテゴリのキュレーション版レポートを生成。

曜日テーマ・PD研究と同じ立ち位置の独立カテゴリ。Yuji がその都度依頼した
任意テーマの論文10本をサマライズする運用。テーマは都度変わるため、
--topic でテーマ名（ヘッダー表示・reports.json 記録用）を指定できる。
other_curated_content.py 内に TOPIC 変数があればそれも使う。

使い方:
    python scripts/generate_other_curated_report.py --date YYYYMMDD --topic "睡眠と認知機能"

- other_curated_content.CONTENT（id は {date}_other_NN）の10本を採用
- 新規論文は papers.json に追加、既存なら更新
- HTML を docs/reports/{date}_other.html に生成
- reports.json に weekday="other" のエントリを追記
- 生成前に validate_urls.py と validate_quality.py を実行（rev7/rev9-15 準拠）
"""
from __future__ import annotations

import argparse
import html
import json
import re
from datetime import datetime
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
DATA_DIR = REPO / "docs" / "data"
REPORTS_DIR = REPO / "docs" / "reports"

PAPERS_PATH = DATA_DIR / "papers.json"
REPORTS_JSON_PATH = DATA_DIR / "reports.json"

THEME_KEY = "other"
THEME_JP = "その他"
THEME_EN = "other"
THEME_COLOR = "#0d9488"  # teal-600


def _normalize_title(t: str) -> str:
    return re.sub(r"[^a-z0-9]", "", (t or "").lower())


def _load_topic(cli_topic: str | None) -> str:
    """テーマ名を決定：--topic 引数 > other_curated_content.TOPIC > 既定。"""
    if cli_topic:
        return cli_topic
    try:
        from other_curated_content import TOPIC  # type: ignore
        if TOPIC:
            return str(TOPIC)
    except Exception:
        pass
    return "依頼テーマ"


def select_papers(papers: list[dict], reports_by_id: dict, n: int = 10,
                  report_id: str = "") -> list[dict]:
    """other_curated_content.CONTENT の論文を採用。

    新規論文（CONTENT の id が papers.json に未登録）は dict を構築して返し、
    呼び出し側で papers.json に追加する。過去の「その他」レポートと
    タイトル/URL が完全重複するものは除外する（同テーマ再依頼時の重複防止）。
    """
    try:
        from other_curated_content import CONTENT
    except ImportError:
        CONTENT = {}

    # 過去の「その他」レポートに含まれる論文のタイトル・URL（重複検出用）
    # 今回再生成中の report_id 由来は除外（idempotent）
    existing_titles, existing_urls = set(), set()
    for p in papers:
        for rid in (p.get("source_reports") or []):
            if rid == report_id:
                continue
            r = reports_by_id.get(rid)
            if r and r.get("weekday") == "other":
                nt = _normalize_title(p.get("title", ""))
                url = (p.get("url") or "").rstrip("/").lower()
                if nt:
                    existing_titles.add(nt)
                if url:
                    existing_urls.add(url)
                break

    selected = []
    seen_titles, seen_urls = set(), set()
    paper_index = {p["id"]: p for p in papers}

    for cid, content in CONTENT.items():
        nt = _normalize_title(content.get("title", ""))
        url = (content.get("url") or "").rstrip("/").lower()
        if nt and nt in existing_titles:
            print(f"  ⚠️  skip (過去のその他レポートと重複): {content['title'][:60]}")
            continue
        if url and url in existing_urls:
            print(f"  ⚠️  skip (URL重複): {content['title'][:60]}")
            continue
        if nt and nt in seen_titles:
            continue
        if url and url in seen_urls:
            continue

        if cid in paper_index:
            p = paper_index[cid]
        else:
            p = {
                "id": cid,
                "title": content.get("title", ""),
                "authors": content.get("authors", ""),
                "journal": content.get("journal", ""),
                "design": content.get("design", ""),
                "url": content.get("url", ""),
                "summary": content.get("summary", ""),
                "methodology": content.get("methodology", ""),
                "limitation": content.get("limitation", ""),
                "implication": content.get("implication", ""),
                "idea": content.get("idea", ""),
                "novelty": content.get("originality", ""),
                "background": content.get("overview", ""),
                "result": content.get("discovery", ""),
                "impact": content.get("importance", ""),
                "keywords": "",
                "tags": list(content.get("tags", [])),
                "source_reports": [],
                "is_pd_related": False,
                "first_seen_date": f"{datetime.now():%Y-%m-%d}",
                "fulltext_status": content.get("fulltext_status", ""),
                "_is_new": True,
            }
        selected.append(p)
        if nt:
            seen_titles.add(nt)
        if url:
            seen_urls.add(url)
        if len(selected) >= n:
            break

    if len(selected) < n:
        print(f"  ⚠️  CONTENT に {n} 本未満（{len(selected)} 本のみ）")
    return selected


def merge_curated_content(paper: dict) -> dict:
    try:
        from other_curated_content import CONTENT
    except ImportError:
        return paper
    rich = CONTENT.get(paper.get("id"))
    if not rich:
        return paper
    enriched = dict(paper)
    for k, v in rich.items():
        if v in (None, ""):
            continue
        if k == "tags" and isinstance(v, list):
            existing = enriched.get("tags") or []
            enriched[k] = list(dict.fromkeys(list(v) + list(existing)))
        else:
            enriched[k] = v
    return enriched


# ============================================================
# HTML rendering（PD/曜日レポートの構造を流用、teal テーマ）
# ============================================================

def _nav_html() -> str:
    return f"""<!-- INJECTED-NAV-V1 -->
<div style="position:sticky;top:0;z-index:1000;background:#fff;border-bottom:1px solid #e2e8f0;padding:10px 18px;font-family:-apple-system,BlinkMacSystemFont,'Hiragino Kaku Gothic ProN','Hiragino Sans','Helvetica Neue',Arial,sans-serif;font-size:14px;display:flex;align-items:center;gap:14px;flex-wrap:wrap">
  <a href="../index.html" style="color:#475569;text-decoration:none;font-weight:600">← ダッシュボード</a>
  <a href="../papers.html" style="color:#475569;text-decoration:none">論文一覧</a>
  <a href="../themes.html" style="color:#475569;text-decoration:none">曜日テーマ</a>
  <a href="../pd.html" style="color:#475569;text-decoration:none">📍 PD研究</a>
  <a href="../other.html" style="color:{THEME_COLOR};text-decoration:none;font-weight:600">🗂 その他</a>
  <a href="../favorites.html" style="color:#475569;text-decoration:none">★ お気に入り</a>
  <span style="margin-left:auto;color:#94a3b8;font-size:12px">その他 キュレーション版</span>
</div>
"""


INLINE_CSS = """
body { font-family: -apple-system, BlinkMacSystemFont, "Hiragino Kaku Gothic ProN", "Hiragino Sans", sans-serif;
  margin: 0; padding: 0; background: #f8fafc; color: #0f172a; line-height: 1.7; }
.report-wrapper { max-width: 980px; margin: 0 auto; padding: 24px 20px 80px; }
.report-header { background: #fff; border: 1px solid #e2e8f0; border-radius: 10px;
  padding: 22px 24px; margin-bottom: 24px; position: relative; overflow: hidden;
  box-shadow: 0 4px 16px rgba(15,23,42,0.06); }
.report-header::before { content: ""; position: absolute; top: 0; left: 0; right: 0;
  height: 4px; background: #0d9488; }
.report-header h1 { margin: 0 0 6px; font-size: 26px; letter-spacing: -0.02em; }
.report-header .meta { color: #475569; font-size: 14px; }
.paper-card { background: #fff; border: 1px solid #e2e8f0; border-radius: 10px;
  padding: 22px 24px; margin-bottom: 16px; box-shadow: 0 1px 2px rgba(15,23,42,0.04); }
.paper-rank { display: inline-block; background: #0d9488; color: white; font-weight: 700;
  font-size: 13px; padding: 3px 10px; border-radius: 999px; margin-right: 8px; }
.task-tag { display: inline-block; background: #0d9488; color: white; font-size: 11px;
  padding: 2px 8px; border-radius: 999px; font-weight: 700; }
.task-tag.other { background: #0d9488; }
.paper-title { font-size: 17px; font-weight: 700; margin: 8px 0 6px; line-height: 1.4; }
.paper-title a { color: #0f172a; text-decoration: none; }
.paper-title a:hover { color: #2563eb; }
.paper-meta { color: #475569; font-size: 13px; margin-bottom: 16px; }
.section-block { border-left: 4px solid currentColor; padding: 10px 14px; margin: 12px 0;
  background: #f1f5f9; border-radius: 0 6px 6px 0; color: #0f172a; }
.section-block .section-label { display: inline-block; font-size: 12px; font-weight: 700;
  letter-spacing: 0.04em; margin-bottom: 6px; }
.section-block .section-content { font-size: 14px; }
.section-block.summary     { color: #3182ce; } .section-block.summary .section-label     { color: #3182ce; }
.section-block.overview    { color: #718096; } .section-block.overview .section-label    { color: #718096; }
.section-block.importance  { color: #d69e2e; } .section-block.importance .section-label  { color: #d69e2e; }
.section-block.originality { color: #805ad5; } .section-block.originality .section-label { color: #805ad5; }
.section-block.discovery   { color: #16a34a; } .section-block.discovery .section-label   { color: #16a34a; }
.section-block.method      { color: #38a169; } .section-block.method .section-label      { color: #38a169; }
.section-block.limit       { color: #c53030; } .section-block.limit .section-label       { color: #c53030; }
.section-block.citation    { color: #805ad5; } .section-block.citation .section-label    { color: #805ad5; }
.section-block.implication { color: #805ad5; } .section-block.implication .section-label { color: #805ad5; }
.section-block.idea        { color: #319795; } .section-block.idea .section-label        { color: #319795; }
.section-block .section-content { color: #0f172a; line-height: 1.8; }
.tag-list { margin-top: 12px; font-size: 11px; color: #64748b; }
.tag-list .tag { display: inline-block; background: #f1f5f9; padding: 2px 8px; border-radius: 999px; margin-right: 4px; }
.fav-checkbox { float: right; font-size: 13px; color: #475569; cursor: pointer; user-select: none; }
.fav-checkbox input { vertical-align: middle; margin-right: 4px; }
"""

SECTION_DEFS = [
    ("summary",     "▎一言要約",                "summary"),
    ("overview",    "▎研究概要",                "overview"),
    ("importance",  "▎重要な点",                "importance"),
    ("originality", "▎オリジナリティ（独自性）", "originality"),
    ("discovery",   "▎新発見項目（新しく分かったこと）", "discovery"),
    ("methodology", "▎方法論評価",              "method"),
    ("limitation",  "▎限界",                    "limit"),
    ("citation",    "▎どんな引用に使えるか",    "citation"),
    ("implication", "▎研究への示唆",            "implication"),
    ("idea",        "▎研究アイデア",            "idea"),
]


def _format_discovery(text: str) -> str:
    if not text:
        return ""
    if re.search(r"[①-⑩]", text):
        parts = re.split(r"(?=[①-⑩])", text)
        return "<br>".join(html.escape(p.strip()) for p in parts if p.strip())
    return html.escape(text)


def render_paper_card(rank: int, paper: dict) -> str:
    pid = paper.get("id", "")
    title = html.escape(paper.get("title", "(タイトル不明)"))
    authors = html.escape(paper.get("authors", ""))
    journal = html.escape(paper.get("journal", ""))
    design = html.escape(paper.get("design", ""))
    url = html.escape(paper.get("url", "#"))

    data_attrs = " ".join([
        f'data-paper-id="{html.escape(pid)}"',
        f'data-title="{html.escape(paper.get("title",""))}"',
        f'data-authors="{html.escape(paper.get("authors",""))}"',
        f'data-journal="{html.escape(paper.get("journal",""))}"',
        f'data-design="{html.escape(paper.get("design",""))}"',
        f'data-url="{html.escape(paper.get("url",""))}"',
        f'data-summary="{html.escape(paper.get("summary",""))}"',
        f'data-methodology="{html.escape(paper.get("methodology",""))}"',
        f'data-limitation="{html.escape(paper.get("limitation",""))}"',
        f'data-implication="{html.escape(paper.get("implication",""))}"',
        f'data-idea="{html.escape(paper.get("idea",""))}"',
        f'data-novelty="{html.escape(paper.get("novelty",""))}"',
        f'data-background="{html.escape(paper.get("background",""))}"',
        f'data-result="{html.escape(paper.get("result",""))}"',
        f'data-impact="{html.escape(paper.get("impact",""))}"',
        f'data-keywords="{html.escape(paper.get("keywords",""))}"',
        f'data-tags="{html.escape("|".join(paper.get("tags", []) or []))}"',
    ])

    sections_html = ""
    for field, label, css_class in SECTION_DEFS:
        val = paper.get(field, "")
        if not val or not str(val).strip():
            continue
        content_html = _format_discovery(str(val)) if field == "discovery" else html.escape(str(val))
        sections_html += f"""
    <div class="section-block {css_class}">
      <div class="section-label">{label}</div>
      <div class="section-content">{content_html}</div>
    </div>"""

    meta_parts = []
    if authors:
        meta_parts.append(authors)
    if journal:
        meta_parts.append(f"<i>{journal}</i>")
    if design:
        meta_parts.append(design)
    meta_line = " · ".join(meta_parts)

    tags = paper.get("tags", []) or []
    tags_html = ""
    if tags:
        tags_html = '<div class="tag-list">' + "".join(
            f'<span class="tag">{html.escape(t)}</span>' for t in tags
        ) + "</div>"

    return f"""
  <div class="paper-card" {data_attrs}>
    <label class="fav-checkbox"><input type="checkbox" class="fav-toggle" data-pid="{html.escape(pid)}"> お気に入り</label>
    <span class="paper-rank">#{rank}</span>
    <span class="task-tag other">🗂 その他</span>
    <h2 class="paper-title"><a href="{url}" target="_blank" rel="noopener">{title}</a></h2>
    <p class="paper-meta">{meta_line}</p>
    {sections_html}
    {tags_html}
  </div>
"""


def render_report(date_str: str, topic: str, papers: list[dict]) -> str:
    fmt_date = f"{date_str[:4]}年{int(date_str[4:6])}月{int(date_str[6:8])}日"
    paper_cards = "\n".join(render_paper_card(i + 1, p) for i, p in enumerate(papers))
    topic_esc = html.escape(topic)

    return f"""<!DOCTYPE html>
<html lang="ja">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>その他（{topic_esc}）— {fmt_date}</title>
<style>{INLINE_CSS}</style>
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'%3E%3Crect width='100' height='100' rx='22' fill='%230d9488'/%3E%3Ctext x='50' y='68' text-anchor='middle' font-size='52' fill='white'%3E%F0%9F%97%82%3C/text%3E%3C/svg%3E">
</head>
<body data-source-date="{date_str}" data-source-theme="{THEME_EN}" data-topic="{topic_esc}">
{_nav_html()}
<div class="report-wrapper">

  <div class="report-header">
    <h1>🗂 その他 — {topic_esc}</h1>
    <p class="meta">{fmt_date} ・ 依頼テーマ「{topic_esc}」のキュレーション論文{len(papers)}本</p>
  </div>

{paper_cards}

</div>
<script src="../js/favorites.js"></script>
<script>
document.querySelectorAll('.fav-toggle').forEach(cb => {{
  const pid = cb.dataset.pid;
  if (Favorites.has(pid)) cb.checked = true;
  cb.addEventListener('change', () => {{
    const card = cb.closest('.paper-card');
    const ds = card.dataset;
    const paper = {{
      id: ds.paperId, title: ds.title, authors: ds.authors, journal: ds.journal,
      design: ds.design, url: ds.url, summary: ds.summary, methodology: ds.methodology,
      limitation: ds.limitation, implication: ds.implication, idea: ds.idea, novelty: ds.novelty,
      background: ds.background, result: ds.result, impact: ds.impact, keywords: ds.keywords,
      tags: (ds.tags || "").split("|").filter(Boolean),
      source_reports: ["{date_str}_{THEME_KEY}"],
      is_pd_related: false,
      first_seen_date: "{date_str[:4]}-{date_str[4:6]}-{date_str[6:8]}",
    }};
    if (cb.checked) Favorites.add(paper); else Favorites.remove(pid);
  }});
}});
</script>
</body>
</html>"""


# ============================================================
# 検証（SKILL.md rev7/rev9-15）
# ============================================================

def _run_validator(script_name: str, label: str, fail_msg: str):
    import subprocess
    import sys
    content_file = REPO / "scripts" / f"{THEME_KEY}_curated_content.py"
    print(f"{label} ({content_file.name})...")
    result = subprocess.run(
        ["python3", str(REPO / "scripts" / script_name), str(content_file)],
        capture_output=True, text=True,
    )
    if result.returncode != 0:
        print(result.stdout)
        print(result.stderr, file=sys.stderr)
        print(fail_msg, file=sys.stderr)
        sys.exit(1)
    print(result.stdout.strip().splitlines()[-1] if result.stdout.strip() else "OK")
    print()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--date", default=datetime.now().strftime("%Y%m%d"))
    ap.add_argument("--topic", default=None,
                    help="依頼テーマ名（ヘッダー表示・reports.json 記録用）")
    ap.add_argument("--skip-url-check", action="store_true")
    args = ap.parse_args()

    if not args.skip_url_check:
        _run_validator("validate_urls.py", "🔍 URL validation",
                       "\n❌ URL validation failed. fabricated URL を修正してください。")
        _run_validator("validate_quality.py", "📋 質要件検証",
                       "\n❌ 質要件未達。SKILL.md rev9-15 に従って修正してください。")

    topic = _load_topic(args.topic)
    papers = json.loads(PAPERS_PATH.read_text(encoding="utf-8"))
    reports = json.loads(REPORTS_JSON_PATH.read_text(encoding="utf-8"))
    rep_by_id = {r["id"]: r for r in reports}

    report_id = f"{args.date}_{THEME_KEY}"
    selected = select_papers(papers, rep_by_id, n=10, report_id=report_id)
    selected_enriched = [merge_curated_content(p) for p in selected]

    REPORTS_DIR.mkdir(parents=True, exist_ok=True)
    out_path = REPORTS_DIR / f"{report_id}.html"
    out_path.write_text(render_report(args.date, topic, selected_enriched), encoding="utf-8")
    print(f"✅ wrote {out_path}")

    # idempotent cleanup
    for p in papers:
        srcs = p.get("source_reports") or []
        if report_id in srcs:
            p["source_reports"] = [s for s in srcs if s != report_id]

    paper_index = {p["id"]: p for p in papers}
    enriched_index = {p["id"]: p for p in selected_enriched}
    new_papers_added = 0
    for pid in enriched_index.keys():
        rich = enriched_index[pid]
        is_new = rich.pop("_is_new", False)
        if is_new and pid not in paper_index:
            new_paper = {k: v for k, v in rich.items() if k != "_is_new"}
            new_paper["source_reports"] = [report_id]
            papers.append(new_paper)
            paper_index[pid] = new_paper
            new_papers_added += 1
        else:
            base = paper_index[pid]
            for k, v in rich.items():
                if k == "_is_new" or k == "source_reports":
                    continue
                if v in (None, ""):
                    continue
                if k == "tags" and isinstance(v, list):
                    base[k] = list(dict.fromkeys(v + (base.get(k) or [])))
                else:
                    base[k] = v
            srcs = base.setdefault("source_reports", [])
            if report_id not in srcs:
                srcs.append(report_id)
    PAPERS_PATH.write_text(json.dumps(papers, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"✅ updated papers.json (added {new_papers_added} new papers, total now {len(papers)})")

    new_report = {
        "id": report_id,
        "date": f"{args.date[:4]}-{args.date[4:6]}-{args.date[6:8]}",
        "weekday": THEME_KEY,
        "theme_jp": THEME_JP,
        "theme_en": THEME_EN,
        "topic_label": topic,
        "report_type": "regular",
        "source_html_path": f"docs/reports/{report_id}.html",
        "paper_ids": [p["id"] for p in selected_enriched],
        "paper_count": len(selected_enriched),
    }
    reports = [r for r in reports if r["id"] != report_id]
    reports.append(new_report)
    REPORTS_JSON_PATH.write_text(json.dumps(reports, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"✅ updated reports.json (id: {report_id}, topic: {topic}, {len(selected_enriched)} papers)")

    print("\n=== Selected papers ===")
    for i, p in enumerate(selected_enriched, 1):
        print(f"  {i:2d}. [{p['id']}] {p['title'][:70]}")


if __name__ == "__main__":
    main()
