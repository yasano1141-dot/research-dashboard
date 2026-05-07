#!/usr/bin/env python3
"""
PD研究専用テーマの「キュレーション版」レポートを既存論文から生成。

使い方:
    python scripts/generate_pd_curated_report.py [--date YYYYMMDD]

- papers.json から is_pd_related=true の論文を richness（novelty/background/result/impactの埋まり度）でランク付け
- 上位10本を選定
- HTMLレポートを docs/reports/{YYYYMMDD}_pd.html に生成
- reports.json に新エントリを追記
"""
from __future__ import annotations

import argparse
import html
import json
from datetime import datetime
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
DATA_DIR = REPO / "docs" / "data"
REPORTS_DIR = REPO / "docs" / "reports"

PAPERS_PATH = DATA_DIR / "papers.json"
REPORTS_JSON_PATH = DATA_DIR / "reports.json"


def richness_score(p: dict) -> int:
    """詳細フィールドが埋まっているほど高スコア。"""
    fields = ["summary", "methodology", "limitation", "implication", "idea",
              "novelty", "background", "result", "impact", "keywords"]
    return sum(1 for f in fields if p.get(f) and str(p[f]).strip())


def _load_pd_keywords():
    """themes.json から PD関連の高重み・中重みキーワードを取得。"""
    themes_path = REPO / "scripts" / "themes.json"
    themes = json.loads(themes_path.read_text(encoding="utf-8"))
    pd = themes.get("pd", {})
    ck = pd.get("core_keywords", {})
    return ck.get("high_weight", []), ck.get("middle_weight", [])


def relevance_score(p: dict, high_kw: list[str], mid_kw: list[str]) -> int:
    """PD研究計画への接続度スコア。high=+3、middle=+1、tagsはhighと同等の重み。"""
    haystack = " ".join([
        p.get("title", ""), p.get("summary", ""), p.get("overview", ""),
        p.get("methodology", ""), p.get("implication", ""), p.get("idea", ""),
        p.get("novelty", ""), p.get("background", ""), p.get("result", ""),
        p.get("impact", ""), p.get("keywords", ""),
        " ".join(p.get("tags", []) or []),
    ]).lower()

    score = 0
    matched_high = []
    for kw in high_kw:
        if kw.lower() in haystack:
            score += 3
            matched_high.append(kw)
    for kw in mid_kw:
        if kw.lower() in haystack:
            score += 1
    return score, matched_high


def _normalize_title(t: str) -> str:
    """重複検出用：タイトルを大小文字・記号無視で正規化。"""
    import re
    return re.sub(r'[^a-z0-9]', '', (t or '').lower())


def select_top_pd_papers(papers: list[dict], n: int = 10) -> list[dict]:
    high_kw, mid_kw = _load_pd_keywords()
    pd_papers = [p for p in papers if p.get("is_pd_related")]

    # スコアリング
    scored = []
    for idx, p in enumerate(pd_papers):
        rel, matched = relevance_score(p, high_kw, mid_kw)
        rich = richness_score(p)
        composite = rel * 1000 + rich * 10 + min(_date_key(p), 99999999) // 10000
        scored.append((composite, idx, p, rel, matched))

    scored.sort(key=lambda x: (-x[0], x[1]))

    # 重複除去（タイトルベース）
    seen_titles = set()
    selected = []
    for _, _, p, rel, matched in scored:
        norm = _normalize_title(p.get("title", ""))
        if norm in seen_titles:
            continue
        seen_titles.add(norm)
        selected.append((p, rel, matched))
        if len(selected) >= n:
            break

    # 採点ログを表示
    print("\n=== Relevance scoring (top 10) ===")
    for i, (p, rel, matched) in enumerate(selected, 1):
        print(f"  {i:2d}. score={rel:3d}  match={matched[:3]}  {p['title'][:60]}")
    print()

    return [p for p, _, _ in selected]


def _date_key(p: dict) -> int:
    d = p.get("first_seen_date", "")
    try:
        return int(d.replace("-", ""))
    except (ValueError, AttributeError):
        return 0


# ============================================================
# HTML rendering
# ============================================================

