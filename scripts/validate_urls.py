#!/usr/bin/env python3
"""
論文URLの存在確認（HEAD/GETでHTTP 200を確認）。

使い方：
    python3 scripts/validate_urls.py [content_file]

例：
    python3 scripts/validate_urls.py scripts/saturday_curated_content.py
    python3 scripts/validate_urls.py scripts/friday_curated_content.py

戻り値：
    0 = 全URLがHTTP 200/3xx
    1 = 1つ以上のURLが404または接続エラー
"""
from __future__ import annotations

import argparse
import importlib.util
import sys
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

REPO = Path(__file__).resolve().parent.parent

# 一部の出版社は HEAD requestをブロックするため GET を使う
USER_AGENT = "Mozilla/5.0 (Research Dashboard URL Validator)"


def check_url(url: str, timeout: int = 10) -> tuple[bool, str]:
    """URLの存在を確認。返り値: (ok, status_message)"""
    if not url or url == "#":
        return False, "empty/placeholder URL"
    try:
        req = Request(url, method="GET", headers={"User-Agent": USER_AGENT})
        with urlopen(req, timeout=timeout) as resp:
            status = resp.status
            if 200 <= status < 400:
                return True, f"HTTP {status}"
            return False, f"HTTP {status}"
    except HTTPError as e:
        if e.code in (403,):
            # 403 は認証なしのscholarly siteで多発するが、URL自体は存在する
            return True, f"HTTP 403 (likely paywalled, URL exists)"
        return False, f"HTTP {e.code}"
    except URLError as e:
        return False, f"URL error: {e.reason}"
    except Exception as e:
        return False, f"error: {type(e).__name__}: {e}"


def load_content_from_file(path: Path) -> dict:
    """{theme}_curated_content.py を動的にロード"""
    spec = importlib.util.spec_from_file_location("content_module", path)
    if spec is None or spec.loader is None:
        raise ImportError(f"Cannot load {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return getattr(module, "CONTENT", {})


def main():
    ap = argparse.ArgumentParser(description="Validate paper URLs in curated content files")
    ap.add_argument("content_file", help="Path to {theme}_curated_content.py")
    ap.add_argument("--timeout", type=int, default=10)
    args = ap.parse_args()

    path = Path(args.content_file)
    if not path.is_absolute():
        path = REPO / path
    if not path.exists():
        print(f"❌ {path} not found", file=sys.stderr)
        sys.exit(2)

    content = load_content_from_file(path)
    print(f"📋 Validating {len(content)} URLs from {path.name}...\n")

    failed = []
    for pid, paper in content.items():
        url = paper.get("url", "")
        title = (paper.get("title") or "")[:60]
        ok, msg = check_url(url, timeout=args.timeout)
        marker = "✅" if ok else "❌"
        print(f"  {marker} [{pid}] {msg}")
        print(f"      {title}")
        print(f"      {url}")
        if not ok:
            failed.append((pid, title, url, msg))

    print()
    if failed:
        print(f"❌ {len(failed)} URL(s) failed:")
        for pid, title, url, msg in failed:
            print(f"  - [{pid}] {msg}: {url}")
        sys.exit(1)
    else:
        print(f"✅ All {len(content)} URLs verified")
        sys.exit(0)


if __name__ == "__main__":
    main()
