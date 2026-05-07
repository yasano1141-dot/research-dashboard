# Research Dashboard

> 浅野優次郎（東北大学PD）の研究論文ダッシュボード。
> 毎日デスクトップの **📊 Daily Report** をダブルクリックすると、
> 曜日テーマ別の最新論文10本がHTMLレポート化され、Vercel上のサイトに自動公開されます。

## 🚀 ライブサイト

**`https://research-dashboard.vercel.app/`**
（正確なURLはVercelダッシュボードで確認）

GitHub: [yasano1141-dot/research-dashboard](https://github.com/yasano1141-dot/research-dashboard)

---

## 運用フロー（毎日30秒）

```
┌─ 1. Macを開く ─────────────────────┐
│                                     │
│  Desktopの「📊 Daily Report」を     │
│  ダブルクリック                      │
│                                     │
└──────────────┬──────────────────────┘
               ↓
┌─ 2. 自動で全部走る（5〜10分） ──────┐
│  - GitHubから最新を pull            │
│  - Claude Code が論文検索＋執筆      │
│    （サブスクリプション枠で動作）     │
│  - HTML生成 / JSON更新 / RSS再生成   │
│  - 自動 commit & push               │
│  - Vercelが自動デプロイ              │
│  - macOS通知＋ブラウザ自動オープン   │
└──────────────┬──────────────────────┘
               ↓
       サイトに反映 ✅
```

**API課金なし** — Claude Codeのサブスクリプション枠で動作するので、Pro/Maxプラン契約料以外の追加課金は発生しません。

---

## ディレクトリ構成

```
research-dashboard/
├── daily.command                  ← ダブルクリックで起動（Desktopにエイリアス）
├── docs/                          ← Vercel outputDirectory
│   ├── index.html                ← ダッシュボード
│   ├── papers.html               ← 全論文一覧（検索／フィルタ／ソート）
│   ├── themes.html               ← 曜日テーマ別ビュー
│   ├── pd.html                   ← 📍 PD研究専用ビュー
│   ├── favorites.html            ← お気に入り（★3段階＋JSON/BibTeX/HTML書出）
│   ├── 404.html
│   ├── rss.xml                   ← RSSフィード
│   ├── reports/                  ← 過去のHTMLレポート
│   ├── data/{papers,reports}.json
│   ├── css/{style,report}.css
│   └── js/{site,favorites,bibtex}.js
├── .claude/skills/
│   └── daily-research-report/    ← Claude Codeスキル本体（プロジェクトスコープ）
│       ├── SKILL.md              ← 絶対遵守ルール
│       ├── references/           ← テーマ・優先ジャーナル・PD計画など
│       └── templates/regular-report.html
├── scripts/
│   ├── daily_generator.py        ← API版（GitHub Actions用フォールバック）
│   ├── themes.json               ← 曜日テーマ・検索式（編集容易）
│   ├── generate_rss.py           ← RSSフィード生成
│   ├── requirements.txt
│   ├── migrate_existing_reports.py / copy_existing_reports.py / inject_nav_into_reports.py
└── .github/workflows/
    ├── daily-update.yml          ← API版フォールバック（cron無効、手動のみ）
    └── validate.yml              ← push時のJSON/HTML/Python健全性チェック
```

---

## 機能

| ページ | できること |
|---|---|
| **ホーム** | 最新レポート、累計統計、曜日テーマカード、過去30日カレンダー、最近の論文 |
| **論文一覧** | 全論文の検索／曜日テーマ・PD・お気に入りで絞り込み／詳細展開／ソート |
| **曜日テーマ** | 7テーマそれぞれ独立ページ。過去レポート＋テーマ内の全論文 |
| **📍 PD研究** | 脳-身体機能・EEG・SHAP・筋質と認知の論文を全曜日から自動集約 |
| **お気に入り** | ★1〜3段階／JSON書出・取り込み／**BibTeX書出**／HTML書出 |
| **RSSフィード** | `rss.xml` を購読すれば最新論文を任意のリーダーで購読可能 |

### 曜日テーマ

| 曜日 | テーマ | 木曜のみ追加 |
|---|---|---|
| 月 | 老年医学・健康寿命 | |
| 火 | 身体活動・運動疫学 | |
| 水 | 筋質・体組成 | |
| 木 | 脳・認知 | **PD研究特化版** |
| 金 | 疫学方法論 | |
| 土 | AI・データ科学 | |
| 日 | 遺伝子・オミクス | |

検索式・優先ジャーナルは `scripts/themes.json` 1ファイルで完結。後から自由に追加・編集できます。

---

## セットアップ

詳細は [SETUP.md](SETUP.md) 参照。

1. ✅ GitHub `yasano1141-dot/research-dashboard` リポジトリ作成・push（完了済み）
2. Vercelでimport → 自動デプロイ
3. Desktopの **📊 Daily Report** をダブルクリックして動作確認
4. 完了。以降は毎日Macを開いた時にダブルクリックするだけ

---

## なぜ「毎日1クリック」運用なのか（設計判断）

| 案 | コスト | 電源OFF対応 | 既存スキルの活用 |
|---|---|---|---|
| GitHub Actions cron + API | 月$15〜30+ | ✅ | ❌ 再実装 |
| ローカル launchd cron | $0 | ❌（OFF時スキップ） | ✅ |
| **デスクトップ1クリック（採用）** | **$0**（サブスク枠内） | ✅（Macが起動した時に実行） | ✅ |

「毎日Macを開く」という既存習慣に1クリック乗せるだけで、コスト最小・既存スキル流用・電源依存なしを両立できます。

API版（`scripts/daily_generator.py` + GitHub Actions）はフォールバックとして残置。長期出張等で `ANTHROPIC_API_KEY` を一時的に登録すれば自動運用に切替可能です。

---

## データスキーマ

### papers.json（配列）
```json
{
  "id": "<sha1(title+journal)[:12]>",
  "title": "...", "authors": "...", "journal": "...", "design": "...",
  "url": "...", "summary": "...", "overview": "...", "importance": "...",
  "methodology": "...", "limitation": "...", "implication": "...",
  "idea": "...", "novelty": "...", "background": "...", "result": "...",
  "impact": "...", "keywords": "...", "tags": ["..."],
  "source_reports": ["20260427_monday"],
  "is_pd_related": true,
  "first_seen_date": "2026-04-27"
}
```

### reports.json（配列）
```json
{
  "id": "20260427_monday",
  "date": "2026-04-27", "weekday": "monday",
  "theme_jp": "老年医学・健康寿命", "theme_en": "geriatrics-healthspan",
  "report_type": "regular | detail | pd_focused",
  "source_html_path": "docs/reports/20260427_monday.html",
  "paper_ids": ["..."], "paper_count": 10
}
```

---

## お気に入りシステム

- ブラウザ `localStorage` キー: `researchFavorites_v3`
- v2/v1の旧データは自動マイグレーション
- 同一ドメイン（Vercel配下）のため**全ページで共有**
- ★3段階評価／JSON・BibTeX・HTML書出／検索／フィルタ

---

## スキル運用ルール（絶対遵守）

`.claude/skills/daily-research-report/SKILL.md` 参照。要点：

1. DOCX生成しない（HTML のみ）
2. 詳細分析レポートは作らない（通常レポート1本／木曜のみPD特化追加で2本）
3. 10色分けセクションブロック厳守
4. 10本中2本以上はPD研究計画関連
5. PD関連には `<span class="task-tag pd">📍 PD研究</span>` バッジ
6. お気に入り機能は `<script src="../js/favorites.js"></script>` で外部読込
7. 出力先: `docs/reports/{YYYYMMDD}_{theme_en}.html`、papers.json/reports.jsonに追記
8. メール送信は廃止

---

## ライセンス

私的利用。