NAV_HTML = """<!-- INJECTED-NAV-V1 -->
<div style="position:sticky;top:0;z-index:1000;background:#fff;border-bottom:1px solid #e2e8f0;padding:10px 18px;font-family:-apple-system,BlinkMacSystemFont,'Hiragino Kaku Gothic ProN','Hiragino Sans','Helvetica Neue',Arial,sans-serif;font-size:14px;display:flex;align-items:center;gap:14px;flex-wrap:wrap">
  <a href="../index.html" style="color:#475569;text-decoration:none;font-weight:600">← ダッシュボード</a>
  <a href="../papers.html" style="color:#475569;text-decoration:none">論文一覧</a>
  <a href="../themes.html" style="color:#475569;text-decoration:none">曜日テーマ</a>
  <a href="../pd.html" style="color:#be123c;text-decoration:none;font-weight:600">📍 PD研究</a>
  <a href="../favorites.html" style="color:#475569;text-decoration:none">★ お気に入り</a>
  <span style="margin-left:auto;color:#94a3b8;font-size:12px">PD研究キュレーション版</span>
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
  height: 4px; background: #be123c; }
.report-header h1 { margin: 0 0 6px; font-size: 26px; letter-spacing: -0.02em; }
.report-header .meta { color: #475569; font-size: 14px; }
.paper-card { background: #fff; border: 1px solid #e2e8f0; border-radius: 10px;
  padding: 22px 24px; margin-bottom: 16px; box-shadow: 0 1px 2px rgba(15,23,42,0.04); }
.paper-rank { display: inline-block; background: #be123c; color: white; font-weight: 700;
  font-size: 13px; padding: 3px 10px; border-radius: 999px; margin-right: 8px; }
.task-tag { display: inline-block; background: #be123c; color: white; font-size: 11px;
  padding: 2px 8px; border-radius: 999px; font-weight: 700; }
.task-tag.pd { background: #be123c; }
.paper-title { font-size: 17px; font-weight: 700; margin: 8px 0 6px; line-height: 1.4; }
.paper-title a { color: #0f172a; text-decoration: none; }
.paper-title a:hover { color: #2563eb; }
.paper-meta { color: #475569; font-size: 13px; margin-bottom: 16px; }
.section-block { border-left: 4px solid currentColor; padding: 10px 14px; margin: 12px 0;
  background: #f1f5f9; border-radius: 0 6px 6px 0; color: #0f172a; }
.section-block .section-label { display: inline-block; font-size: 12px; font-weight: 700;
  letter-spacing: 0.04em; margin-bottom: 6px; }
.section-block .section-content { font-size: 14px; }
.section-block.summary    { color: #3182ce; } .section-block.summary .section-label { color: #3182ce; }
.section-block.overview   { color: #718096; } .section-block.overview .section-label { color: #718096; }
.section-block.importance { color: #d69e2e; } .section-block.importance .section-label { color: #d69e2e; }
.section-block.method     { color: #38a169; } .section-block.method .section-label { color: #38a169; }
.section-block.limit      { color: #c53030; } .section-block.limit .section-label { color: #c53030; }
.section-block.implication{ color: #805ad5; } .section-block.implication .section-label { color: #805ad5; }
.section-block.idea       { color: #319795; } .section-block.idea .section-label { color: #319795; }
.section-block.novelty    { color: #805ad5; } .section-block.novelty .section-label { color: #805ad5; }
.section-block .section-content { color: #0f172a; }
.fav-checkbox { float: right; font-size: 13px; color: #475569; cursor: pointer; user-select: none; }
.fav-checkbox input { vertical-align: middle; margin-right: 4px; }
"""


SECTION_DEFS = [
    ("summary",     "▎一言要約",   "summary"),
    ("overview",    "▎研究概要",   "overview"),
    ("importance",  "▎重要な点",   "importance"),
    ("methodology", "▎方法論評価", "method"),
    ("limitation",  "▎限界",       "limit"),
    ("implication", "▎研究への示唆", "implication"),
    ("idea",        "▎研究アイデア", "idea"),
    ("novelty",     "▎新規性",     "novelty"),
]


def render_paper_card(rank: int, paper: dict) -> str:
    pid = paper.get("id", "")
    title = html.escape(paper.get("title", "(タイトル不明)"))
    authors = html.escape(paper.get("authors", ""))
    journal = html.escape(paper.get("journal", ""))
    design = html.escape(paper.get("design", ""))
    url = html.escape(paper.get("url", "#"))

    # data-* attributes for favorites compatibility
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
        sections_html += f"""
    <div class="section-block {css_class}">
      <div class="section-label">{label}</div>
      <div class="section-content">{html.escape(str(val))}</div>
    </div>"""

    meta_parts = []
    if authors: meta_parts.append(authors)
    if journal: meta_parts.append(f"<i>{journal}</i>")
    if design: meta_parts.append(design)
    meta_line = " · ".join(meta_parts)

    return f"""
  <div class="paper-card" {data_attrs}>
    <label class="fav-checkbox"><input type="checkbox" class="fav-toggle" data-pid="{html.escape(pid)}"> お気に入り</label>
    <span class="paper-rank">#{rank}</span>
    <span class="task-tag pd">📍 PD研究</span>
    <h2 class="paper-title"><a href="{url}" target="_blank" rel="noopener">{title}</a></h2>
    <p class="paper-meta">{meta_line}</p>
    {sections_html}
  </div>
"""


