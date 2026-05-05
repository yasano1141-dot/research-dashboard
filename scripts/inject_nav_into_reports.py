#!/usr/bin/env python3
"""
docs/reports/*.html にサイトナビゲーションバーを注入する。

- <body> 直後に「← ダッシュボードへ戻る」のヘッダを差し込む
- 既存のお気に入りインラインJSは残す（v2キーを使うがfavorites.jsがv3でv2を吸収する）
- すでにナビが入っているファイルは skip
"""
import re
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
DST_DIR = REPO / "docs" / "reports"

NAV_MARK = "<!-- INJECTED-NAV-V1 -->"

NAV_HTML = """<!-- INJECTED-NAV-V1 -->
<div style="position:sticky;top:0;z-index:1000;background:#fff;border-bottom:1px solid #e2e8f0;padding:10px 18px;font-family:-apple-system,BlinkMacSystemFont,'Hiragino Kaku Gothic ProN','Hiragino Sans','Helvetica Neue',Arial,sans-serif;font-size:14px;display:flex;align-items:center;gap:14px;flex-wrap:wrap">
  <a href="../index.html" style="color:#475569;text-decoration:none;font-weight:600">← ダッシュボード</a>
  <a href="../papers.html" style="color:#475569;text-decoration:none">論文一覧</a>
  <a href="../themes.html" style="color:#475569;text-decoration:none">曜日テーマ</a>
  <a href="../favorites.html" style="color:#475569;text-decoration:none">★ お気に入り</a>
  <span style="margin-left:auto;color:#94a3b8;font-size:12px">📅 過去アーカイブ</span>
</div>
"""

count = 0
for html_path in sorted(DST_DIR.glob("*.html")):
    content = html_path.read_text(encoding="utf-8")
    if NAV_MARK in content:
        continue
    new_content = re.sub(r"(<body[^>]*>)", lambda m: m.group(1) + "\n" + NAV_HTML, content, count=1)
    if new_content != content:
        html_path.write_text(new_content, encoding="utf-8")
        count += 1

print(f"✅ Injected nav into {count} report files")
