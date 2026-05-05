# Research Dashboard

> 浅野優次郎（東北大学PD）の研究論文ダッシュボード。
> 毎朝8:00 JSTに曜日テーマ別の最新論文10本をHTMLレポート化し、ウェブサイトに自動公開。

## 🚀 ライブサイト

GitHubにpushしてGitHub Pagesを有効化すると：
**`https://<your-github-username>.github.io/research-dashboard/`**

## 構成

```
research-dashboard/
├── docs/                          ← GitHub Pagesのルート
│   ├── index.html                ← ダッシュボード（最新レポート＋カレンダー）
│   ├── papers.html               ← 全論文一覧（検索／フィルタ／ソート）
│   ├── themes.html               ← 曜日テーマ別ビュー
│   ├── favorites.html            ← お気に入り（★3段階＋JSONエクスポート）
│   ├── 404.html
│   ├── reports/                  ← 過去のHTMLレポート
│   ├── data/
│   │   ├── papers.json           ← 全論文データ（200本）
│   │   └── reports.json          ← レポートメタデータ（29件）
│   ├── css/{style.css, report.css}
│   └── js/{site.js, favorites.js}
├── skills/
│   └── daily-research-report/    ← Claude Codeスキル本体
├── scripts/
│   ├── run_daily_update.sh       ← 毎朝8:00に launchd から呼ばれるエントリ
│   ├── install_launchd.sh        ← launchd登録インストーラ
│   ├── com.yujiro.research-dashboard.plist
│   ├── migrate_existing_reports.py
│   ├── copy_existing_reports.py
│   └── inject_nav_into_reports.py
└── .github/workflows/validate.yml ← push時にJSON/HTML健全性チェック
```

## 機能

| ページ | できること |
|---|---|
| **ホーム** | 最新レポート、累計統計（レポート数／論文数／PD関連数／お気に入り数）、曜日テーマカード、過去30日カレンダー、最近の論文 |
| **論文一覧** | 全200論文を検索（タイトル・著者・要約・タグ）／曜日テーマで絞り込み／PD関連／お気に入りのみ／ソート（日付・お気に入り・ジャーナル等）／詳細展開 |
| **曜日テーマ** | 7テーマそれぞれ独立ページ。過去レポート一覧＋テーマ内の全論文 |
| **お気に入り** | ★1〜3段階評価／検索／フィルタ／JSON書き出し・取り込み／HTML書き出し（共有用）／全削除 |

### 曜日テーマ

| 曜日 | テーマ | カラー |
|---|---|---|
| 月 | 老年医学・健康寿命 | 紫 |
| 火 | 身体活動・運動疫学 | 緑 |
| 水 | 筋質・体組成 | オレンジ |
| 木 | 脳・認知（＋PD研究特化） | 青 |
| 金 | 疫学方法論 | ピンク |
| 土 | AI・データ科学 | シアン |
| 日 | 遺伝子・オミクス | アンバー |

## 初回セットアップ手順

### 1. GitHubリポジトリ作成（手動）

GitHub.com にログイン → New repository → Name: `research-dashboard` → Public（GitHub Pagesは公開だがプライバシーに配慮しつつ） → Create

### 2. ローカルからpush

```bash
cd ~/github/research-dashboard

# 初回のみリモート設定
git remote add origin https://github.com/<your-username>/research-dashboard.git
git branch -M main
git push -u origin main
```

`gh` CLIがあれば1コマンド：
```bash
gh repo create research-dashboard --public --source=. --remote=origin --push
```

### 3. GitHub Pages有効化

リポジトリ → **Settings → Pages** →
- **Source**: Deploy from a branch
- **Branch**: `main` / `/docs`
- Save

数分後 `https://<username>.github.io/research-dashboard/` でアクセス可能。

### 4. 毎朝8:00自動更新の設定（macOS launchd）

```bash
bash ~/github/research-dashboard/scripts/install_launchd.sh
```

これで毎日8:00 JSTに：
1. Claude Codeで `daily-research-report` スキルを起動
2. 今日の曜日テーマで最新論文10本を検索・レポート生成
3. `docs/reports/` にHTMLを保存、`papers.json`と`reports.json`を更新
4. 自動コミット → GitHub push → GitHub Pages自動デプロイ

確認：
```bash
launchctl list | grep com.yujiro.research-dashboard
tail -f ~/github/research-dashboard/scripts/logs/$(date +%Y%m%d).log
```

手動テスト実行：
```bash
launchctl start com.yujiro.research-dashboard
# または直接：
bash ~/github/research-dashboard/scripts/run_daily_update.sh
```

アンインストール：
```bash
launchctl unload ~/Library/LaunchAgents/com.yujiro.research-dashboard.plist
rm ~/Library/LaunchAgents/com.yujiro.research-dashboard.plist
```

### 注意事項

- **Macが8:00時点でスリープ中の場合**: launchdはMac起動後に最大1時間以内に遅延実行する設定にしています。完全に電源OFFだとスキップされるので、夜間スリープ運用が前提です。常時オン運用を望む場合はAnthropicの `scheduled-tasks` MCPを使う代替方法をお伝えします。
- **git pushの認証**: 初回pushでmacOSキーチェーンに認証情報が保存されれば、以降のlaunchd実行時もそれを使ってpushできます。SSH鍵を使う場合は `git remote set-url origin git@github.com:...` に変更してください。

## データ駆動型サイト

ウェブサイトは静的HTML＋JSのみ。すべての情報は `docs/data/papers.json` と `docs/data/reports.json` から動的に描画されます。

### papers.json スキーマ

```json
{
  "id": "<安定ID, sha1(title+journal)[:12]>",
  "title": "...",
  "authors": "...",
  "journal": "...",
  "design": "...",
  "url": "...",
  "summary": "...",
  "methodology": "...",
  "limitation": "...",
  "implication": "...",
  "idea": "...",
  "novelty": "...",
  "background": "...",
  "result": "...",
  "impact": "...",
  "keywords": "...",
  "tags": ["...", "..."],
  "source_reports": ["20260427_monday", ...],
  "is_pd_related": true,
  "first_seen_date": "2026-04-27"
}
```

### reports.json スキーマ

```json
{
  "id": "20260427_monday",
  "date": "2026-04-27",
  "weekday": "monday",
  "theme_jp": "老年医学・健康寿命",
  "theme_en": "geriatrics-healthspan",
  "report_type": "regular" | "detail" | "pd_focused",
  "source_html_path": "...",
  "paper_ids": ["...", "..."],
  "paper_count": 10
}
```

## お気に入りシステム

- ブラウザの `localStorage` キー: `researchFavorites_v3`
- v2/v1の旧データは自動マイグレーション
- 同一ドメイン内なら全ページで共有（GitHub Pagesに置けばどのページからでも同期）
- ★3段階評価、JSON/HTMLエクスポート、検索、絞り込み

## スキル運用ルール（絶対遵守）

`skills/daily-research-report/SKILL.md` 参照。要点：

1. DOCX生成しない（HTML のみ）
2. 詳細分析レポートは作らない（通常レポート1本のみ／木曜のみPD特化を追加で2本）
3. 10色分けセクションブロック厳守
4. 10本中2本以上はPD研究計画関連
5. PD研究関連には `<span class="task-tag pd">📍 PD研究</span>` バッジ
6. お気に入り機能は `<script src="../js/favorites.js"></script>` で外部読み込み
7. 出力先: `docs/reports/{YYYYMMDD}_{theme_en}.html`、papers.json/reports.jsonに追記
8. メール送信は廃止（ウェブサイトに移行）

## ライセンス

私的利用。
