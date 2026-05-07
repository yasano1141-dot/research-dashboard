# 🔴 絶対遵守ルール（永続的に有効）

**このファイルは Yuji が過去に明示的に指示したルールを集約したもの。例外なくすべての daily-research-report 実行で適用する。新規セッション・新規 Claude インスタンスでも同様。**

---

## 1. DOCX生成は絶対に行わない

- 指示日: 2026-04-30、rev3 (2026-05-03) で確定
- 理由: HTMLのみで運用するため
- 違反した場合: ユーザーが明示的にフラストレーションを示す
- 例外: なし
- 影響範囲: `scripts/generate-docx.js`、`scripts/generate-detail-docx.js` は使わない

## 2. 詳細分析レポート（バージョンB）は絶対に作らない

- 指示日: 2026-04-30、rev3 (2026-05-03) で確定
- 理由: 通常レポートの分量を1.2-1.4倍に増やしたため、別途詳細版は不要
- 違反した場合: ユーザーが明示的にフラストレーションを示す
- 例外: なし
- 影響範囲: `templates/detail-report.html`、`templates/email-detail.html` は使わない

## 3. 10色分けセクション様式を絶対に守る

各論文カードは以下の10ブロック構成：

| # | クラス | ラベル | 色 | 分量目安 |
|---|---|---|---|---|
| 1 | `summary` | ▎一言要約 | 青 #3182ce | 3〜4文 |
| 2 | `overview` | ▎研究概要 | 灰 #718096 | 5〜6文（背景・方法・結果・結論を含む） |
| 3 | `importance` | ▎重要な点 | 黄 #d69e2e | 3〜4文 |
| 4 | `originality` | ▎オリジナリティ（独自性） | 紫 #805ad5 | 3〜4文 |
| 5 | `discovery` | ▎新発見項目 | 緑 #16a34a | 5〜6項目（①②③形式） |
| 6 | `method` | ▎方法論評価 | 緑 #38a169 | 2〜3文 |
| 7 | `limit` | ▎限界 | 赤 #c53030 | 2〜3文 |
| 8 | `citation` | ▎どんな引用に使えるか | 紫 #805ad5 | introduction引用例＋discussion引用例（各2〜3文、統計値含む） |
| 9 | `implication` | ▎研究への示唆 | 紫 #805ad5 | 2〜3文 |
| 10 | `idea` | ▎研究アイデア | ティール #319795 | 2〜3文 |

各セクションのHTML形式：
```html
<div class="section-block summary">
  <span class="section-label">▎一言要約</span>
  <div class="section-content">...</div>
</div>
```

## 4. 「どんな引用に使えるか」セクションの内容

このセクションには **2つの引用例** を必ず含める：

- **例1: introduction引用例** — 自分の研究の introduction や background でどう引用できるか（具体的な文脈と論理を示す、統計値必須）
- **例2: discussion引用例** — 自分の研究の discussion でどう引用できるか（自分の結果との対比・補強として、統計値必須）

形式例：
> ①[introduction] 認知症リスクの早期予測について論じる際、本研究のp-tau217時計（MAE 3.7年）を「血液マーカーで個人レベルの発症時期予測が可能になった例」として引用できる。
> ②[discussion] 自分のmulti-organ aging score研究で「脳老化指標としてp-tau217時計を統合する根拠」として、本研究のr=0.73、E-value 2.4を引用し、scoreの妥当性を補強できる。

## 5. data-* 属性の必須追加

各 `<div class="paper-card ...">` opening tag に：

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

`<body>` タグに：
- `data-source-date="YYYYMMDD"`
- `data-source-theme="テーマ名"`

## 6. お気に入り機能JSの必須注入

- 指示日: 2026-04-30、rev3 で再強調
- 注入位置: `</body>` 直前
- マーカー: `<!-- favorites-injected-start -->` 〜 `<!-- favorites-injected-end -->`
- 正典: `/Users/asanoyuujiro/Desktop/3勉強/claudeのファイル/_inject_to_reports.py` の `INJECT_JS` 変数
- 注入方法: `python3 "/Users/asanoyuujiro/Desktop/3勉強/claudeのファイル/_inject_to_reports.py" "{HTMLパス}"`

## 7. PD研究関連を毎日10本中2本以上

- 指示日: 2026-05-03 (rev3)
- 選定キーワード: `references/pd-research-plan.md` を参照
- PD関連論文の表示:
  - `data-tags` に「PD関連」を含める
  - ランクバッジ近くに `<span class="task-tag pd">📍 PD研究</span>` を表示
  - 重要性が高いため Top 5 以内に少なくとも1本は配置
