#!/usr/bin/env python3
"""
Daily Research Report Generator (cloud-runnable)
================================================

Runs in GitHub Actions every day at 8:00 JST. Searches PubMed + bioRxiv for the
day's theme, asks Claude to rank/explain top-10 papers (with ≥2 PD-related),
renders an HTML report, and updates papers.json / reports.json.

Usage:
    python scripts/daily_generator.py [--weekday monday] [--type regular|pd_focused] [--dry-run]

Env vars:
    ANTHROPIC_API_KEY  required
    NCBI_API_KEY       optional (PubMed faster rate-limit)
    USE_OPUS=1         optional (use Opus 4.7 instead of Sonnet 4.6)
"""
from __future__ import annotations

import argparse
import hashlib
import html as html_lib
import json
import os
import re
import sys
import time
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any
from xml.etree import ElementTree as ET

import requests
from anthropic import Anthropic

# ---------- paths ----------
REPO = Path(__file__).resolve().parent.parent
DATA_DIR = REPO / "docs" / "data"
REPORTS_DIR = REPO / "docs" / "reports"
THEMES_PATH = REPO / "scripts" / "themes.json"
TEMPLATE_PATH = REPO / "skills" / "daily-research-report" / "templates" / "regular-report.html"

JST = timezone(timedelta(hours=9))

WEEKDAY_ORDER = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]


# ============================================================
# 1. Theme config
# ============================================================

def load_themes() -> dict[str, Any]:
    return json.loads(THEMES_PATH.read_text(encoding="utf-8"))


def determine_weekday() -> str:
    return WEEKDAY_ORDER[datetime.now(JST).weekday()]


# ============================================================
# 2. PubMed (NCBI E-utilities)
# ============================================================

PUBMED_ESEARCH = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
PUBMED_EFETCH = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi"

def search_pubmed(query: str, days_back: int = 21, max_results: int = 30) -> list[dict]:
    """Return list of paper dicts from PubMed."""
    api_key = os.getenv("NCBI_API_KEY")
    today = datetime.now(JST)
    start = today - timedelta(days=days_back)
    date_filter = f' AND ("{start.strftime("%Y/%m/%d")}"[PDAT] : "{today.strftime("%Y/%m/%d")}"[PDAT])'

    params = {
        "db": "pubmed",
        "term": query + date_filter,
        "retmax": str(max_results),
        "sort": "date",
        "retmode": "json",
    }
    if api_key: params["api_key"] = api_key

    try:
        r = requests.get(PUBMED_ESEARCH, params=params, timeout=20)
        r.raise_for_status()
        ids = r.json().get("esearchresult", {}).get("idlist", [])
    except Exception as e:
        print(f"  PubMed esearch failed: {e}", file=sys.stderr)
        return []

    if not ids: return []

    fetch_params = {"db": "pubmed", "id": ",".join(ids), "retmode": "xml"}
    if api_key: fetch_params["api_key"] = api_key
    try:
        r = requests.get(PUBMED_EFETCH, params=fetch_params, timeout=30)
        r.raise_for_status()
    except Exception as e:
        print(f"  PubMed efetch failed: {e}", file=sys.stderr)
        return []

    return parse_pubmed_xml(r.text)


def parse_pubmed_xml(xml_text: str) -> list[dict]:
    out = []
    try:
        root = ET.fromstring(xml_text)
    except ET.ParseError as e:
        print(f"  PubMed XML parse failed: {e}", file=sys.stderr)
        return out
    for art in root.findall(".//PubmedArticle"):
        try:
            pmid = art.findtext(".//PMID") or ""
            title = (art.findtext(".//ArticleTitle") or "").strip()
            journal = (art.findtext(".//Journal/Title") or art.findtext(".//Journal/ISOAbbreviation") or "").strip()
            year = art.findtext(".//PubDate/Year") or art.findtext(".//PubDate/MedlineDate") or ""
            year = year[:4] if year else ""
            authors = []
            for a in art.findall(".//Author"):
                ln = a.findtext("LastName") or ""
                fn = a.findtext("Initials") or ""
                if ln: authors.append(f"{ln} {fn}".strip())
            authors_str = ", ".join(authors[:3]) + (" et al." if len(authors) > 3 else "")
            abstract = " ".join((t.text or "") for t in art.findall(".//AbstractText")).strip()
            doi = ""
            for aid in art.findall(".//ArticleId"):
                if aid.get("IdType") == "doi": doi = aid.text or ""
            url = f"https://doi.org/{doi}" if doi else f"https://pubmed.ncbi.nlm.nih.gov/{pmid}/"
            out.append({
                "source": "pubmed", "pmid": pmid, "doi": doi, "url": url,
                "title": title, "authors": authors_str,
                "journal": f"{journal}{', ' + year if year else ''}",
                "abstract": abstract,
            })
        except Exception as e:
            print(f"  pubmed parse skip: {e}", file=sys.stderr)
    return out


