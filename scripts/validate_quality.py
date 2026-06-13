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

    # rev11: 著者名・ジャーナル IF・fulltext_status のチェック
    rev11_violations = []

    # ジャーナル IF 併記チェック
    journal = str(paper.get("journal", ""))
    if "IF=" not in journal and "IF =" not in journal:
        rev11_violations.append(
            f"    - journal: IF併記なし「{journal[:60]}」— rev11 で IF（または IF=N/A）の併記必須"
        )

    # 著者名の曖昧表記チェック（pre-rev11 grandfathered な論文は許容）
    authors = str(paper.get("authors", ""))
    is_grandfathered = paper.get("fulltext_status") == "pre-rev11_needs_verification"
    AMBIGUOUS_AUTHOR_PATTERNS = [
        r"Various authors",
        r"関連雑誌",
        r"同分野",
        r"^著者[不未]明",
    ]
    for pat in AMBIGUOUS_AUTHOR_PATTERNS:
        if re.search(pat, authors):
            if not is_grandfathered:
                rev11_violations.append(
                    f"    - authors: 曖昧表記「{authors[:60]}」— rev11 で verbatim 必須"
                )
            break

    # fulltext_status フィールド必須チェック
    ALLOWED_FULLTEXT_STATUS = {
        "read_full", "read_pmc", "read_abstract_only",
        "could_not_read", "pre-rev11_needs_verification",
    }
    fts = paper.get("fulltext_status")
    if fts is None:
        rev11_violations.append(
            "    - fulltext_status: フィールド欠落 — rev11 で必須（read_full/read_pmc/read_abstract_only/could_not_read のいずれか）"
        )
    elif fts not in ALLOWED_FULLTEXT_STATUS:
        rev11_violations.append(
            f"    - fulltext_status: 不正値「{fts}」— allowed: {sorted(ALLOWED_FULLTEXT_STATUS)}"
        )
    elif fts == "could_not_read":
        rev11_violations.append(
            f"    - fulltext_status: 「could_not_read」の論文は採用不可（rev11）。代替論文に差し替えること"
        )

    if rev11_violations:
        violations.append("  🚫 SKILL.md rev11: 著者名／ジャーナルIF／本文読解の義務違反：")
        violations.extend(rev11_violations)

    # rev12: 公刊年が直近3年以内であることをチェック
    # journal フィールドから年を抽出（例 "Nature Aging (IF=17.0), 2025年" → 2025）
    rev12_violations = []
    journal_str = str(paper.get("journal", ""))
    year_match = re.search(r"(20\d{2})\s*年", journal_str)
    if year_match:
        pub_year = int(year_match.group(1))
        from datetime import date
        current_year = date.today().year
        cutoff_year = current_year - 3
        tags = paper.get("tags", []) or []
        is_foundational = "foundational" in [str(t).lower() for t in tags]
        is_grandfathered = paper.get("fulltext_status") == "pre-rev11_needs_verification"

        if pub_year < cutoff_year:
            if is_foundational:
                # 例外（最大1本）として情報のみ出力、violations には追加しない
                print(f"  ℹ️  rev12: {paper.get('title','')[:50]}（{pub_year}年、foundational 例外として許容）")
            elif is_grandfathered:
                # 移行措置として情報のみ出力、violations には追加しない
                print(f"  ℹ️  rev12: {paper.get('title','')[:50]}（{pub_year}年、pre-rev11 移行措置）")
            else:
                rev12_violations.append(
                    f"    - journal: {pub_year}年は cutoff {cutoff_year}年未満（直近3年要件違反、最新論文に差替必須）"
                )

    if rev12_violations:
        violations.append("  🚫 SKILL.md rev12: 公刊年が直近3年以内であること：")
        violations.extend(rev12_violations)

    # rev13: ジャーナル IF・ジャーナル名・URL の strict 検証
    rev13_violations = []
    journal_field = str(paper.get("journal", ""))

    # 1. IF placeholder 検出
    PLACEHOLDER_IF_PATTERNS = [
        r"IF\s*=\s*確認待ち",
        r"IF\s*=\s*未確認",
        r"IF\s*=\s*TBD",
        r"IF\s*=\s*\?",
        r"IF\s*=\s*tbd",
    ]
    for pat in PLACEHOLDER_IF_PATTERNS:
        if re.search(pat, journal_field):
            rev13_violations.append(
                f"    - journal: IF プレースホルダー検出「{journal_field[:80]}」— 実値に修正必須"
            )
            break

    # 2. 「関連雑誌」「関連メタ解析」「関連論文」「同分野」検出
    VAGUE_JOURNAL_PATTERNS = [
        r"関連雑誌",
        r"関連メタ解析",
        r"関連論文",
        r"同分野",
    ]
    for pat in VAGUE_JOURNAL_PATTERNS:
        if re.search(pat, journal_field):
            rev13_violations.append(
                f"    - journal: 曖昧表記「{journal_field[:80]}」— publisher 公式表記に修正必須"
            )
            break

    # 3. ジャーナル名への日本語混入検出（IF=N/A や年表記の文脈外で）
    # journal の先頭部分（IF= や , 年 の前）に日本語があるかチェック
    journal_main = re.split(r"\s*\(IF=", journal_field, maxsplit=1)[0]
    # 「Alzheimer's & 認知症」「ガン Research」など
    JAPANESE_IN_JOURNAL = [
        (r"認知症", "Dementia"),
        (r"ガン(?!（)", "Cancer"),  # ガン（OR併記可）等の説明用は除外
        (r"フレイル", "Frailty"),
        (r"サルコペニア", "Sarcopenia"),
    ]
    for pat, en in JAPANESE_IN_JOURNAL:
        if re.search(pat, journal_main):
            rev13_violations.append(
                f"    - journal: ジャーナル名に日本語混入「{journal_main[:60]}」→「{en}」に戻す必須"
            )
            break

    # 4. IF=N/A は preprint/conference のみ許容
    if re.search(r"IF\s*=\s*N/A", journal_field):
        is_preprint_or_conf = any(
            kw in journal_field.lower()
            for kw in ["arxiv", "biorxiv", "medrxiv", "neurips", "icml", "cvpr",
                       "iclr", "aaai", "kdd", "preprint", "proceedings"]
        )
        if not is_preprint_or_conf:
            rev13_violations.append(
                f"    - journal: IF=N/A は preprint/conference のみ許容「{journal_field[:80]}」— 実IFに修正必須"
            )

    if rev13_violations:
        violations.append("  🚫 SKILL.md rev13: IF・ジャーナル名 strict 検証違反：")
        violations.extend(rev13_violations)

    # rev15: 本文の英字比率チェック（WARNING のみ、hard fail にはしない）
    body_fields = ("summary", "overview", "importance", "originality",
                   "discovery", "methodology", "limitation", "citation",
                   "implication", "idea", "design")
    body_concat = "".join(str(paper.get(f, "")) for f in body_fields)
    ascii_letters = len(re.findall(r"[A-Za-z]", body_concat))
    non_space = len(re.sub(r"[\s\d]", "", body_concat))
    eng_ratio = (ascii_letters / non_space * 100) if non_space else 0
    if eng_ratio > 40:
        # WARNING のみ（violations に入れず、has_violations を立てない）
        print(f"  ⚠️  rev15 英字比率 WARNING: {paper.get('title','')[:45]}（本文英字 {eng_ratio:.0f}%、目安30%以下・40%超は説明的英語の japanize 漏れを疑う）")

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
