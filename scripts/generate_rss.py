#!/usr/bin/env python3
"""
RSS feed generator. Reads docs/data/papers.json + reports.json and writes
docs/rss.xml (latest 30 papers).

Run as a CI step after the daily generator (or standalone).
"""
import json
import html
from datetime import datetime, timezone
from pathlib import Path
from xml.sax.saxutils import escape

REPO = Path(__file__).resolve().parent.parent
DATA_DIR = REPO / "docs" / "data"
OUT = REPO / "docs" / "rss.xml"

SITE_URL = "https://research-dashboard-nine.vercel.app"   # Vercel自動URL — カスタムドメイン使うなら変更


def main():
    papers = json.loads((DATA_DIR / "papers.json").read_text(encoding="utf-8"))
    reports = json.loads((DATA_DIR / "reports.json").read_text(encoding="utf-8"))
    rep_by_id = {r["id"]: r for r in reports}

    def report_for(p):
        for rid in (p.get("source_reports") or []):
            r = rep_by_id.get(rid)
            if r: return r
        return None

    def date_key(p):
        r = report_for(p)
        return r["date"] if r else (p.get("first_seen_date") or "")

    items = sorted(papers, key=date_key, reverse=True)[:30]

    now = datetime.now(timezone.utc).strftime("%a, %d %b %Y %H:%M:%S +0000")
    item_xml = []
    for p in items:
        r = report_for(p)
        link = f"{SITE_URL}/reports/{r['id']}" if r else (p.get("url") or SITE_URL)
        title = escape(p.get("title", "(no title)"))
        desc_parts = []
        if p.get("summary"): desc_parts.append(p["summary"])
        if p.get("authors"): desc_parts.append(f"著者: {p['authors']}")
        if p.get("journal"): desc_parts.append(f"掲載: {p['journal']}")
        if p.get("is_pd_related"): desc_parts.append("📍 PD研究関連")
        desc = escape(" / ".join(desc_parts))
        date_str = date_key(p) or datetime.now().strftime("%Y-%m-%d")
        try:
            pub = datetime.strptime(date_str, "%Y-%m-%d").replace(tzinfo=timezone.utc).strftime("%a, %d %b %Y %H:%M:%S +0000")
        except ValueError:
            pub = now
        guid = f"{SITE_URL}/papers/{p['id']}"
        cats = "".join(f"<category>{escape(t)}</category>" for t in (p.get("tags") or [])[:5])
        item_xml.append(f"""    <item>
      <title>{title}</title>
      <link>{link}</link>
      <guid isPermaLink="false">{guid}</guid>
      <pubDate>{pub}</pubDate>
      <description>{desc}</description>
      {cats}
    </item>""")

    feed = f"""<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0" xmlns:atom="http://www.w3.org/2005/Atom">
  <channel>
    <title>Research Dashboard — Yujiro Asano</title>
    <link>{SITE_URL}</link>
    <atom:link href="{SITE_URL}/rss.xml" rel="self" type="application/rss+xml"/>
    <description>毎朝8:00 JST更新の研究論文レポート（老年医学・運動疫学・筋質・脳認知・疫学方法論・AI・オミクス）</description>
    <language>ja</language>
    <lastBuildDate>{now}</lastBuildDate>
{chr(10).join(item_xml)}
  </channel>
</rss>"""

    OUT.write_text(feed, encoding="utf-8")
    print(f"✅ wrote {OUT} ({len(items)} items)")


if __name__ == "__main__":
    main()