# ============================================================
# 3. bioRxiv API
# ============================================================

def search_biorxiv(categories: list[str], days_back: int = 14, max_results: int = 30) -> list[dict]:
    today = datetime.now(JST)
    start = today - timedelta(days=days_back)
    interval = f"{start.strftime('%Y-%m-%d')}/{today.strftime('%Y-%m-%d')}"

    out = []
    for server in ("biorxiv", "medrxiv"):
        try:
            r = requests.get(f"https://api.biorxiv.org/details/{server}/{interval}/0", timeout=20)
            r.raise_for_status()
            data = r.json().get("collection", [])
            for it in data:
                cat = (it.get("category") or "").lower()
                if categories and not any(c.lower() in cat for c in categories):
                    continue
                doi = it.get("doi", "")
                out.append({
                    "source": server, "pmid": "", "doi": doi,
                    "url": f"https://doi.org/{doi}" if doi else f"https://www.{server}.org/",
                    "title": (it.get("title") or "").strip(),
                    "authors": (it.get("authors") or "")[:200],
                    "journal": f"{server}, preprint, {it.get('date', '')}",
                    "abstract": (it.get("abstract") or "").strip(),
                })
                if len(out) >= max_results: break
        except Exception as e:
            print(f"  {server} fetch failed: {e}", file=sys.stderr)
        if len(out) >= max_results: break
    return out[:max_results]


# ============================================================
# 4. PD relevance heuristic
# ============================================================

def is_pd_related(paper: dict, pd_keywords: list[str]) -> bool:
    text = f"{paper.get('title', '')} {paper.get('abstract', '')}".lower()
    return any(kw.lower() in text for kw in pd_keywords)


# ============================================================
# 5. Claude — rank top-10 + write 10-section content
# ============================================================

MODEL = "claude-opus-4-7-20250514" if os.getenv("USE_OPUS") == "1" else "claude-sonnet-4-6-20250514"

SYSTEM_PROMPT = """You are a research librarian and methodology expert. You assist
浅野優次郎 (Yujiro Asano), a PhD researcher at Tohoku University focusing on:
- Geriatrics, sports physiology, epidemiology
- Healthy aging, healthspan, multifaceted health (cognitive + physical + functional)
- His PD research project: brain-muscle relationships, EEG during exercise, SHAP-based
  feature importance for physical function, sarcopenia + cognition

Critical output rules:
- Always respond in Japanese (日本語) unless user asks otherwise.
- Use research-grade depth — assume the reader is a PhD epidemiologist.
- Always include critical perspectives (limitations, biases, alternative explanations)
  alongside positive points.
- Be concise but specific."""


def call_claude(client: Anthropic, system: str, user: str, max_tokens: int = 4000) -> str:
    """Single Claude call with prompt caching on the system block."""
    resp = client.messages.create(
        model=MODEL,
        max_tokens=max_tokens,
        system=[{"type": "text", "text": system, "cache_control": {"type": "ephemeral"}}],
        messages=[{"role": "user", "content": user}],
    )
    return "".join(b.text for b in resp.content if hasattr(b, "text"))


