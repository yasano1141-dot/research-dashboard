#!/usr/bin/env python3
"""
キュレーションコンテンツの質要件を自動検証する。

SKILL.md rev8 の質要件：
- 各セクションの最低字数
- 日本語ポリシー違反の検出
- 1論文の合計字数 ≥ 2,500字
- 全10論文合計 ≥ 25,000字

使い方：
    python3 scripts/validate_quality.py scripts/{theme}_curated_content.py

戻り値：
    0 = 全要件 pass
    1 = 1つ以上の要件違反
"""
from __future__ import annotations

import argparse
import importlib.util
import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent

# SKILL.md rev8 で定義されたセクション最低字数
MIN_CHARS = {
    "summary": 300,
    "overview": 700,
    "importance": 150,
    "originality": 100,
    "discovery": 300,
    "methodology": 150,
    "limitation": 100,
    "citation": 300,
    "implication": 200,
    "idea": 250,
}

# 1論文の合計最低字数
MIN_TOTAL_PER_PAPER = 2500

# 全10論文の合計最低字数
MIN_TOTAL_ALL = 25000

# 日本語化すべき英語語彙（SKILL.md rev6.1 + rev8）
# これらが本文に出てきたら警告
JAPANESE_REQUIRED = [
    # mortality
    (r"\ball[- ]cause mortality\b", "全原因死亡"),
    # diseases
    (r"\bcardiovascular disease\b", "心血管疾患"),
    (r"\bcancer\b(?! incidence)", "ガン"),  # cancer incidence はそのまま許可
    # study design
    (r"\bcohort\b(?! study\b)", "コホート"),
    (r"\bobservational study\b", "観察研究"),
    (r"\brandomized controlled trial\b", "ランダム化比較試験"),
    (r"\brandomized\b", "ランダム化"),
    # statistics
    (r"\beffect size\b", "効果サイズ"),
    (r"\bhazard ratio\b", "ハザード比（HR併記可）"),
    (r"\bodds ratio\b", "オッズ比（OR併記可）"),
    (r"\bconfidence interval\b", "信頼区間（95%CI併記可）"),
    (r"\bmeta[- ]analysis\b", "メタ解析"),
    (r"\bsensitivity analysis\b", "感度分析"),
    (r"\bcross[- ]sectional\b", "横断的"),
    (r"\blongitudinal\b(?! cohort\b| study\b)", "縦断的"),
    (r"\bregression\b(?! discontinuity\b| forest\b)", "回帰"),
    (r"\btreatment effect\b", "治療効果"),
    # bias
    (r"\bconfound(er|ing)\b", "交絡変数／交絡"),
    (r"\bbias\b(?! mitigation| auditing)", "バイアス"),
    (r"\bexposure\b(?! window)", "曝露"),
    (r"\boutcome\b(?! variable)", "アウトカム"),
    # disease conditions
    (r"\bdementia\b", "認知症"),
    (r"\bfrailty\b", "フレイル"),
    (r"\bsarcopenia\b", "サルコペニア"),
    (r"\bgait speed\b", "歩行速度"),
    (r"\bgrip strength\b", "握力"),
    (r"\bphysical activity\b(?! epidemiology)", "身体活動"),
    # other
    (r"\bmediation\b(?! analysis\b)", "媒介"),
    (r"\bvalidation\b(?! cohort\b)", "検証"),
    (r"\bbenchmark\b", "ベンチマーク"),
    (r"\bguideline\b(?!s? for)", "ガイドライン"),
    (r"\bprediction\b(?!s? model)", "予測"),
    # review terms
    (r"\bsystematic review\b", "システマティックレビュー／体系レビュー"),
    (r"\bcomprehensive review\b", "包括的レビュー"),
    (r"\bscoping review\b", "スコーピングレビュー"),
]

# rev10 (2026-05-10): summary/importance には PD課題・Yuji 接続を入れてはならない。
# 該当するフレーズの正規表現リスト。検出時は SKILL.md rev10 違反として警告。
# implication/idea で Yuji/PD 接続を書くのは OK（むしろ必須）。
PD_FORBIDDEN_IN_SUMMARY = [
    r"Yuji の[^。]{0,40}研究",
    r"Yuji 自身",
    r"Yuji の博士",
    r"Yuji の自前",
    r"Yuji の核心",
    r"Yuji の論文",
    r"Yuji の PD",
    r"Yuji コホート",
    r"PD 申請書",
    r"PD課題[123１２３]",
    r"PD 課題[123１２３]",
    r"PD 拡張軸",
    r"PD研究計画",
    r"学振 ?PD",
    r"博士論文での",
    r"博士論文・PD",
    r"500名コホート",
    r"900名コホート",
    r"国立長寿の?",
    r"TMM[・×]JAGES",
    r"TMM コホート",
    r"自前研究",
    r"自前データ",
    r"自前 cohort",
]