- 違反した場合: ユーザーが「PDが入っていない」と指摘する

## 8. 木曜日は2つのHTMLを生成

- 指示日: 2026-05-03 (rev3)
- ファイル1: `YYYYMMDD_脳認知.html` — 一般的な認知機能・脳研究（10本中6-7本を脳-身体機能関連）
- ファイル2: `YYYYMMDD_脳認知_PD研究特化.html` — PD研究1（脳・筋・SHAP・身体機能）と研究2（運動中EEG）に特化した10本
- メール送信: 通常版＋PD特化版＋パス情報版の **3通**

木曜日の脳-身体機能関連の例:
- 脳容量・脳構造（MRI）と身体機能・サルコペニアの関連（UK Biobank サルコペニア-脳構造-認知 SEM等）
- 運動中脳波・EEG・cortical activity と歩行・バランス（mobile EEG、aperiodic exponent）
- tDCS・rTMS など非侵襲的脳刺激による身体機能介入（tDCS×balance training RCT）
- 運動単位・神経筋接合部・corticospinal control
- 残り3-4本は通常の認知症リスク・予測モデル・疫学方法論

## 9. メール送信は HTML のみ、DOCX 添付禁止

- 指示日: 2026-04-30、rev3 で確定
- メール構成:
  - 通常日（月火水金土日）: 通常レポート＋パス情報の **2通**
  - 木曜日: 通常版＋PD特化版＋パス情報の **3通**
- 詳細分析メールは送らない
- DOCXファイルを添付しない（HTMLでメール内本文として埋め込み）

## 10. 各セクションの分量を1.2-1.4倍に維持

- 指示日: 2026-05-03 (rev3)
- 理由: DOCX・詳細版を廃止した分、通常レポートの情報密度を上げる
- 具体的な分量目安は上記「3. 10色分けセクション様式」を参照

---

## ⚠️ 違反防止チェックリスト（毎回必ず確認）

レポート生成完了直前に以下をすべてチェック：

- [ ] DOCXを作っていないか？（`.docx`ファイルがフォルダに存在しない）
- [ ] 「詳細分析」HTMLを作っていないか？（ファイル名に「詳細分析」が含まれない、木曜の「PD研究特化」は除く）
- [ ] 10セクション色分けで構成されているか？（summary/overview/importance/originality/discovery/method/limit/citation/implication/idea）
- [ ] 「どんな引用に使えるか」セクションがあり、introduction引用例＋discussion引用例の2例が含まれているか？
- [ ] PD研究関連の論文が10本中2本以上含まれているか？
- [ ] PD関連論文に `<span class="task-tag pd">📍 PD研究</span>` バッジが付いているか？
- [ ] PD関連論文の `data-tags` に「PD関連」が含まれているか？
- [ ] お気に入り機能JSが `</body>` 直前に注入されているか？（`<!-- favorites-injected-start -->` を確認）
- [ ] 各 `<div class="paper-card ...">` に `data-paper-id` ほかすべての data-* 属性があるか？
- [ ] `<body>` に `data-source-date` と `data-source-theme` があるか？
- [ ] メールで `<a href="file://...">` を使っていないか？（コピー可能テキスト形式で埋め込む）
- [ ] 木曜日の場合、2つのHTML（一般＋PD特化）と3通のメールを準備したか？

---

## 📝 違反履歴（学習用）

過去の違反パターン（同じミスを繰り返さないために記録）:

- **2026-05-05**: 通常レポート + 詳細分析レポート両方をDOCXとHTMLで作成。9セクション形式（古い形式）を使用、「どんな引用に使えるか」セクションなし、PD研究関連論文ゼロ、お気に入りJS注入なし。
  - 根本原因: スケジュールタスクで使ったSKILL.md（uploadsの古いバージョン）が rev3 を反映していなかった
  - 対策: rev4 でclaude-code-skillsのSKILL.mdを完全更新、 critical-rules.md を独立ファイル化、PD研究計画を別ファイル化

- それ以前にも同様の違反が複数回発生（Yuji が「毎日これ」と指摘）

---

## 🔄 ルール更新の流れ

ルール更新時は：
1. このファイル（`critical-rules.md`）の冒頭に新ルールを追加
2. SKILL.md の「絶対遵守ルール」セクションも同期更新
3. `last_updated` を新しい日付・rev番号に更新
4. ワークスペース直下に `SKILL_updated_YYYYMMDD.md` を残す（履歴保存用）