def rank_top10(client: Anthropic, candidates: list[dict], theme_jp: str, is_pd_focused: bool) -> list[int]:
    """Return list of indices into candidates for top-10."""
    if len(candidates) <= 10:
        return list(range(len(candidates)))

    summary = "\n\n".join(
        f"[{i}] {p['title']}\n  Journal: {p['journal']}\n  Source: {p['source']}\n  PD-related: {p.get('pd', False)}\n  Abstract: {p['abstract'][:600]}"
        for i, p in enumerate(candidates)
    )

    pd_constraint = (
        "全10本ともPD研究計画関連（脳-身体機能・EEG・SHAP・筋質と認知）に強く関連するもの"
        if is_pd_focused else
        "10本中【2本以上】はPD研究計画関連（脳-身体機能・EEG・SHAP・筋質と認知）"
    )

    prompt = f"""今日のテーマ: {theme_jp}

以下の候補論文から、トップ10を選んでください。

選定基準（重要度順）：
1. {pd_constraint}
2. 研究デザイン: メタ解析 > 大規模コホート > 因果推論 > RCT > 観察研究
3. 高インパクトジャーナル優先（Nature/Cell/Lancet/JAMA系、専門誌のトップ）
4. 症例報告・小規模研究・基礎のみは除外
5. 浅野の関心：高齢者の健康全般・健康寿命・身体機能・認知機能・健康寿命

候補:
{summary}

出力形式: トップ10の論文インデックスのみをJSONの配列で返してください。例: [3, 7, 12, 0, 5, 9, 14, 1, 8, 22]
余計な説明は不要。JSONの配列だけ。"""

    raw = call_claude(client, SYSTEM_PROMPT, prompt, max_tokens=300)
    m = re.search(r"\[[\d,\s]+\]", raw)
    if not m:
        print(f"  WARN: ranking returned non-JSON, fallback to first 10. Raw: {raw[:200]}", file=sys.stderr)
        return list(range(min(10, len(candidates))))
    try:
        idxs = json.loads(m.group(0))
        return [i for i in idxs if 0 <= i < len(candidates)][:10]
    except Exception as e:
        print(f"  WARN: ranking JSON parse failed: {e}", file=sys.stderr)
        return list(range(min(10, len(candidates))))


SECTION_DEFS = [
    ("summary",     "▎一言要約",     "3〜4文で論文の核心を述べる。"),
    ("overview",    "▎研究概要",     "5〜6文。デザイン、対象、主要指標、結果。"),
    ("importance",  "▎重要な点",     "3〜4文。なぜこの研究が重要か。"),
    ("originality", "▎オリジナリティ", "3〜4文。新規性・既存研究との違い。"),
    ("discovery",   "▎新発見項目",   "5〜6項目。①②③形式で。"),
    ("method",      "▎方法論評価",   "2〜3文。強み・適切さ。"),
    ("limit",       "▎限界",         "2〜3文。残余交絡・サンプル代表性など。"),
    ("citation",    "▎どんな引用に使えるか", "introduction引用例＋discussion引用例（各2〜3文）。"),
    ("implication", "▎研究への示唆", "2〜3文。浅野の研究計画にどうつなげるか。"),
    ("idea",        "▎研究アイデア", "2〜3文。具体的な解析・コホート活用案。"),
]


def write_sections(client: Anthropic, paper: dict, theme_jp: str, paper_idx: int) -> dict:
    """Generate the 10-section content + tags + design + summary fields for one paper."""
    paper_meta = (
        f"Title: {paper['title']}\n"
        f"Authors: {paper['authors']}\n"
        f"Journal: {paper['journal']}\n"
        f"DOI/URL: {paper.get('url','')}\n"
        f"Abstract: {paper['abstract']}\n"
    )

    section_spec = "\n".join(f"  {i+1}. {label} ({key}): {hint}" for i, (key, label, hint) in enumerate(SECTION_DEFS))

    prompt = f"""論文 #{paper_idx+1}（テーマ: {theme_jp}）について、以下の10セクション
すべての本文を生成してください。各セクションは独立に書く。

論文情報:
{paper_meta}

10セクション:
{section_spec}

加えて、以下のメタ情報も生成：
  research_design: 研究デザインを20字以内で（例: "縦断観察コホート（n=12,345、5年追跡）"）
  tags: 5〜7個のキーワードタグの配列（日本語）

出力形式: 純粋なJSONオブジェクト。バッククォートやMarkdownなし。
{{
  "summary": "...", "overview": "...", "importance": "...", "originality": "...",
  "discovery": "①〜①〜...", "method": "...", "limit": "...", "citation": "...",
  "implication": "...", "idea": "...",
  "research_design": "...",
  "tags": ["tag1", "tag2", ...]
}}"""

    raw = call_claude(client, SYSTEM_PROMPT, prompt, max_tokens=3000)
    # Extract JSON
    m = re.search(r"\{[\s\S]*\}", raw)
    if not m:
        print(f"  WARN: paper #{paper_idx+1} sections raw not JSON: {raw[:200]}", file=sys.stderr)
        return _empty_sections()
    try:
        return json.loads(m.group(0))
    except json.JSONDecodeError as e:
        print(f"  WARN: paper #{paper_idx+1} JSON decode: {e}", file=sys.stderr)
        return _empty_sections()


