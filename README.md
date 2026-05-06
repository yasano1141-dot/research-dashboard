# Research Dashboard

> 浅野優次郎（東北大学PD）の研究論文ダッシュボード。
> 毎朝8:00 JSTに曜日テーマ別の最新論文10本をHTMLレポート化し、
> Vercel上のサイトに自動公開。**Macが電源OFFでも動きます**。

## 🚀 ライブサイト

**`https://research-dashboard-yasano1141-dot.vercel.app/`**
（正確なURLはVercelダッシュボードで確認）

---

## アーキテクチャ

```
┌─ GitHub Actions (cron 23:00 UTC) ─┐
│  毎朝8:00 JSTに自動実行            │
│  scripts/daily_generator.py        │
│   ├─ PubMed E-utilities 検索       │
│   ├─ bioRxiv API 検索              │
│   ├─ Anthropic API でランク＋執筆   │
│   ├─ docs/reports/*.html 生成      │
│   ├─ docs/data/*.json 更新         │
│   └─ scripts/generate_rss.py       │
│                                    │
│  → git commit & push to main       │
└────────────────┬───────────────────┘
                 ↓
   ┌── Vercel auto-deploy ──┐
   │  /docs を静的サイトとして│
   │  公開（CDN込み）         │
   └────────────────────────┘
```

**電源OFFでもクラウド完結**：GitHub ActionsとVercelはAnthropicの環境とは独立した
クラウドインフラで動作するため、ユーザーのMacの状態に関係なく毎日動きます。

---

## ディレクトリ構成

```
research-dashboard/
├── docs/                          ← Vercel outputDirectory
│   ├── index.html                ← ダッシュボード
│   ├── papers.html               ← 全論文一覧（検索／フィルタ／ソート）
│   ├── themes.html               ← 曜日テーマ別ビュー
│   ├── pd.html                   ← 📍 PD研究専用ビュー
│   ├── favorites.html            ← お気に入り（★3段階＋JSON/BibTeX/HTML書出）
│   ├── 404.html
│   ├── rss.xml                   ← RSSフィード（毎日自動更新）
│   ├── reports/                  ← 過去のHTMLレポート
│   ├── data/{papers,reports}.json  ← 全データ
│   ├── css/{style,report}.css
│   └── js/{site,favorites,bibtex}.js
├── skills/daily-research-report/  ← Claude Codeスキル本体（ローカル運用時に使用）
├── scripts/
│   ├── daily_generator.py        ← クラウド版日次生成器（GitHub Actionsで実行）
│   ├── themes.json               ← 曜日テーマ・検索式（編集しやすい）
│   ├── generate_rss.py           ← RSSフィード生成
│   ├── requirements.txt          ← Python依存
│   ├── migrate_existing_reports.py  ← 既存HTMLからJSON抽出（履歴再構築用）
│   ├── copy_existing_reports.py
│   ├── inject_nav_into_reports.py
│   └── (旧 launchd 関連 — フォールバック用に保持)
├── .github/workflows/
│   ├── daily-update.yml          ← 毎朝8:00 JSTのcron
│   └── validate.yml              ← push時のJSON/HTML/Python健全性チェック
└── vercel.json                   ← Vercelデプロイ設定
```

---

## 機能

| ページ | できること |
|---|---|
| **ホーム** | 最新レポート、累計統計、曜日テーマカード、過去30日カレンダー、最近の論文 |
| **論文一覧** | 全論文の検索／曜日テーマ・PD・お気に入りで絞り込み／詳細展開／ソート（日付・お気に入り・ジャーナル等） |
| **曜日テーマ** | 7テーマそれぞれ独立ページ。過去レポート＋テーマ内の全論文 |
| **📍 PD研究** | 脳-身体機能・EEG・SHAP・筋質と認知の論文を全曜日から自動集約 |
| **お気に入り** | ★1〜3段階／JSON書出・取り込み／**BibTeX書出**／HTML書出／検索／フィルタ |
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

詳細は [SETUP.md](SETUP.md) 参照。要約：

1. GitHub `yasano1141-dot/research-dashboard` リポジトリを作成
2. `git push -u origin main`
3. Vercelでimport → 自動デプロイ
4. GitHub Secretsに `ANTHROPIC_API_KEY` を登録
5. 完了。毎朝8:00 JSTに自動更新

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
- ★3段階評価／JSON・BibTeX・HTML書出／検索／フィルタ／全削除

### BibTeX書出
申請書執筆時に便利。お気に入りページの「📚 BibTeX書き出し」ボタンで `papers_YYYY-MM-DD.bib` がダウンロード。

---

## 絶対遵守ルール（スキル運用）

`skills/daily-research-report/SKILL.md` および `scripts/daily_generator.py` のSYSTEM_PROMPT に内蔵：

1. DOCX生成しない（HTML のみ）
2. 詳細分析レポートは作らない（通常レポート1本／木曜のみPD特化追加で2本）
3. 10色分けセクションブロック厳守（一言要約／概要／重要な点／オリジナリティ／新発見／方法論／限界／引用例／示唆／アイデア）
4. 10本中2本以上はPD研究計画関連
5. PD関連には `<span class="task-tag pd">📍 PD研究</span>` バッジ
6. お気に入り機能は `<script src="../js/favorites.js"></script>` で外部読込
7. 出力先: `docs/reports/{YYYYMMDD}_{theme_en}.html`、papers.json/reports.jsonに追記
8. メール送信は廃止（ウェブサイトに移行）

---

## ライセンス

私的利用。
