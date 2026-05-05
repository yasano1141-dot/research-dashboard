---
name: daily-research-report
description: 毎朝7:00に曜日テーマ別の研究論文レポート（通常版・HTMLのみ）を作成し、research-dashboard ウェブサイト（GitHub Pages）にデプロイする。10色分けセクションブロック＋お気に入りJS外部読込＋data-* 属性が固定様式。10本中2本以上をYujiのPD研究計画関連にする。木曜日のみ「一般版」と「PD研究特化版」の2本を生成。生成後は papers.json と reports.json も更新する。"daily-research-report"、"研究レポート"、"研究論文レポート"、"daily report"などのキーワードで起動する。
last_updated: 2026-05-05 (rev5 — メール廃止、ウェブサイト運用に移行)
---

# Daily Research Report Skill

毎日の研究論文レポートを作成し、研究ダッシュボード（research-dashboard リポジトリ / GitHub Pages）にデプロイするスキル。曜日ごとに異なるテーマの最新論文10本を検索し、HTMLレポートを生成、`docs/reports/` 配下に保存し、`docs/data/papers.json` と `docs/data/reports.json` を更新する。

---

## 🔴 絶対遵守ルール（過去の指示を引き継ぎ、永続的に有効）

**以下のルールは Yuji が過去に明示的に指示したものであり、例外なくすべての daily-research-report 実行で適用すること。今後、別のセッションでも、別の Claude インスタンスでも、これらは絶対に守る。**

### 過去の指示の永続化（rev5 / 2026-05-05 時点）

1. **DOCX 生成は絶対に行わない**（HTMLのみで運用、2026-04-30 指示、rev3 にて確定）
2. **詳細分析レポート（バージョンB）は絶対に作らない**（通常レポートのみ、2026-04-30 指示、rev3 にて確定）
3. **10色分けセクションブロック様式（後述）を絶対に守る**（2026-04-30 指示、2026-05-03 再指示）
4. **お気に入りJSは外部ファイル（`../js/favorites.js`）として読み込む**（rev5 で導入。各レポートHTMLは共通JSをsrc参照する）
5. **毎日10本中2本以上を Yuji の PD 研究計画関連にする**（2026-05-03 指示。`references/pd-research-plan.md` 必読）
6. **木曜日は2つのHTMLレポート**を作成（`YYYYMMDD_brain-cognition.html` ＋ `YYYYMMDD_brain-cognition-pd.html`）
7. **メール送信は廃止された**（rev5 / 2026-05-05）。Gmail下書き作成・送信などのメール処理は一切行わない。代わりに `docs/data/papers.json` と `docs/data/reports.json` を更新し、ウェブサイト（GitHub Pages）に自動デプロイされる。

### 実行前チェック（必ず確認）
- [ ] DOCXを作っていないか？
- [ ] 「詳細分析」HTMLを作っていないか？
- [ ] 10セクション色分けで構成されているか？
- [ ] 「どんな引用に使えるか」セクション（introduction引用例＋discussion引用例）があるか？
- [ ] PD研究関連の論文が10本中2本以上含まれているか？
- [ ] PD関連論文に `<span class="task-tag pd">📍 PD研究</span>` バッジが付いているか？
- [ ] `<script src="../js/favorites.js"></script>` が `</body>` 直前に書かれているか？
- [ ] 各 `<div class="paper-card ...">` に `data-paper-id` ほかすべての data-* 属性があるか？
- [ ] `<body>` に `data-source-date` と `data-source-theme` があるか？
- [ ] `docs/data/papers.json` と `docs/data/reports.json` を更新したか？
- [ ] メール処理を一切実行していないか？

詳細は `references/critical-rules.md` を参照。

---

## 起動条件

- ユーザーが「研究レポート作って」「daily research report」「今日の研究論文」などと言った時
- スケジュールタスクとして毎朝7:00 JSTに自動実行（ユーザー側で設定する場合）

## 実行手順

### Step 1: 必須参照ファイルを最初に読む

スキル実行前に **必ず** 以下を読むこと：

1. `references/critical-rules.md` — 🔴 絶対遵守ルール（最優先）
2. `references/pd-research-plan.md` — Yuji の PD 研究計画（毎日2本以上の選定基準）
3. `references/themes-by-day.md` — 曜日別テーマ
4. `references/priority-journals.md` — 優先ジャーナルと検索戦略
5. `references/researcher-profile.md` — Yuji の研究プロフィール
6. `references/output-spec-regular.md` — 通常レポートの詳細仕様（10セクション）
7. `references/file-naming.md` — ファイル命名規則とフォルダ構造
8. `references/website-update-spec.md` — ウェブサイト連携仕様（papers.json / reports.json 追記）

