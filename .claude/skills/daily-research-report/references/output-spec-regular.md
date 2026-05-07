# 通常レポート（HTMLのみ）の出力仕様

**重要: rev3 (2026-05-03) 以降、通常レポートのみを生成する。詳細分析（バージョンB）と DOCX は廃止。**

10本の論文を **同じ分量・同じフォーマットで均等に解説** する。

---

## 必須構成: 10色分けセクションブロック

各論文に以下の **すべての項目を独立した10セクションブロック** として並列に表示する。

| # | セクション名 | クラス | 色 | 分量目安 |
|---|---|---|---|---|
| 1 | ▎一言要約 | `summary` | 青 #3182ce | 3〜4文 |
| 2 | ▎研究概要 | `overview` | 灰 #718096 | 5〜6文（背景・方法・結果・結論を含む） |
| 3 | ▎重要な点 | `importance` | 黄 #d69e2e | 3〜4文 |
| 4 | ▎オリジナリティ | `originality` | 紫 #805ad5 | 3〜4文 |
| 5 | ▎新発見項目 | `discovery` | 緑 #16a34a | 5〜6項目（①②③形式） |
| 6 | ▎方法論評価 | `method` | 緑 #38a169 | 2〜3文 |
| 7 | ▎限界 | `limit` | 赤 #c53030 | 2〜3文 |
| 8 | ▎どんな引用に使えるか | `citation` | 紫 #805ad5 | introduction引用例＋discussion引用例（各2〜3文、統計値含む） |
| 9 | ▎研究への示唆 | `implication` | 紫 #805ad5 | 2〜3文 |
| 10 | ▎研究アイデア | `idea` | ティール #319795 | 2〜3文 |

各セクションのHTML形式：
```html
<div class="section-block summary">
  <span class="section-label">▎一言要約</span>
  <div class="section-content">本研究は…</div>
</div>
```

### CSS仕様

```css
.section-block { margin: 12px 0; padding: 12px 16px; border-radius: 6px; border-left: 4px solid; }
.section-block.summary { background: #ebf8ff; border-left-color: #3182ce; }
.section-block.overview { background: #f7fafc; border-left-color: #718096; }
.section-block.importance { background: #fef5e7; border-left-color: #d69e2e; }
.section-block.originality { background: #faf5ff; border-left-color: #805ad5; }
.section-block.discovery { background: #f0fdf4; border-left-color: #16a34a; }
.section-block.method { background: #f0fff4; border-left-color: #38a169; }
.section-block.limit { background: #fff5f5; border-left-color: #c53030; }
.section-block.citation { background: #faf5ff; border-left-color: #805ad5; }
.section-block.implication { background: #faf5ff; border-left-color: #805ad5; }
.section-block.idea { background: #e6fffa; border-left-color: #319795; }
.section-label { display: inline-block; font-weight: 700; font-size: 12px; color: #1a365d; margin-bottom: 6px; }
.section-content { font-size: 13.5px; line-height: 1.75; }
```

---

## 各セクションの書き方

### 1. ▎一言要約（青）3〜4文
- 結論を凝縮、何を発見したか
- 主要統計値（HR、OR、効果量等）を必ず含める
- 例: 「中年期15年間でWHOガイドラインを一貫達成した女性は全死亡 HR=0.49（95%CI 0.41-0.59）と約半減した。」

### 2. ▎研究概要（灰）5〜6文
背景・方法・結果・結論を全て含める：
- 1〜2文: 背景（なぜこの研究が必要か）
- 2〜3文: 方法（対象、デザイン、主要測定）
- 1〜2文: 結果
- 1文: 結論

### 3. ▎重要な点（黄）3〜4文
- なぜこの研究が重要か
- 分野へのインパクト
- 臨床・公衆衛生応用の可能性

### 4. ▎オリジナリティ（紫）3〜4文
**「先行研究にはなかったこの研究の独自要素」を書く：**
- 「世界初の◯◯コホートでの検証」
- 「△△と××の関連を初めて◯◯デザインで実証」
- 「先行研究では未検討だった××を初めて評価」
- 「機械学習を使って◯◯と××を初めて分類」

