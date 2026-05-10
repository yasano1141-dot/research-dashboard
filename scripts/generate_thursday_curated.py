#!/usr/bin/env python3
"""
金曜日（疫学方法論）テーマのキュレーション版レポートを生成。
generate_pd_curated_report.py の構造を流用し、theme=friday で実装。
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

THEME_KEY = "thursday"
THEME_JP = "脳・認知"
THEME_EN = "brain-cognition"
THEME_COLOR = "#2563eb"


def _normalize_title(t: str) -> str:
    return re.sub(r'[^a-z0-9]', '', (t or '').lower())


def richness_score(p: dict) -> int:
    fields = ["summary", "methodology", "limitation", "implication", "idea",
              "novelty", "background", "result", "impact", "keywords"]
    return sum(1 for f in fields if p.get(f) and str(p[f]).strip())


def select_top_papers(papers: list[dict], reports_by_id: dict, n: int = 10,
                      report_id: str = ""):
    """rev2 (2026-05-08): thursday_curated_content.py に書かれた新規論文を最優先で採用。

    新規論文（CONTENT keys with ID like '20260508_fri_NN'）が papers.json にまだ
    存在しない場合は、本関数の戻り値に含めて呼び出し側で papers.json に追加する。
    既存papers との重複（タイトル正規化＋URLで判定）は除外。
    """
    try:
        from thursday_curated_content import CONTENT
    except ImportError:
        CONTENT = {}

    # 既存friday報告書に含まれる論文のタイトル・URL（重複検出用）
    # ただし今回再生成中の report_id は除外（idempotent処理）
    existing_titles = set()
    existing_urls = set()
    for p in papers:
        for rid in (p.get("source_reports") or []):
            if rid == report_id: continue
            r = reports_by_id.get(rid)
            if r and r.get("weekday") == "friday":
                nt = _normalize_title(p.get("title", ""))
                url = (p.get("url") or "").rstrip("/").lower()
                if nt: existing_titles.add(nt)
                if url: existing_urls.add(url)
                break

    # 新規論文（CONTENT keys）を最優先で組み立て
    selected = []
    seen_titles = set()
    seen_urls = set()
    paper_index = {p["id"]: p for p in papers}

    for cid, content in CONTENT.items():
        # CONTENT のタイトル/URL が既存friday報告書と重複していたらskip
        nt = _normalize_title(content.get("title", ""))
        url = (content.get("url") or "").rstrip("/").lower()
        if nt and nt in existing_titles:
            print(f"  ⚠️  skip (duplicates existing friday paper): {content['title'][:60]}")
            continue
        if url and url in existing_urls:
            print(f"  ⚠️  skip (duplicate URL): {content['title'][:60]}")
            continue
        if nt and nt in seen_titles: continue
        if url and url in seen_urls: continue

        # papers.jsonに既存ならそれを使う、なければ CONTENT から構築
        if cid in paper_index:
            p = paper_index[cid]
        else:
            # 新規論文を papers.json用に構築（後で呼び出し側で追加）
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
                "first_seen_date": "2026-05-08",
                "_is_new": True,  # マーカー（呼び出し側でpapers.json追加用）
            }
        selected.append(p)
        if nt: seen_titles.add(nt)
        if url: seen_urls.add(url)
        if len(selected) >= n: break

    if len(selected) < n:
        print(f"  ⚠️  CONTENTに{n}本未満のリッチ本文（{len(selected)}本のみ）")

    return selected


def merge_curated_content(paper: dict) -> dict:
    try:
        from thursday_curated_content import CONTENT
    except ImportError:
        return paper

    pid = paper.get("id")
    rich = CONTENT.get(pid)
    if not rich: return paper

    enriched = dict(paper)
    for k, v in rich.items():
        if v in (None, ""): continue
        if k == "tags" and isinstance(v, list):
            existing = enriched.get("tags") or []
            enriched[k] = list(dict.fromkeys(list(v) + list(existing)))
        else:
            enriched[k] = v
    return enriched


# ============================================================
# HTML (mirror generate_pd_curated_report.py のCSS/構造を流用)
# ============================================================

NAV_HTML = """<!-- INJECTED-NAV-V1 -->
<div style="position:sticky;top:0;z-index:1000;background:#fff;border-bottom:1px solid #e2e8f0;padding:10px 18px;font-family:-apple-system,BlinkMacSystemFont,'Hiragino Kaku Gothic ProN','Hiragino Sans','Helvetica Neue',Arial,sans-serif;font-size:14px;display:flex;align-items:center;gap:14px;flex-wrap:wrap">
  <a href="../index.html" style="color:#475569;text-decoration:none;font-weight:600">← ダッシュボード</a>
  <a href="../papers.html" style="color:#475569;text-decoration:none">論文一覧</a>
  <a href="../themes.html?day=friday" style="color:#db2777;text-decoration:none;font-weight:600">脳・認知</a>
  <a href="../pd.html" style="color:#475569;text-decoration:none">📍 PD</a>
  <a href="../favorites.html" style="color:#475569;text-decoration:none">★ お気に入り</a>
  <span style="margin-left:auto;color:#94a3b8;font-size:12px">脳・認知 キュレーション版</span>
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
  height: 4px; background: """ + THEME_COLOR + """; }