### Step 2: 今日の曜日テーマを確認

`references/themes-by-day.md` を読み、本日の曜日に対応するテーマを特定する。

**木曜日の特例**: テーマは「認知機能・脳研究」だが、必ず2つのHTMLを生成する：
- `YYYYMMDD_brain-cognition.html` — 一般的な認知機能・脳研究（10本中6-7本を脳-身体機能関連）
- `YYYYMMDD_brain-cognition-pd.html` — PD申請書研究1（脳・筋・SHAP・身体機能）と研究2（運動中EEG）に特化した10本

### Step 3: 最新論文の検索

`references/priority-journals.md` の優先ジャーナルから、WebSearchで論文を検索する。

**必須要件：**
- 10本選定する
- うち1〜2本は直近1〜2週間以内に出版された最新論文（検索キーワードに「2026」「latest」「recent」を加える）
- **2本以上は PD 研究計画関連**（`references/pd-research-plan.md` のキーワードに該当）
- 研究デザイン優先順位: メタ解析 > 大規模コホート > 因果推論 > 方法論 > RCT
- 除外: 症例報告、基礎研究のみ、小規模研究

### Step 4: 10本を重要度順にランキング

PD関連論文を必ず Top 5 以内に1本以上入れる（重要性が高いため）。

### Step 5: 通常レポートHTMLを生成

詳細仕様: `references/output-spec-regular.md` を参照。

各論文に以下のセクションを **すべて独立した10並列ブロック** として記述する（10本均等の分量、rev3 で各セクション約1.2-1.4倍に増量済み）：

| # | セクション名 | クラス | 色 | 分量目安 |
|---|---|---|---|---|
| 1 | ▎一言要約 | `summary` | 青 #3182ce | 3〜4文 |
| 2 | ▎研究概要 | `overview` | 灰 #718096 | 5〜6文 |
| 3 | ▎重要な点 | `importance` | 黄 #d69e2e | 3〜4文 |
| 4 | ▎オリジナリティ | `originality` | 紫 #805ad5 | 3〜4文 |
| 5 | ▎新発見項目 | `discovery` | 緑 #16a34a | 5〜6項目（①②③形式） |
| 6 | ▎方法論評価 | `method` | 緑 #38a169 | 2〜3文 |
| 7 | ▎限界 | `limit` | 赤 #c53030 | 2〜3文 |
| 8 | ▎どんな引用に使えるか | `citation` | 紫 #805ad5 | introduction例＋discussion例（各2〜3文） |
| 9 | ▎研究への示唆 | `implication` | 紫 #805ad5 | 2〜3文 |
| 10 | ▎研究アイデア | `idea` | ティール #319795 | 2〜3文 |

各セクションのHTML形式：
```html
<div class="section-block summary">
  <span class="section-label">▎一言要約</span>
  <div class="section-content">...</div>
</div>
```

最後に「まとめ一覧表」（10本すべてを含む表）。

**HTMLヘッダの相対パス**（`docs/reports/` 配下に置く前提）：
- CSS: `<link rel="stylesheet" href="../css/report.css">`
- お気に入り共通JS: `<script src="../js/favorites.js"></script>`（`</body>` 直前）
- ホームへ戻るリンク: `<a href="../index.html">← ダッシュボードへ</a>`

### Step 6: PDタグの付与

PD研究関連の論文には、ランクバッジ近くに以下を表示：

```html
<span class="task-tag pd">📍 PD研究</span>
```

`data-tags` 属性にも「PD関連」を含める。

### Step 7: data-* 属性の埋め込み（必須）

各 `<div class="paper-card ...">` の opening tag に以下の属性を必ず追加する：

- `data-paper-id="YYYYMMDD_NN"`
- `data-title="..."`
- `data-authors="..."`
- `data-journal="..."`
- `data-design="..."`
- `data-url="..."`
- `data-summary="..."`
- `data-overview="..."`
- `data-importance="..."`
- `data-originality="..."`
- `data-discovery="..."`
- `data-methodology="..."`
- `data-limitation="..."`
- `data-citation="..."` （= どんな引用に使えるか）
- `data-implication="..."`
- `data-idea="..."`
- `data-tags="..."`（PD関連の場合は「PD関連」を含む）

`<body>` タグには：
- `data-source-date="YYYYMMDD"`
- `data-source-theme="テーマ名"`

### Step 8: お気に入り機能JSの読込（必須）

`</body>` 直前に **共通JSへの参照を1行**書く：

```html
<script src="../js/favorites.js"></script>
```

旧来の `_inject_to_reports.py` によるインライン注入は **rev5 で廃止**。各レポートHTMLは `docs/js/favorites.js`（リポジトリ共通）を相対パスで読み込む。

### Step 9: ファイル保存

