# ウェブサイト連携仕様

研究ダッシュボード（research-dashboard リポジトリ / GitHub Pages）と日次レポート生成の連携仕様。
**メール送信は rev5 で廃止された。代わりに以下のファイルを更新することで、GitHub Pages で全データが配信される。**

---

## 出力ファイル

毎日の生成で以下を更新する：

1. **HTML レポート**: `/Users/asanoyuujiro/github/research-dashboard/docs/reports/{YYYYMMDD}_{theme_en}.html` を新規作成
2. **papers.json 追記**: `/Users/asanoyuujiro/github/research-dashboard/docs/data/papers.json` を読み込み、当日選定した論文エントリを追記し書き戻す
3. **reports.json 追記**: 同様に `/Users/asanoyuujiro/github/research-dashboard/docs/data/reports.json` にレポートエントリを追記し書き戻す

木曜日は HTML が2つ・reports.json エントリも2件・papers.json は重複しない論文のみ追記。

---

## theme_en 対応

ファイル名・URL の英数字ハイフン化に使う。

| 曜日 | テーマ（日本語） | theme_en |
|------|------------------|----------|
| 月 | 健康寿命・老年学 | `geriatrics-healthspan` |
| 火 | 身体活動・運動疫学 | `physical-activity-epidemiology` |
| 水 | 筋質・体組成 | `muscle-body-composition` |
| 木（一般） | 認知機能・脳研究 | `brain-cognition` |
| 木（PD特化） | 認知機能・脳研究 PD特化 | `brain-cognition-pd` |
| 金 | 疫学・方法論 | `epidemiology-methods` |
| 土 | AI・データサイエンス | `ai-data-science` |
| 日 | 遺伝学・オミクス | `genetics-omics` |

例：
- 火曜日 2026-05-05: `20260505_physical-activity-epidemiology.html`
- 木曜日 2026-05-07: `20260507_brain-cognition.html` ＋ `20260507_brain-cognition-pd.html`

---

## HTMLの相対パス

各レポートHTMLは `docs/reports/` 配下に置かれるため、以下の相対パスを使う：

```html
<!DOCTYPE html>
<html lang="ja">
<head>
  <meta charset="UTF-8">
  <title>...</title>
  <link rel="stylesheet" href="../css/report.css">
</head>
<body data-source-date="20260505" data-source-theme="身体活動・運動疫学">
  <nav><a href="../index.html">← ダッシュボードへ</a></nav>
  <!-- 10本のpaper-card -->
  <script src="../js/favorites.js"></script>
</body>
</html>
```

具体的なテンプレートは `scripts/generate_report_template.py` 等のリポジトリ既存スクリプトを参照（存在しない場合は `templates/regular-report.html` をベースにし、CSS/JS の参照パスを上記に書き換える）。

---

## papers.json のスキーマ

`docs/data/papers.json` は **配列**。各エントリは以下のキーを持つ：

| キー | 型 | 説明 |
|------|----|------|
| `id` | string | `YYYYMMDD_NN`（例: `20260505_01`）。レポート内ランクと一致 |
| `title` | string | 論文タイトル（英語原文） |
| `authors` | string | 著者リスト（カンマ区切り、et al. 可） |
| `journal` | string | ジャーナル名・年（例: `Lancet 2026`） |
| `design` | string | 研究デザイン（例: `IPDメタ解析`） |
| `url` | string | DOI または論文URL |
| `summary` | string | ▎一言要約（3〜4文） |
| `methodology` | string | ▎方法論評価 |
| `limitation` | string | ▎限界 |
| `implication` | string | ▎研究への示唆 |
| `idea` | string | ▎研究アイデア |
| `novelty` | string | ▎オリジナリティ |
| `background` | string | ▎研究概要のうち背景部分（または overview 全文） |
| `result` | string | 主要結果（▎新発見項目の要約でも可） |
| `impact` | string | ▎重要な点 |
| `keywords` | string | カンマ区切りキーワード |
| `tags` | array<string> | タグ配列（例: `["PD関連", "最新2026", "中年期"]`） |
| `source_reports` | array<string> | このペーパーが登場するレポートID（例: `["20260505_physical-activity-epidemiology"]`） |
| `is_pd_related` | boolean | PD研究関連なら `true` |
| `first_seen_date` | string | このペーパーが初めて登場した日付（`YYYY-MM-DD`） |