def _empty_sections() -> dict:
    return {k: "" for k, _, _ in SECTION_DEFS} | {"research_design": "", "tags": []}


# ============================================================
# 6. HTML rendering
# ============================================================

SECTION_COLORS = {
    "summary": "#3182ce", "overview": "#718096", "importance": "#d69e2e",
    "originality": "#805ad5", "discovery": "#16a34a", "method": "#38a169",
    "limit": "#c53030", "citation": "#805ad5", "implication": "#805ad5", "idea": "#319795",
}


def html_escape(s: str) -> str:
    return html_lib.escape(s or "", quote=True)


def stable_id(title: str, journal: str) -> str:
    h = hashlib.sha1(f"{title}|{journal}".encode("utf-8")).hexdigest()
    return h[:12]


def render_paper_card(idx: int, paper: dict, sections: dict, is_pd: bool, theme_color: str) -> str:
    pid = stable_id(paper["title"], paper["journal"])
    pd_badge = '<span class="task-tag pd">📍 PD研究</span>' if is_pd else ""
    rank_badge = f'<span class="rank-badge">#{idx+1}</span>'
    tags = sections.get("tags", []) or []
    tags_str = "|".join(tags)

    blocks = []
    for key, label, _ in SECTION_DEFS:
        content = sections.get(key, "") or ""
        if not content: continue
        blocks.append(f'''
        <div class="section-block {key}" style="border-left-color:{SECTION_COLORS[key]};">
          <span class="section-label" style="color:{SECTION_COLORS[key]};">{label}</span>
          <div class="section-content">{html_escape(content).replace(chr(10), "<br>")}</div>
        </div>''')

    section_html = "".join(blocks)

    return f'''
<article class="paper-card"
         data-paper-id="{pid}"
         data-title="{html_escape(paper['title'])}"
         data-authors="{html_escape(paper['authors'])}"
         data-journal="{html_escape(paper['journal'])}"
         data-design="{html_escape(sections.get('research_design', ''))}"
         data-url="{html_escape(paper.get('url', ''))}"
         data-summary="{html_escape(sections.get('summary', ''))}"
         data-overview="{html_escape(sections.get('overview', ''))}"
         data-importance="{html_escape(sections.get('importance', ''))}"
         data-methodology="{html_escape(sections.get('method', ''))}"
         data-limitation="{html_escape(sections.get('limit', ''))}"
         data-implication="{html_escape(sections.get('implication', ''))}"
         data-idea="{html_escape(sections.get('idea', ''))}"
         data-novelty="{html_escape(sections.get('originality', ''))}"
         data-background=""
         data-result="{html_escape(sections.get('discovery', ''))}"
         data-impact="{html_escape(sections.get('citation', ''))}"
         data-keywords="{html_escape(','.join(tags))}"
         data-tags="{html_escape(tags_str)}"
         style="border-top:4px solid {theme_color};padding:24px;margin:18px 0;background:#fff;border-radius:10px;box-shadow:0 2px 8px rgba(15,23,42,0.05);">
  <div style="display:flex;align-items:flex-start;gap:12px;margin-bottom:8px;">
    {rank_badge} {pd_badge}
    <label style="display:inline-flex;align-items:center;gap:6px;margin-left:auto;font-size:13px;color:#475569">
      <input type="checkbox" class="favorite-checkbox" data-paper-id="{pid}"> お気に入り
    </label>
  </div>
  <h2 class="paper-title" style="font-size:18px;margin:6px 0;line-height:1.5;">
    <a href="{html_escape(paper.get('url', '#'))}" target="_blank" rel="noopener" style="color:#0f172a;text-decoration:none;">
      {html_escape(paper['title'])}
    </a>
  </h2>
  <p class="paper-meta" style="color:#475569;font-size:13px;margin-bottom:6px;">
    {html_escape(paper['authors'])} · <i>{html_escape(paper['journal'])}</i>
    {' · ' + html_escape(sections.get('research_design', '')) if sections.get('research_design') else ''}
  </p>
  {section_html}
</article>'''