詳細仕様: `references/file-naming.md` および `references/website-update-spec.md` を参照。

- 場所: `/Users/asanoyuujiro/github/research-dashboard/docs/reports/`
- 通常版: `{YYYYMMDD}_{theme_en}.html`（例: `20260505_physical-activity-epidemiology.html`）
- 木曜PD特化版: `{YYYYMMDD}_brain-cognition-pd.html`

`theme_en` の対応表は `references/website-update-spec.md` を参照。

**DOCX は生成しない。**

### Step 10: papers.json / reports.json を更新（メール送信の代替）

詳細仕様: `references/website-update-spec.md` を参照。

1. `/Users/asanoyuujiro/github/research-dashboard/docs/data/papers.json` を読み込み、当日選定した10本（木曜は20本）の論文エントリを追記し書き戻す
2. `/Users/asanoyuujiro/github/research-dashboard/docs/data/reports.json` を読み込み、当日のレポートエントリを追記し書き戻す

スキーマは `migrate_existing_reports.py`（リポジトリ既存スクリプト）が生成するものと一致させること。

**メール送信は一切行わない**（rev5 で廃止）。GitHub Pages による自動デプロイで全データが配信される。

### Step 11: 完了報告

ユーザーに以下を報告：
- 生成したHTMLファイル（通常日: 1個、木曜: 2個）の絶対パス
- 更新したJSON（papers.json: +N件、reports.json: +1〜2件）
- 選定論文10本のうち最新（2026）論文の本数
- PD関連論文の本数（必ず2本以上）
- Top 3 のタイトルと一行サマリー

---

## 必須参照ファイル

- `references/critical-rules.md` — 🔴 絶対遵守ルール
- `references/pd-research-plan.md` — Yuji の PD 研究計画
- `references/themes-by-day.md` — 曜日別テーマ
- `references/priority-journals.md` — 優先ジャーナル
- `references/researcher-profile.md` — 研究プロフィール
- `references/output-spec-regular.md` — 通常レポート仕様
- `references/file-naming.md` — ファイル命名規則
- `references/website-update-spec.md` — ウェブサイト連携仕様（papers.json / reports.json）
- `references/troubleshooting.md` — トラブルシューティング

## テンプレート

`templates/` 配下：
- `templates/regular-report.html` — 通常レポートのHTML骨格（10セクション色分け）

**`templates/detail-report.html` は使用しない**（rev3 で詳細分析を廃止）。**メール用テンプレートは rev5 で削除済み**。

## スクリプト

`scripts/` 配下：
- `scripts/get-today-context.py` — 今日の曜日・テーマ・フォルダを返す

**`scripts/inject-favorites.py` は rev5 で実質的に不要**（共通JSを `<script src>` で読み込むため）。残存している場合は廃止予定。

**`scripts/generate-docx.js` および `scripts/generate-detail-docx.js` は使用しない**（rev3 で DOCX 生成を廃止）。

## アセット

- なし（旧 `assets/favorites-viewer.html` は rev5 で削除。代替は research-dashboard リポジトリの `docs/favorites.html`）

## 過去例

`examples/` 配下に参考になる過去のレポート例（テンプレート参照用）。最新仕様の参考は：
- 2026-04-30 木曜日_脳・認知の例（10セクション色分けの参考）
- 2026-04-29 水曜日_筋質・体組成の例（同上）

---

## 重要な注意事項

### お気に入り機能の動作要件
- HTMLは GitHub Pages 上の `https://<user>.github.io/research-dashboard/reports/...` で開く
- localStorage キー: `researchFavorites_v2`（互換性のため不変）
- ビューアパス: `../favorites.html`（相対パス、ダッシュボード側のページ）

### 日本語環境
- 日本語フォント: Noto Sans JP / Noto Serif JP（HTML）
- ファイル名は theme_en（英数字ハイフン）に統一（GitHub Pages URL の安全のため）
- 日付は `YYYYMMDD` 形式（例：`20260505`）

### スケジュールタスクとして使う場合
ユーザー不在時はreasonable defaultsを選んで進む。完了後にレポート。ただし上記の絶対遵守ルールは「合理的判断」の対象外。例外なく適用する。

## トラブルシューティング

`references/troubleshooting.md` 参照。よくある問題：
- お気に入りチェックボックスが表示されない → `<script src="../js/favorites.js">` の読み込みと `data-paper-id` 属性を確認
- papers.json/reports.json の追記でJSONが壊れた → バックアップから復元、Pythonの `json.dump(..., ensure_ascii=False, indent=2)` を使用
- ブラウザで `file://` が開かない → GitHub Pages URLで開く（ローカル動作確認は `python3 -m http.server` を `docs/` 配下で起動）