.report-header h1 { margin: 0 0 6px; font-size: 26px; letter-spacing: -0.02em; }
.report-header .meta { color: #475569; font-size: 14px; }
.paper-card { background: #fff; border: 1px solid #e2e8f0; border-radius: 10px;
  padding: 22px 24px; margin-bottom: 16px; box-shadow: 0 1px 2px rgba(15,23,42,0.04); }
.paper-rank { display: inline-block; background: """ + THEME_COLOR + """; color: white; font-weight: 700;
  font-size: 13px; padding: 3px 10px; border-radius: 999px; margin-right: 8px; }
.theme-tag { display: inline-block; background: """ + THEME_COLOR + """; color: white; font-size: 11px;
  padding: 2px 8px; border-radius: 999px; font-weight: 700; }
.task-tag.pd { background: #be123c; color: white; font-size: 11px;
  padding: 2px 8px; border-radius: 999px; font-weight: 700; display: inline-block; }
.paper-title { font-size: 17px; font-weight: 700; margin: 8px 0 6px; line-height: 1.4; }
.paper-title a { color: #0f172a; text-decoration: none; }
.paper-title a:hover { color: #2563eb; }
.paper-meta { color: #475569; font-size: 13px; margin-bottom: 16px; }
.section-block { border-left: 4px solid currentColor; padding: 10px 14px; margin: 12px 0;
  background: #f1f5f9; border-radius: 0 6px 6px 0; color: #0f172a; }
.section-block .section-label { display: inline-block; font-size: 12px; font-weight: 700;
  letter-spacing: 0.04em; margin-bottom: 6px; }
.section-block .section-content { font-size: 14px; line-height: 1.8; }
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
.section-block .section-content { color: #0f172a; }
.fav-checkbox { float: right; font-size: 13px; color: #475569; cursor: pointer; user-select: none; }
.fav-checkbox input { vertical-align: middle; margin-right: 4px; }
.tag-list { margin-top: 12px; font-size: 11px; color: #64748b; }
.tag-list .tag { display: inline-block; background: #f1f5f9; padding: 2px 8px; border-radius: 999px; margin-right: 4px; }
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
    if not text: return ""
    if re.search(r'[①-⑩]', text):
        parts = re.split(r'(?=[①-⑩])', text)
        return "<br>".join(html.escape(p.strip()) for p in parts if p.strip())
    return html.escape(text)


def render_paper_card(rank: int, paper: dict) -> str:
    pid = paper.get("id", "")
    title = html.escape(paper.get("title", ""))
    authors = html.escape(paper.get("authors", ""))
    journal = html.escape(paper.get("journal", ""))
    design = html.escape(paper.get("design", ""))
    url = html.escape(paper.get("url", "#"))
    is_pd = paper.get("is_pd_related", False)

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
        f'data-tags="{html.escape("|".join(paper.get("tags", []) or []))}"',
    ])

    sections_html = ""
    for field, label, css_class in SECTION_DEFS:
        val = paper.get(field, "")
        if not val or not str(val).strip(): continue
        content = _format_discovery(str(val)) if field == "discovery" else html.escape(str(val))
        sections_html += f'\n    <div class="section-block {css_class}"><div class="section-label">{label}</div><div class="section-content">{content}</div></div>'

    meta_parts = [x for x in [authors, f"<i>{journal}</i>" if journal else "", design] if x]
    meta_line = " · ".join(meta_parts)

    tags = paper.get("tags", []) or []
    tags_html = ""
    if tags:
        tags_html = '<div class="tag-list">' + "".join(f'<span class="tag">{html.escape(t)}</span>' for t in tags) + '</div>'

    pd_badge = '<span class="task-tag pd">📍 PD研究</span> ' if is_pd else ''

    return f"""
  <div class="paper-card" {data_attrs}>
    <label class="fav-checkbox"><input type="checkbox" class="fav-toggle" data-pid="{html.escape(pid)}"> お気に入り</label>
    <span class="paper-rank">#{rank}</span>
    {pd_badge}<span class="theme-tag">{THEME_JP}</span>
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
<title>{THEME_JP} — {fmt_date}</title>
<style>{INLINE_CSS}</style>
</head>
<body data-source-date="{date_str}" data-source-theme="{THEME_EN}">
{NAV_HTML}
<div class="report-wrapper">
  <div class="report-header">
    <h1>📚 {THEME_JP}</h1>
    <p class="meta">{fmt_date}（金曜日） ・ 脳・認知テーマ10本</p>
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


def _validate_urls_or_exit():
    """SKILL.md rev7: 生成前に必ず URL 検証。fabricated URL があれば exit。"""
    import subprocess
    content_file = REPO / "scripts" / f"{THEME_KEY}_curated_content.py"
    print(f"🔍 URL validation ({content_file.name})...")
    result = subprocess.run(
        ["python3", str(REPO / "scripts" / "validate_urls.py"), str(content_file)],
        capture_output=True, text=True
    )
    if result.returncode != 0:
        print(result.stdout)
        print(result.stderr, file=__import__('sys').stderr)
        print("\n❌ URL validation failed. Fix fabricated URLs before generating report.", file=__import__('sys').stderr)
        __import__('sys').exit(1)
    print("✅ All URLs verified\n")




def _validate_quality_or_exit():
    """SKILL.md rev9: 質要件の自動検証。最低字数・日本語ポリシー違反があれば exit。"""
    import subprocess as _sp, sys as _sys
    content_file = REPO / "scripts" / f"{THEME_KEY}_curated_content.py"
    print(f"📋 質要件検証 ({content_file.name})...")
    result = _sp.run(
        ["python3", str(REPO / "scripts" / "validate_quality.py"), str(content_file)],
        capture_output=True, text=True
    )
    if result.returncode != 0:
        print(result.stdout)
        print(result.stderr, file=_sys.stderr)
        print("
❌ 質要件未達。SKILL.md rev8 の最低字数・日本語ポリシーに従って修正してください。", file=_sys.stderr)
        _sys.exit(1)
    print("✅ 質要件 pass
")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--date", default=datetime.now().strftime("%Y%m%d"))
    ap.add_argument("--skip-url-check", action="store_true",
                    help="URL検証をスキップ（緊急時のみ。SKILL.md rev7では非推奨）")
    args = ap.parse_args()

    if not args.skip_url_check:
        _validate_urls_or_exit()
        _validate_quality_or_exit()

    papers = json.loads(PAPERS_PATH.read_text(encoding="utf-8"))
    reports = json.loads(REPORTS_JSON_PATH.read_text(encoding="utf-8"))
    rep_by_id = {r["id"]: r for r in reports}

    report_id = f"{args.date}_{THEME_KEY}"
    selected = select_top_papers(papers, rep_by_id, n=10, report_id=report_id)
    selected_enriched = [merge_curated_content(p) for p in selected]

    REPORTS_DIR.mkdir(parents=True, exist_ok=True)
    out_path = REPORTS_DIR / f"{report_id}.html"
    out_path.write_text(render_report(args.date, selected_enriched), encoding="utf-8")
    print(f"✅ wrote {out_path}")

    # idempotent cleanup: stale source_reports 参照を削除
    for p in papers:
        srcs = p.get("source_reports") or []
        if report_id in srcs:
            p["source_reports"] = [s for s in srcs if s != report_id]

    # 新規論文を papers.json に追加 + 既存論文を更新
    paper_index = {p["id"]: p for p in papers}
    enriched_index = {p["id"]: p for p in selected_enriched}
    new_papers_added = 0
    for pid in enriched_index.keys():
        rich = enriched_index[pid]
        is_new = rich.pop("_is_new", False)
        if is_new and pid not in paper_index:
            # 新規論文 → papers.json に追加
            new_paper = {k: v for k, v in rich.items() if k != "_is_new"}
            new_paper["source_reports"] = [report_id]
            papers.append(new_paper)
            paper_index[pid] = new_paper
            new_papers_added += 1
        else:
            # 既存論文 → rich content で update
            base = paper_index[pid]
            for k, v in rich.items():
                if k == "_is_new": continue
                if v in (None, ""): continue
                if k == "source_reports": continue
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
        "report_type": "regular",
        "source_html_path": f"docs/reports/{report_id}.html",
        "paper_ids": [p["id"] for p in selected_enriched],
        "paper_count": len(selected_enriched),
    }
    reports = [r for r in reports if r["id"] != report_id]
    reports.append(new_report)
    REPORTS_JSON_PATH.write_text(json.dumps(reports, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"✅ updated reports.json (id: {report_id}, {len(selected_enriched)} papers)")

    print("\n=== Selected papers ===")
    for i, p in enumerate(selected_enriched, 1):
        print(f"  {i:2d}. [{p['id']}] {p['title'][:70]}")


if __name__ == "__main__":
    main()