### 追記処理の擬似コード

```python
import json
from pathlib import Path

papers_path = Path("/Users/asanoyuujiro/github/research-dashboard/docs/data/papers.json")
papers = json.loads(papers_path.read_text(encoding="utf-8"))

existing_ids = {p["id"] for p in papers}
for new_paper in today_papers:
    if new_paper["id"] in existing_ids:
        # 既存エントリに source_reports を追記
        for p in papers:
            if p["id"] == new_paper["id"]:
                if today_report_id not in p["source_reports"]:
                    p["source_reports"].append(today_report_id)
        continue
    papers.append(new_paper)

papers_path.write_text(
    json.dumps(papers, ensure_ascii=False, indent=2),
    encoding="utf-8"
)
```

---

## reports.json のスキーマ

`docs/data/reports.json` は **配列**。各エントリは以下のキーを持つ：

| キー | 型 | 説明 |
|------|----|------|
| `id` | string | `{YYYYMMDD}_{theme_en}`（例: `20260505_physical-activity-epidemiology`） |
| `date` | string | `YYYY-MM-DD` |
| `weekday` | string | 曜日（日本語1文字、例: `火`） |
| `theme_jp` | string | 日本語テーマ名（例: `身体活動・運動疫学`） |
| `theme_en` | string | 英数字ハイフン名（上記対応表） |
| `report_type` | string | `regular` または `pd-special`（木曜PD特化のみ） |
| `source_html_path` | string | `reports/{YYYYMMDD}_{theme_en}.html`（docsからの相対パス） |
| `paper_ids` | array<string> | このレポートに含まれる10本の `paper.id` 配列 |
| `paper_count` | number | 通常 10 |

### 追記処理の擬似コード

```python
reports_path = Path("/Users/asanoyuujiro/github/research-dashboard/docs/data/reports.json")
reports = json.loads(reports_path.read_text(encoding="utf-8"))

reports.append({
    "id": f"{yyyymmdd}_{theme_en}",
    "date": f"{yyyy}-{mm}-{dd}",
    "weekday": weekday_jp,
    "theme_jp": theme_jp,
    "theme_en": theme_en,
    "report_type": "regular",  # または "pd-special"
    "source_html_path": f"reports/{yyyymmdd}_{theme_en}.html",
    "paper_ids": [p["id"] for p in today_papers],
    "paper_count": len(today_papers),
})

reports_path.write_text(
    json.dumps(reports, ensure_ascii=False, indent=2),
    encoding="utf-8"
)
```

---

## スキーマ整合性

`migrate_existing_reports.py`（research-dashboard リポジトリの既存スクリプト）が過去レポートから生成したスキーマと一致させること。乖離が見つかった場合は `migrate_existing_reports.py` の出力を正典とし、本ファイルを更新する。

---

## メール送信について

**メール送信は rev5（2026-05-05）で完全に廃止された**。

- Gmail 下書き作成、メール送信、SMTP 連携などの処理は **一切行わない**
- 旧来の「【研究レポート】」「【パス情報】」「【PD研究特化】」メールは送らない
- 代わりに上記の papers.json / reports.json 更新で配信する。GitHub Pages による自動デプロイで Yuji 本人がブラウザで確認できる
- もし「メールで送って」と言われた場合は、本仕様変更を伝え、ウェブサイト URL を案内する

---

## ローカル動作確認

GitHub Pages にデプロイする前にローカルで確認する場合：

```bash
cd /Users/asanoyuujiro/github/research-dashboard/docs
python3 -m http.server 8000
# http://localhost:8000/ を開く
```

`file://` で直接開くと相対パスや fetch() が CORS で動かないことがあるため、必ず `http://` 経由で確認する。