### 5. ▎新発見項目（緑）5〜6項目（①②③形式）
**「この研究で新たに明らかになった事実」を数値で書く。**

形式：
```
①散発的MVPA 150分/週で死亡リスク48%低下（HR=0.52, 95%CI 0.45-0.61）を初めて定量化
②総活動量と独立して『多様性』が19%の死亡リスク低減効果
③5,000-7,000歩で変曲点（CVD、認知症、転倒）
④「7,000歩」が「10,000歩」と同等の予防効果
⑤呼吸器疾患死亡で多様性の最大効果（HR=0.59）
```

### オリジナリティ vs 新発見の書き分け
- **オリジナリティ** = "What did they do that's new?"（やり方の新しさ）
- **新発見** = "What did they find that's new?"（結果の新しさ）

### 6. ▎方法論評価（緑）2〜3文
- 統計的妥当性
- バイアス対策の質
- 量反応モデルの適切性

### 7. ▎限界（赤）2〜3文
- 残存交絡
- 外的妥当性
- 測定誤差

### 8. ▎どんな引用に使えるか（紫）introduction＋discussion 2例
**必ず2例を含める：**

```
①[introduction] 認知症リスクの早期予測について論じる際、本研究のp-tau217時計（MAE 3.7年）を「血液マーカーで個人レベルの発症時期予測が可能になった例」として引用できる。

②[discussion] 自分のmulti-organ aging score研究で「脳老化指標としてp-tau217時計を統合する根拠」として、本研究のr=0.73、E-value 2.4を引用し、scoreの妥当性を補強できる。
```

両例とも統計値を必ず含める。

### 9. ▎研究への示唆（紫）2〜3文
- 自分の研究分野（健康寿命・身体機能・筋質・身体活動・認知機能・遺伝子・方法論）との関連
- 自分の研究を補強・拡張する方向性

### 10. ▎研究アイデア（ティール）2〜3文
- 日本コホート（東北メガバンク、JAGES、NCGG等）での応用
- 自分が次に取り組むべき具体的研究テーマ
- PD関連論文の場合は PD研究1/2/3 への接続を明示

---

## ヘッダー部分（論文ごと）

```html
<div class="paper-card top1" 
     data-paper-id="YYYYMMDD_01"
     data-title="..."
     data-authors="..."
     data-journal="..."
     data-design="..."
     data-url="..."
     data-summary="..."
     data-overview="..."
     data-importance="..."
     data-originality="..."
     data-discovery="..."
     data-methodology="..."
     data-limitation="..."
     data-citation="..."
     data-implication="..."
     data-idea="..."
     data-tags="tag1|tag2|tag3">
  <span class="rank-badge">RANK 1</span>
  <span class="task-tag pd">📍 PD研究</span>  <!-- PD関連の場合のみ -->
  <h2>論文タイトル（英語）</h2>
  <div class="meta-line"><strong>著者:</strong> ...</div>
  <div class="meta-line"><strong>ジャーナル・年:</strong> ...</div>
  <div class="meta-line"><strong>研究デザイン:</strong> ...</div>
  <div class="url-line"><a href="...">URL</a></div>
  
  <!-- ここから10セクションブロック -->
  <div class="section-block summary">...</div>
  <div class="section-block overview">...</div>
  <div class="section-block importance">...</div>
  <div class="section-block originality">...</div>
  <div class="section-block discovery">...</div>
  <div class="section-block method">...</div>
  <div class="section-block limit">...</div>
  <div class="section-block citation">...</div>
  <div class="section-block implication">...</div>
  <div class="section-block idea">...</div>
  
  <div class="tags">
    <span class="tag fresh">最新2026</span>
    <span class="tag method">target trial emulation</span>
    <span class="tag theme">中年期</span>
    <span class="tag field">健康寿命</span>
  </div>
</div>
```

---

