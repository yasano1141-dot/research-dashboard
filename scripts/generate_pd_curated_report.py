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

    # rich content がある論文には大幅ブースト（執筆済みなので優先選定）
    try:
        from pd_curated_content import CONTENT
        prepared_ids = set(CONTENT.keys())
    except ImportError:
        prepared_ids = set()

    # スコアリング
    scored = []
    for idx, p in enumerate(pd_papers):
        rel, matched = relevance_score(p, high_kw, mid_kw)
        rich = richness_score(p)
        prepared_bonus = 50 if p["id"] in prepared_ids else 0
        composite = rel * 1000 + prepared_bonus * 100 + rich * 10 + min(_date_key(p), 99999999) // 10000
        scored.append((composite, idx, p, rel, matched))

    scored.sort(key=lambda x: (-x[0], x[1]))

    # 重複除去：完全一致タイトル or URL の重複のみ排除
    seen_titles = set()
    seen_urls = set()
    selected = []
    for _, _, p, rel, matched in scored:
        norm_title = _normalize_title(p.get("title", ""))
        url = (p.get("url") or "").rstrip("/").lower()
        if norm_title and norm_title in seen_titles:
            continue
        if url and url in seen_urls:
            continue
        if norm_title:
            seen_titles.add(norm_title)
        if url:
            seen_urls.add(url)
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