def render_report(date_str: str, papers: list[dict]) -> str:
    fmt_date = f"{date_str[:4]}年{int(date_str[4:6])}月{int(date_str[6:8])}日"

    paper_cards = "\n".join(render_paper_card(i + 1, p) for i, p in enumerate(papers))

    return f"""<!DOCTYPE html>
<html lang="ja">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>PD研究 キュレーション版 — {fmt_date}</title>
<style>{INLINE_CSS}</style>
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'%3E%3Crect width='100' height='100' rx='22' fill='%23be123c'/%3E%3Ctext x='50' y='66' text-anchor='middle' font-size='40' fill='white' font-family='Arial' font-weight='800'%3EPD%3C/text%3E%3C/svg%3E">
</head>
<body data-source-date="{date_str}" data-source-theme="pd-research">
{NAV_HTML}
<div class="report-wrapper">

  <div class="report-header">
    <h1>📍 PD研究 — キュレーション版</h1>
    <p class="meta">{fmt_date} ・ 既存データベースから選定した代表的なPD関連論文10本</p>
  </div>

{paper_cards}

</div>
<script src="../js/favorites.js"></script>
<script>
// お気に入りチェックボックスのhydration
document.querySelectorAll('.fav-toggle').forEach(cb => {{
  const pid = cb.dataset.pid;
  if (Favorites.has(pid)) cb.checked = true;
  cb.addEventListener('change', () => {{
    const card = cb.closest('.paper-card');
    const ds = card.dataset;
    const paper = {{
      id: ds.paperId, title: ds.title, authors: ds.authors, journal: ds.journal,
      design: ds.design, url: ds.url, summary: ds.summary, methodology: ds.methodology,
      limitation: ds.limitation, implication: ds.implication, idea: ds.idea,
      novelty: ds.novelty, background: ds.background, result: ds.result,
      impact: ds.impact, keywords: ds.keywords,
      tags: (ds.tags || "").split("|").filter(Boolean),
      source_reports: ["{date_str}_pd"],
      is_pd_related: true,
      first_seen_date: "{date_str[:4]}-{date_str[4:6]}-{date_str[6:8]}",
    }};
    if (cb.checked) Favorites.add(paper); else Favorites.remove(pid);
  }});
}});
</script>
</body>
</html>"""


# ============================================================
# Main
# ============================================================

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--date", default=datetime.now().strftime("%Y%m%d"),
                    help="Date in YYYYMMDD (default: today)")
    args = ap.parse_args()

    papers = json.loads(PAPERS_PATH.read_text(encoding="utf-8"))
    reports = json.loads(REPORTS_JSON_PATH.read_text(encoding="utf-8"))

    selected = select_top_pd_papers(papers, n=10)
    if len(selected) < 10:
        print(f"⚠️  PD関連論文が10本未満（{len(selected)}本のみ）。続行します。")

    # Generate HTML
    REPORTS_DIR.mkdir(parents=True, exist_ok=True)
    report_id = f"{args.date}_pd"
    out_path = REPORTS_DIR / f"{report_id}.html"
    html_content = render_report(args.date, selected)
    out_path.write_text(html_content, encoding="utf-8")
    print(f"✅ wrote {out_path}")

    # Update papers.json: add this report id to source_reports for selected papers
    selected_ids = {p["id"] for p in selected}
    paper_index = {p["id"]: p for p in papers}
    for pid in selected_ids:
        if pid in paper_index:
            srcs = paper_index[pid].setdefault("source_reports", [])
            if report_id not in srcs:
                srcs.append(report_id)
    PAPERS_PATH.write_text(json.dumps(papers, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"✅ updated papers.json (linked {len(selected_ids)} papers to {report_id})")

    # Update reports.json: add new report
    new_report = {
        "id": report_id,
        "date": f"{args.date[:4]}-{args.date[4:6]}-{args.date[6:8]}",
        "weekday": "pd",
        "theme_jp": "PD研究",
        "theme_en": "pd-research",
        "report_type": "regular",
        "source_html_path": f"docs/reports/{report_id}.html",
        "paper_ids": [p["id"] for p in selected],
        "paper_count": len(selected),
    }
    # Remove previous entry with same id if any (idempotent)
    reports = [r for r in reports if r["id"] != report_id]
    reports.append(new_report)
    REPORTS_JSON_PATH.write_text(json.dumps(reports, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"✅ updated reports.json (id: {report_id}, {len(selected)} papers)")

    print()
    print("=== Selected papers ===")
    for i, p in enumerate(selected, 1):
        print(f"  {i:2d}. [{p['id']}] {p['title'][:80]}")


if __name__ == "__main__":
    main()