def render_summary_table(papers_with_sections: list[tuple[dict, dict, bool]]) -> str:
    rows = []
    for i, (paper, sec, is_pd) in enumerate(papers_with_sections):
        title = html_escape(paper["title"])
        rows.append(f'''<tr>
          <td>{i+1}</td>
          <td>{title}{' <span class="task-tag pd">📍</span>' if is_pd else ''}</td>
          <td>{html_escape(paper['journal'])}</td>
          <td>{html_escape(sec.get('research_design', ''))}</td>
          <td>{html_escape((sec.get('summary', '') or '')[:100])}…</td>
        </tr>''')
    return f'''
<h2 style="margin-top:32px">まとめ一覧表</h2>
<table style="width:100%;border-collapse:collapse;font-size:13px">
  <thead><tr style="background:#f1f5f9">
    <th style="padding:8px;border:1px solid #e2e8f0">#</th>
    <th style="padding:8px;border:1px solid #e2e8f0;text-align:left">タイトル</th>
    <th style="padding:8px;border:1px solid #e2e8f0;text-align:left">ジャーナル</th>
    <th style="padding:8px;border:1px solid #e2e8f0;text-align:left">デザイン</th>
    <th style="padding:8px;border:1px solid #e2e8f0;text-align:left">要約</th>
  </tr></thead>
  <tbody>{''.join(rows)}</tbody>
</table>'''


def render_full_html(theme_jp: str, theme_en: str, theme_color: str, date_str: str,
                     report_type: str, paper_cards_html: str, summary_table_html: str) -> str:
    title = f"{date_str} {theme_jp}"
    if report_type == "pd_focused":
        title += " — PD研究特化"
    return f'''<!DOCTYPE html>
<html lang="ja">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<link rel="stylesheet" href="../css/report.css">
<meta property="og:title" content="{title}">
<meta property="og:description" content="毎朝8:00自動生成の研究論文レポート">
<meta property="og:type" content="article">
</head>
<body data-source-date="{date_str.replace('-', '')}" data-source-theme="{theme_en}" style="background:#f8fafc;color:#0f172a;font-family:-apple-system,BlinkMacSystemFont,'Hiragino Kaku Gothic ProN','Helvetica Neue',Arial,sans-serif;margin:0;padding:0;">
<!-- INJECTED-NAV-V1 -->
<div style="position:sticky;top:0;z-index:1000;background:#fff;border-bottom:1px solid #e2e8f0;padding:10px 18px;font-size:14px;display:flex;align-items:center;gap:14px;flex-wrap:wrap">
  <a href="../index.html" style="color:#475569;text-decoration:none;font-weight:600">← ダッシュボード</a>
  <a href="../papers.html" style="color:#475569;text-decoration:none">論文一覧</a>
  <a href="../themes.html" style="color:#475569;text-decoration:none">曜日テーマ</a>
  <a href="../favorites.html" style="color:#475569;text-decoration:none">★ お気に入り</a>
  <span style="margin-left:auto;color:#94a3b8;font-size:12px">📅 {date_str}</span>
</div>

<div class="report-wrapper" style="max-width:980px;margin:0 auto;padding:24px 20px 80px;">
  <header class="report-header" style="--theme-color:{theme_color}">
    <h1 style="margin:0 0 6px;font-size:26px;letter-spacing:-0.02em;color:{theme_color}">{theme_jp}</h1>
    <p class="meta">{date_str} ／ {report_type} ／ 10論文</p>
  </header>

  {paper_cards_html}

  {summary_table_html}
</div>

<script src="../js/favorites.js"></script>
<script>
// Auto-add to favorites on checkbox tick
document.querySelectorAll(".favorite-checkbox").forEach(cb => {{
  const pid = cb.dataset.paperId;
  const card = cb.closest(".paper-card");
  cb.checked = Favorites.has(pid);
  cb.addEventListener("change", () => {{
    if (cb.checked) {{
      Favorites.add({{
        id: pid,
        title: card.dataset.title,
        authors: card.dataset.authors,
        journal: card.dataset.journal,
        design: card.dataset.design,
        url: card.dataset.url,
        summary: card.dataset.summary,
        overview: card.dataset.overview,
        importance: card.dataset.importance,
        methodology: card.dataset.methodology,
        limitation: card.dataset.limitation,
        implication: card.dataset.implication,
        idea: card.dataset.idea,
        novelty: card.dataset.novelty,
        background: card.dataset.background,
        result: card.dataset.result,
        impact: card.dataset.impact,
        keywords: card.dataset.keywords,
        tags: (card.dataset.tags || "").split("|").filter(Boolean),
        is_pd_related: !!card.querySelector(".task-tag.pd"),
        source_reports: ["{date_str.replace('-', '')}_{theme_en}"],
        first_seen_date: "{date_str}"
      }});
    }} else {{
      Favorites.remove(pid);
    }}
  }});
}});
</script>
</body>
</html>'''