def select_pinned_pd_papers(papers: list[dict], pinned_ids: list[str]) -> list[dict]:
    """pinned_ids（pd_curated_content.CONTENT のキー順）に厳密一致する論文を選定。

    特定日付のレポートを「キュレーション済みの10本そのまま」で再生成する用途。
    relevance スコアでの全体選定はせず、CONTENT に列挙された論文を順序どおり返す。

    rev17 (2026-08-16): papers.json に未登録の id は CONTENT から新規論文として
    構築する（曜日版 generate_{theme}_curated.py と同じ挙動）。従来は既存論文への
    リンクのみで、新規 PD レポートを作ると 0 本になっていた。
    """
    try:
        from pd_curated_content import CONTENT
    except ImportError:
        CONTENT = {}

    index = {p["id"]: p for p in papers}
    selected = []
    created = []
    for pid in pinned_ids:
        if pid in index:
            selected.append(index[pid])
            continue
        content = CONTENT.get(pid)
        if not content:
            print(f"⚠️  pinned だが papers.json にも CONTENT にも無い id: {pid}")
            continue
        selected.append({
            "id": pid,
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
            "is_pd_related": True,
            "first_seen_date": f"{pid[:4]}-{pid[4:6]}-{pid[6:8]}",
            "_is_new": True,
        })
        created.append(pid)
    if created:
        print(f"🆕 CONTENT から新規論文を構築: {len(created)}本")
    print(f"\n=== Pinned selection ({len(selected)}本、CONTENT キー順) ===")
    for i, p in enumerate(selected, 1):
        print(f"  {i:2d}. [{p['id']}] {p['title'][:60]}")
    print()
    return selected


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
    """新発見項目を①②③形式に整形（既に①などがあれば改行で分割表示）。"""
    if not text:
        return ""
    # ①②③④⑤⑥⑦⑧⑨⑩ を各行頭に
    import re
    # 既に①等が含まれているかチェック
    if re.search(r'[①-⑩]', text):
        # 分割：①の前で改行
        parts = re.split(r'(?=[①-⑩])', text)
        return "<br>".join(html.escape(p.strip()) for p in parts if p.strip())
    # 番号なしテキストはそのまま
    return html.escape(text)


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
        # discovery は①②③形式に整形
        if field == "discovery":
            content_html = _format_discovery(str(val))
        else:
            content_html = html.escape(str(val))
        sections_html += f"""
    <div class="section-block {css_class}">
      <div class="section-label">{label}</div>
      <div class="section-content">{content_html}</div>
    </div>"""

    meta_parts = []
    if authors: meta_parts.append(authors)
    if journal: meta_parts.append(f"<i>{journal}</i>")
    if design: meta_parts.append(design)
    meta_line = " · ".join(meta_parts)

    tags = paper.get("tags", []) or []
    tags_html = ""
    if tags:
        tags_html = '<div class="tag-list">' + "".join(
            f'<span class="tag">{html.escape(t)}</span>' for t in tags
        ) + '</div>'

    return f"""
  <div class="paper-card" {data_attrs}>
    <label class="fav-checkbox"><input type="checkbox" class="fav-toggle" data-pid="{html.escape(pid)}"> お気に入り</label>
    <span class="paper-rank">#{rank}</span>
    <span class="task-tag pd">📍 PD研究</span>
    <h2 class="paper-title"><a href="{url}" target="_blank" rel="noopener">{title}</a></h2>
    <p class="paper-meta">{meta_line}</p>
    {sections_html}
    {tags_html}
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

def _merge_curated_content(paper: dict) -> dict:
    """pd_curated_content.CONTENT があればその論文をリッチコンテンツでoverlayする。"""
    try:
        from pd_curated_content import CONTENT
    except ImportError:
        return paper

    pid = paper.get("id")
    rich = CONTENT.get(pid)
    if not rich:
        return paper

    enriched = dict(paper)
    # rich側で値があれば既存をoverwrite。空の値はスキップ
    for k, v in rich.items():
        if v in (None, ""):
            continue
        if k == "tags" and isinstance(v, list):
            # マージ：rich側のタグをユニーク化して優先
            existing_tags = enriched.get("tags") or []
            merged = list(dict.fromkeys(list(v) + list(existing_tags)))
            enriched["tags"] = merged
        else:
            enriched[k] = v
    return enriched


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--date", default=datetime.now().strftime("%Y%m%d"),
                    help="Date in YYYYMMDD (default: today)")
    ap.add_argument("--pinned", action="store_true",
                    help="pd_curated_content.CONTENT のキーをそのまま採用し、relevance 選定を行わない")
    args = ap.parse_args()

    papers = json.loads(PAPERS_PATH.read_text(encoding="utf-8"))
    reports = json.loads(REPORTS_JSON_PATH.read_text(encoding="utf-8"))

    # CONTENT のキーがすべて当日 (--date) の id（{date}_pd_NN）なら、
    # キュレーション済みの10本そのままで再生成する（特定日付レポートの本文更新用途）。
    # それ以外（新規 PD 枠など）は従来どおり relevance で全体選定する。
    pinned_ids = []
    try:
        from pd_curated_content import CONTENT
        content_ids = list(CONTENT.keys())
        date_prefix = f"{args.date}_pd_"
        if content_ids and all(cid.startswith(date_prefix) for cid in content_ids):
            pinned_ids = content_ids
    except ImportError:
        pass

    if args.pinned or pinned_ids:
        if not pinned_ids:
            # --pinned 明示時は CONTENT のキーをそのまま使う
            from pd_curated_content import CONTENT
            pinned_ids = list(CONTENT.keys())
        print(f"📌 pinned モード：CONTENT の {len(pinned_ids)}本を date={args.date} のレポートとして再生成")
        selected = select_pinned_pd_papers(papers, pinned_ids)
    else:
        selected = select_top_pd_papers(papers, n=10)
    if len(selected) < 10:
        print(f"⚠️  PD関連論文が10本未満（{len(selected)}本のみ）。続行します。")

    # Merge rich curated content (pd_curated_content.py) を各論文に適用
    selected_enriched = [_merge_curated_content(p) for p in selected]

    # Generate HTML
    REPORTS_DIR.mkdir(parents=True, exist_ok=True)
    report_id = f"{args.date}_pd"
    out_path = REPORTS_DIR / f"{report_id}.html"
    html_content = render_report(args.date, selected_enriched)
    out_path.write_text(html_content, encoding="utf-8")
    print(f"✅ wrote {out_path}")

    # Update papers.json: rich content も書き戻す（次回サイト全体で参照可能に）
    selected_ids = {p["id"] for p in selected_enriched}
    paper_index = {p["id"]: p for p in papers}
    enriched_index = {p["id"]: p for p in selected_enriched}

    # Idempotent cleanup: 既存の papers.json から report_id への参照をすべて削除
    # → 今回選定された10本にだけ追加し直す（過去runのstale参照を残さない）
    for p in papers:
        srcs = p.get("source_reports") or []
        if report_id in srcs:
            p["source_reports"] = [s for s in srcs if s != report_id]

    new_papers_added = 0
    for pid in selected_ids:
        rich = enriched_index[pid]
        is_new = rich.pop("_is_new", False)
        if is_new and pid not in paper_index:
            # 新規論文 → papers.json に追加（rev17）
            new_paper = {k: v for k, v in rich.items() if k != "_is_new"}
            new_paper["source_reports"] = [report_id]
            papers.append(new_paper)
            paper_index[pid] = new_paper
            new_papers_added += 1
        elif pid in paper_index:
            base = paper_index[pid]
            for k, v in rich.items():
                if v in (None, ""):
                    continue
                if k in ("source_reports", "_is_new"):
                    continue
                if k == "tags" and isinstance(v, list):
                    base[k] = list(dict.fromkeys(v + (base.get(k) or [])))
                else:
                    base[k] = v
            srcs = base.setdefault("source_reports", [])
            if report_id not in srcs:
                srcs.append(report_id)
    PAPERS_PATH.write_text(json.dumps(papers, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"✅ updated papers.json (added {new_papers_added} new papers, "
          f"linked {len(selected_ids)} to {report_id}, total now {len(papers)})")

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