def load_content(path: Path) -> dict:
    spec = importlib.util.spec_from_file_location("content_module", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return getattr(module, "CONTENT", {})


def check_paper(pid: str, paper: dict) -> tuple[list[str], int]:
    """1論文の質チェック。返り値: (違反リスト, 合計字数)"""
    violations = []
    section_total = 0

    # セクション別字数チェック
    for field, min_chars in MIN_CHARS.items():
        text = (paper.get(field) or "").strip()
        chars = len(text)
        section_total += chars
        if chars < min_chars:
            violations.append(
                f"  ⚠️  {field}: {chars}字（最低 {min_chars}字、不足 {min_chars-chars}字）"
            )

    # 1論文合計チェック
    if section_total < MIN_TOTAL_PER_PAPER:
        violations.append(
            f"  ⚠️  TOTAL: {section_total}字（最低 {MIN_TOTAL_PER_PAPER}字、不足 {MIN_TOTAL_PER_PAPER-section_total}字）"
        )

    # 日本語ポリシー違反チェック
    body_text = " ".join([
        str(paper.get(f, "")) for f in MIN_CHARS.keys()
    ])
    jp_violations = []
    for pattern, ja_term in JAPANESE_REQUIRED:
        matches = re.findall(pattern, body_text, re.IGNORECASE)
        if matches:
            jp_violations.append(f"    - 「{matches[0]}」→「{ja_term}」（{len(matches)}回出現）")
    if jp_violations:
        violations.append(f"  📝 日本語化推奨：")
        violations.extend(jp_violations)

    # rev10: summary/importance には Yuji/PD 接続を入れない
    pd_violations = []
    for field in ("summary", "importance"):
        text = str(paper.get(field, ""))
        for pattern in PD_FORBIDDEN_IN_SUMMARY:
            matches = re.findall(pattern, text)
            if matches:
                pd_violations.append(
                    f"    - {field}: 「{matches[0]}」({len(matches)}回) — PD/Yuji 接続は implication/idea に分離"
                )
    if pd_violations:
        violations.append(f"  🚫 SKILL.md rev10: summary/importance への PD/Yuji 接続禁止：")
        violations.extend(pd_violations)

    return violations, section_total


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("content_file")
    ap.add_argument("--strict", action="store_true",
                    help="日本語ポリシー違反も failure として扱う")
    args = ap.parse_args()

    path = Path(args.content_file)
    if not path.is_absolute():
        path = REPO / path
    if not path.exists():
        print(f"❌ {path} not found", file=sys.stderr)
        sys.exit(2)

    content = load_content(path)
    print(f"📋 質要件チェック ({path.name}, {len(content)}論文)\n")

    has_violations = False
    grand_total = 0
    paper_summaries = []

    for pid, paper in content.items():
        violations, total = check_paper(pid, paper)
        grand_total += total
        title = (paper.get("title") or "")[:60]

        if violations:
            has_violations = True
            print(f"❌ [{pid}] {title}")
            print(f"   合計 {total}字")
            for v in violations:
                print(v)
            print()
        else:
            paper_summaries.append((pid, title, total))

    # 合格 papers
    for pid, title, total in paper_summaries:
        print(f"✅ [{pid}] {total}字  {title}")

    print()
    print(f"=== 全体集計 ===")
    print(f"  合計字数: {grand_total:,}字")
    print(f"  最低要件: {MIN_TOTAL_ALL:,}字")
    if grand_total < MIN_TOTAL_ALL:
        has_violations = True
        print(f"  ❌ 不足 {MIN_TOTAL_ALL-grand_total:,}字")
    else:
        print(f"  ✅ クリア（+{grand_total-MIN_TOTAL_ALL:,}字）")

    if has_violations:
        print()
        print("❌ 質要件未達。SKILL.md rev8 の「各論文の最低字数」と「日本語ポリシー」に従って修正してください。")
        sys.exit(1)
    else:
        print()
        print("✅ 全要件 pass")
        sys.exit(0)


if __name__ == "__main__":
    main()