# ============================================================
# 7. JSON state updater
# ============================================================

def update_papers_json(papers: list[dict], sections_list: list[dict], pd_flags: list[bool],
                       report_id: str, date_str: str) -> list[dict]:
    """Read papers.json, append/merge new papers, write back. Return all paper objects in this report."""
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    pj_path = DATA_DIR / "papers.json"
    existing = json.loads(pj_path.read_text(encoding="utf-8")) if pj_path.exists() else []
    by_id = {p["id"]: p for p in existing}

    paper_ids = []
    for paper, sec, is_pd in zip(papers, sections_list, pd_flags):
        pid = stable_id(paper["title"], paper["journal"])
        paper_ids.append(pid)
        new = {
            "id": pid, "title": paper["title"], "authors": paper["authors"],
            "journal": paper["journal"], "design": sec.get("research_design", ""),
            "url": paper.get("url", ""), "summary": sec.get("summary", ""),
            "overview": sec.get("overview", ""), "importance": sec.get("importance", ""),
            "methodology": sec.get("method", ""), "limitation": sec.get("limit", ""),
            "implication": sec.get("implication", ""), "idea": sec.get("idea", ""),
            "novelty": sec.get("originality", ""), "background": "",
            "result": sec.get("discovery", ""), "impact": sec.get("citation", ""),
            "keywords": ",".join(sec.get("tags", [])),
            "tags": sec.get("tags", []),
            "source_reports": [report_id], "is_pd_related": is_pd,
            "first_seen_date": date_str,
        }
        if pid in by_id:
            old = by_id[pid]
            old["source_reports"] = list(set((old.get("source_reports") or []) + [report_id]))
            for f in ("novelty", "background", "result", "impact", "keywords"):
                if not old.get(f) and new.get(f): old[f] = new[f]
            old["is_pd_related"] = old.get("is_pd_related") or is_pd
        else:
            by_id[pid] = new

    final = list(by_id.values())
    pj_path.write_text(json.dumps(final, ensure_ascii=False, indent=2), encoding="utf-8")
    return paper_ids


def update_reports_json(report_id: str, date_str: str, weekday: str, theme_jp: str,
                        theme_en: str, report_type: str, paper_ids: list[str]) -> None:
    rj_path = DATA_DIR / "reports.json"
    existing = json.loads(rj_path.read_text(encoding="utf-8")) if rj_path.exists() else []
    existing = [r for r in existing if r.get("id") != report_id]
    existing.append({
        "id": report_id, "date": date_str, "weekday": weekday,
        "theme_jp": theme_jp, "theme_en": theme_en,
        "report_type": report_type,
        "source_html_path": f"docs/reports/{report_id}.html",
        "paper_ids": paper_ids, "paper_count": len(paper_ids),
    })
    rj_path.write_text(json.dumps(existing, ensure_ascii=False, indent=2), encoding="utf-8")


# ============================================================
# 8. Main flow
# ============================================================

