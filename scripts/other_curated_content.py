# -*- coding: utf-8 -*-
"""「その他」カテゴリ（依頼テーマ）。SKILL.md rev9-15 準拠。実在 verified 論文のみ。

曜日テーマ・PD研究と並ぶ独立カテゴリ。Yuji が都度依頼した任意テーマの論文を
キュレーションする運用。生成のたびに本ファイルの TOPIC と CONTENT を依頼テーマの
10本で置き換え、`python3 scripts/generate_other_curated_report.py --date YYYYMMDD
--topic "テーマ名"` で生成する。

paper ID 規約: {date}_other_NN（例 20260615_other_01）

ルール（曜日・PD と完全に同じ）：
- rev9 : 各セクション最低字数（summary 300/overview 700/importance 150/originality 100/
  discovery 300/methodology 150/limitation 100/citation 300/implication 200/idea 250）、
  1論文≥2,500字、10論文≥25,000字、日本語ポリシー
- rev10: summary/importance に PD/Yuji/TMM/JAGES/コホート規模/自前研究 接続を書かない
- rev11: 著者 verbatim、ジャーナル名＋IF併記、fulltext_status 必須
- rev12: 公刊年は直近3年以内、うち2-3本は直近2週間
- rev13: IF プレースホルダー禁止・ジャーナル名 verbatim・URL 一致
- rev15: 本文は日本語優先（英字比率 30%目安・40%超で WARNING）

TOPIC はヘッダー表示・reports.json 記録に使う依頼テーマ名。
"""

TOPIC = "（未設定：依頼テーマ名をここに記載）"

# 依頼テーマの論文10本をここに定義する（曜日 content と同じ構造）。
# 下記は構造サンプル（生成時に実在論文へ置き換えること）。
CONTENT = {
    # "20260615_other_01": {
    #     "title": "...",
    #     "authors": "First A, Second B, Third C, et al.",
    #     "journal": "Journal Name (IF=X.X), 2026年",
    #     "fulltext_status": "read_abstract_only",
    #     "design": "...",
    #     "url": "https://pubmed.ncbi.nlm.nih.gov/........./",
    #     "tags": ["その他", "依頼テーマ"],
    #     "summary": "...(300字以上、日本語優先)...",
    #     "overview": "**背景**：... **方法**：... **結果**：... **結論**：...(700字以上)",
    #     "importance": "...(150字以上)",
    #     "originality": "...(100字以上)",
    #     "discovery": "①... ②... ③...(300字以上)",
    #     "methodology": "...(150字以上)",
    #     "limitation": "...(100字以上)",
    #     "citation": "[introduction] ... [discussion] ...(300字以上)",
    #     "implication": "...(200字以上)",
    #     "idea": "...(250字以上)",
    # },
}
