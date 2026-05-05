#!/usr/bin/env python3
"""
既存の研究レポートHTMLを reports.json の id (例: 20260427_monday) に対応する
ファイル名で docs/reports/ にコピーする。
"""
import json
import shutil
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
SRC_BASE = Path("/Users/asanoyuujiro/Library/Mobile Documents/com~apple~CloudDocs/Claude/daily_reports_research")
DST_DIR = REPO / "docs" / "reports"
DST_DIR.mkdir(parents=True, exist_ok=True)

with open(REPO / "docs" / "data" / "reports.json") as f:
    reports = json.load(f)

copied = 0
missing = 0
for r in reports:
    src = SRC_BASE / r["source_html_path"]
    dst = DST_DIR / f"{r['id']}.html"
    if not src.exists():
        print(f"  ❌ MISSING: {src}")
        missing += 1
        continue
    shutil.copy2(src, dst)
    copied += 1

print(f"✅ Copied {copied} reports to {DST_DIR}")
if missing:
    print(f"⚠️  {missing} source files missing")