def generate_report(weekday: str, report_type: str = "regular", dry_run: bool = False) -> str | None:
    themes = load_themes()
    pd_keywords = themes["_pd_keywords"]["must_match_any"]

    is_pd_focused = (report_type == "pd_focused")
    theme_key = "thursday_pd" if is_pd_focused else weekday
    if theme_key not in themes:
        print(f"  ❌ unknown theme key: {theme_key}", file=sys.stderr)
        return None
    theme = themes[theme_key]

    today = datetime.now(JST)
    date_str = today.strftime("%Y-%m-%d")
    yyyymmdd = today.strftime("%Y%m%d")
    report_id = f"{yyyymmdd}_{weekday}{'_pd' if is_pd_focused else ''}"

    print(f"=== Generating {report_id} ({theme['jp']}) ===")

    # Search
    candidates = []
    for q in theme["pubmed_queries"]:
        time.sleep(0.5)
        candidates.extend(search_pubmed(q, days_back=21, max_results=12))
    for cat in theme.get("biorxiv_categories", []):
        time.sleep(0.5)
        candidates.extend(search_biorxiv([cat], days_back=14, max_results=10))

    # De-dupe by title
    seen = set()
    deduped = []
    for p in candidates:
        key = (p["title"] or "").lower()[:120]
        if not key or key in seen: continue
        seen.add(key)
        deduped.append(p)

    # Tag PD relevance
    for p in deduped:
        p["pd"] = is_pd_related(p, pd_keywords)

    print(f"  Found {len(deduped)} unique candidates ({sum(1 for p in deduped if p['pd'])} PD)")

    if not deduped:
        print("  ⚠️  no candidates — aborting")
        return None

    # Rank
    client = Anthropic()
    top_idxs = rank_top10(client, deduped, theme["jp"], is_pd_focused)
    top_papers = [deduped[i] for i in top_idxs]
    print(f"  Selected top {len(top_papers)}")

    # Generate sections
    sections_list = []
    pd_flags = []
    for i, paper in enumerate(top_papers):
        print(f"  [{i+1}/{len(top_papers)}] writing sections: {paper['title'][:60]}…")
        sec = write_sections(client, paper, theme["jp"], i)
        sections_list.append(sec)
        pd_flags.append(paper.get("pd", False))

    # Render HTML
    cards_html = "\n".join(
        render_paper_card(i, p, s, pd, theme["color"])
        for i, (p, s, pd) in enumerate(zip(top_papers, sections_list, pd_flags))
    )
    summary_html = render_summary_table(list(zip(top_papers, sections_list, pd_flags)))
    full_html = render_full_html(theme["jp"], theme["en"], theme["color"], date_str,
                                  report_type, cards_html, summary_html)

    # Write
    REPORTS_DIR.mkdir(parents=True, exist_ok=True)
    out_path = REPORTS_DIR / f"{report_id}.html"
    if dry_run:
        print(f"  [dry-run] would write {out_path}")
        print(f"  [dry-run] HTML len: {len(full_html)} bytes")
    else:
        out_path.write_text(full_html, encoding="utf-8")
        print(f"  ✅ wrote {out_path}")
        paper_ids = update_papers_json(top_papers, sections_list, pd_flags, report_id, date_str)
        update_reports_json(report_id, date_str, weekday, theme["jp"], theme["en"],
                           report_type, paper_ids)
        print(f"  ✅ updated papers.json + reports.json")

    print(f"  PD-related: {sum(pd_flags)}/{len(pd_flags)}")
    return report_id


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--weekday", choices=WEEKDAY_ORDER + ["auto"], default="auto")
    p.add_argument("--type", choices=["regular", "pd_focused", "auto"], default="auto")
    p.add_argument("--dry-run", action="store_true")
    args = p.parse_args()

    weekday = determine_weekday() if args.weekday == "auto" else args.weekday

    if args.type == "auto":
        # Thursday auto-runs both regular + pd_focused
        if weekday == "thursday":
            generate_report("thursday", "regular", args.dry_run)
            generate_report("thursday", "pd_focused", args.dry_run)
        else:
            generate_report(weekday, "regular", args.dry_run)
    else:
        generate_report(weekday, args.type, args.dry_run)


if __name__ == "__main__":
    if not os.getenv("ANTHROPIC_API_KEY"):
        print("ERROR: ANTHROPIC_API_KEY env var is required", file=sys.stderr)
        sys.exit(1)
    main()
