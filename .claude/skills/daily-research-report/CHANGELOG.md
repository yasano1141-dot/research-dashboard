# CHANGELOG

## rev4 — 2026-05-05
**重要なリファクタリング: claude-code 化の前提整備**

### 追加
- `references/critical-rules.md` — 🔴 絶対遵守ルールを独立ファイル化
- `references/pd-research-plan.md` — Yuji の学振PD研究計画を独立ファイル化（毎日2本以上の選定基準）
- `CHANGELOG.md` — 本ファイル

### 変更
- `SKILL.md` を全面書き直し
  - 冒頭に絶対遵守ルール（rev3 までの指示を統合）
  - 必須参照ファイルを critical-rules.md・pd-research-plan.md に拡張
  - 木曜日2HTML生成ルールを明記
  - 違反防止チェックリストを内部化
- `references/output-spec-regular.md` — 10セクション色分け様式（旧9セクション）に更新、「どんな引用に使えるか」セクション（introduction引用例＋discussion引用例）を追加
- `references/email-spec.md` — メール構成を「通常日2通／木曜3通」に更新、DOCX 添付・詳細分析メールの記述を削除
- `references/themes-by-day.md` — 木曜日の特例（2HTML生成）を追記

### 廃止（`.deprecated` サフィックス追加）
- `references/output-spec-detail.md.deprecated` — 詳細分析仕様（rev3 で廃止）
- `templates/detail-report.html.deprecated` — 詳細分析HTMLテンプレート
- `templates/email-detail.html.deprecated` — 詳細分析メールテンプレート
- `scripts/generate-docx.js.deprecated` — DOCX生成スクリプト（rev3 で廃止）
- `scripts/generate-detail-docx.js.deprecated` — 詳細分析DOCX生成

### 違反履歴（学習用）
- 2026-05-05 のスケジュールタスクで重大な違反:
  - 通常レポート + 詳細分析レポート両方をDOCXとHTMLで作成
  - 9セクション形式（古い形式）を使用
  - 「どんな引用に使えるか」セクションなし
  - PD研究関連論文ゼロ
  - お気に入りJS注入なし
  - 根本原因: スケジュールタスクで使ったSKILL.md（uploadsの古いバージョン）が rev3 を反映していなかった
  - 対策: rev4 で claude-code-skills/daily-research-report/ を完全更新

## rev3 — 2026-05-03
- DOCX 生成廃止（HTMLのみ）
- 詳細分析レポート（バージョンB）廃止
- 通常レポートを9セクション色分け化（後に rev4 で10セクション化）
- 各セクション分量を1.2-1.4倍に増量
- PD研究関連を10本中2本以上必須化
- 木曜日2HTML生成（一般版＋PD研究特化版）

## rev2 — 2026-04-30
- お気に入り機能JS注入を必須化
- data-* 属性の必須リスト確定
- 9セクション色分け様式の確立

## rev1 — 2026-04-28
- 初版（バージョンA・B、HTML・DOCX、3通メール）
- claude-code-skills フォルダ構造化