## ランクバッジ仕様

- RANK 1 → 赤 #c53030
- RANK 2 → オレンジ #d69e2e
- RANK 3 → 緑 #38a169
- RANK 4-10 → 青 #4299e1（デフォルト）

```html
<span class="rank-badge">RANK 1</span>
```

```css
.rank-badge { background: #c53030; color: white; padding: 4px 10px; border-radius: 12px; font-size: 11px; font-weight: 700; }
.paper-card.top1 .rank-badge { background: #c53030; }
.paper-card.top2 .rank-badge { background: #d69e2e; }
.paper-card.top3 .rank-badge { background: #38a169; }
```

---

## PD研究タグ

PD関連論文には：
```html
<span class="task-tag pd">📍 PD研究</span>
```

```css
.task-tag.pd {
  display: inline-block;
  background: #fff5e6;
  color: #c2410c;
  border: 1.5px solid #ea580c;
  padding: 3px 10px;
  border-radius: 4px;
  font-size: 11px;
  font-weight: 700;
  margin-left: 8px;
}
```

`data-tags` にも `PD関連|...` で含める。

---

## まとめ一覧表

最後に10本すべてをカバーする表：

| # | 論文タイトル（短縮） | ジャーナル/年 | デザイン | 主要結果 | PD関連 |
|---|------|-------|---------|---------|---------|
| 1 | ... | Lancet 2026/1 | IPDメタ解析 | +5分/日で6-10%死亡予防 | - |
| 2 | ... | NeuroImage 2026/3 | 縦断研究 | brain age × muscle quality | 📍 |

---

## body 属性（必須）

```html
<body data-source-date="20260505" data-source-theme="身体活動・運動疫学">
```

`data-source-theme` は日本語名でOK（人間可読）。一方ファイル名・URLには `theme_en`（例: `physical-activity-epidemiology`）を使う。`references/website-update-spec.md` を参照。

---

## お気に入り機能JSの読込（rev5: 外部ファイル化）

rev5（2026-05-05）以降、各レポートHTMLは共通JS（`docs/js/favorites.js`）を `<script src>` で読み込む。

```html
<script src="../js/favorites.js"></script>
```

これを `</body>` 直前に書く。旧来の `_inject_to_reports.py` によるインライン注入は廃止。`localStorage` キー（`researchFavorites_v2`）は互換性のため不変。

---

## HTMLヘッダの相対パス（rev5: ウェブサイト運用に対応）

各レポートHTMLは `/Users/asanoyuujiro/github/research-dashboard/docs/reports/` 配下に置かれる。`docs/css/`, `docs/js/`, `docs/index.html` を相対パスで参照する：

```html
<link rel="stylesheet" href="../css/report.css">
<a href="../index.html">← ダッシュボードへ</a>
<script src="../js/favorites.js"></script>
```

詳細は `references/website-update-spec.md` を参照。

---

## ファイル名・保存先（rev5）

- 通常版: `/Users/asanoyuujiro/github/research-dashboard/docs/reports/{YYYYMMDD}_{theme_en}.html`
- 木曜PD特化版: `/Users/asanoyuujiro/github/research-dashboard/docs/reports/{YYYYMMDD}_brain-cognition-pd.html`

`theme_en` の対応表は `references/website-update-spec.md` を参照。

例：
- `/Users/asanoyuujiro/github/research-dashboard/docs/reports/20260505_physical-activity-epidemiology.html`
- `/Users/asanoyuujiro/github/research-dashboard/docs/reports/20260507_brain-cognition.html`
- `/Users/asanoyuujiro/github/research-dashboard/docs/reports/20260507_brain-cognition-pd.html`

**DOCXは生成しない。**

レポート保存後は `docs/data/papers.json` と `docs/data/reports.json` も追記更新する（`references/website-update-spec.md` 参照）。

---

## 過去参考実装

- 2026-04-30 木曜日_脳・認知の例（10セクション色分けの最新版）
- 2026-04-29 水曜日_筋質・体組成の例
