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

### 過去の指示の永続化（rev6 / 2026-05-08 時点）

1. **DOCX 生成は絶対に行わない**（HTMLのみで運用、2026-04-30 指示、rev3 にて確定）
2. **詳細分析レポート（バージョンB）は絶対に作らない**（通常レポートのみ、2026-04-30 指示、rev3 にて確定）
3. **10色分けセクションブロック様式（後述）を絶対に守る**（2026-04-30 指示、2026-05-03 再指示）
4. **お気に入りJSは外部ファイル（`../js/favorites.js`）として読み込む**（rev5 で導入。各レポートHTMLは共通JSをsrc参照する）
5. **毎日10本中2本以上を Yuji の PD 研究計画関連にする**（2026-05-03 指示。`references/research-plan/research-plan-extended.md` 必読）
6. **木曜日は2つのHTMLレポート**を作成（`YYYYMMDD_brain-cognition.html` ＋ `YYYYMMDD_brain-cognition-pd.html`）
7. **メール送信は廃止された**（rev5 / 2026-05-05）。Gmail下書き作成・送信などのメール処理は一切行わない。代わりに `docs/data/papers.json` と `docs/data/reports.json` を更新し、ウェブサイト（Vercel）に自動デプロイされる。
8. **🆕 本文の日本語ポリシー**（rev6 / 2026-05-08 指示、rev6.1 / 2026-05-08 詳細化）。

   **英語のままにする**：
   - 論文タイトル（ "Sensitivity Analysis: E-Values" など）
   - 雑誌名（Nature Medicine、Lancet、JAMA、BMJ など）
   - 著者名
   - 専門度の高い手法名（p-hacking、phase angle、target trial emulation、Mendelian randomization、propensity score、causal forest、synthetic control、staggered DiD、SHAP、TMLE、DR-learner、g-formula、DAG など）
   - 略語（MR、HR、OR、AUC、ATE、ATT、ITT、PEHE、E-value、CMC、tDCS、EEG、MRI、CT、DXA、BIA、FA、MD など）
   - 固有名詞（UK Biobank、TMM、JAGES、Nurses' Health Study、SPRINT、ACCORD、OHDSI、CPRD、HRS、ELSA、InCHIANTI など）
   - データ・指標の単位（β=、HR=、OR=、p=、95%CI、I²= など）

   **日本語にする**（一般的な英語の医学・研究語彙）：
   - all-cause mortality → 全原因死亡
   - cardiovascular disease（CVD） → 心血管疾患
   - cancer → ガン（または癌）
   - cohort → コホート
   - reporting standard → 報告の基準（または報告基準）
   - treatment effect → 治療効果
   - sensitivity analysis → 感度分析
   - observational study → 観察研究
   - randomized → ランダム化
   - subgroup → サブグループ
   - regression → 回帰
   - intervention → 介入
   - effect size → 効果サイズ
   - odds ratio → オッズ比（OR は併記可）
   - hazard ratio → ハザード比（HR は併記可）
   - confidence interval → 信頼区間（95%CI は併記可）
   - meta-analysis → メタ解析
   - cross-sectional → 横断的
   - longitudinal → 縦断的
   - bias → バイアス
   - confounder/confounding → 交絡（変数）
   - exposure → 曝露
   - outcome → アウトカム
   - dementia → 認知症
   - frailty → フレイル
   - sarcopenia → サルコペニア
   - gait speed → 歩行速度
   - grip strength → 握力
   - physical activity → 身体活動
   - mediator/mediation → 媒介変数／媒介
   - placebo → プラセボ
   - validation → 検証

   **判断基準**：「日本語論文・教科書で日本語表現が定着している語」は日本語、「研究分野独自の用語で英語のまま読まれている語」は英語のまま。
9. **🆕 同じ論文を重複して紹介しない**（rev6 / 2026-05-08 指示）。レポート生成前に **必ず** `docs/data/papers.json` と `docs/data/reports.json` を読み込み、過去のレポートで紹介済みの論文（タイトル＋ジャーナル＋著者の組み合わせで判定）を除外。新規論文だけで10本を構成する。万一、特に重要な過去論文を再掲する必要がある場合は、本文冒頭で「再掲（前回 YYYY-MM-DD レポート）」と明示する。

11. **🔴 質要件の絶対遵守（rev8 / 2026-05-10 指示）**。

    **背景**：rev6で日本語ポリシー、rev7で実在論文を確立したが、rev6/7以降の実装で文量不足や日本語ポリシー違反が継続発生し、ユーザーから繰り返し指摘を受けた。本ルールでこれを最終決着させる。

    **各論文の最低字数（保存版）**：
    - summary: 300〜500字
    - overview: 700〜1,200字（**背景**・**方法**・**結果**・**結論** の4段構成必須、太字 markdown 装飾）
    - importance: 150〜250字
    - originality: 100〜200字
    - discovery: 300〜600字（**①〜⑩の番号付き、すべて数値・効果サイズ・サンプルサイズ等の具体的事実**）
    - methodology: 150〜250字
    - limitation: 100〜200字
    - citation: 300〜500字（**[introduction]** と **[discussion]** の2文で、効果サイズ・年・雑誌名を必ず併記）
    - implication: 200〜350字（**PD課題1/2/3 もしくは拡張軸への接続を必ず明記**、太字で強調）
    - idea: 250〜400字（**自前データ／TMM／JAGES／UK Biobankへの応用案を3案以上**）

    **これ以下は質要件違反**。1論文の合計が概ね **2,500字以上** であること。

    **日本語ポリシー（rev6.1再掲＋強化）**：
    - **必ず日本語化**する語彙の徹底チェック：all-cause mortality→**全原因死亡**、cardiovascular disease→**心血管疾患**、cancer→**ガン**、cohort→**コホート**、observational study→**観察研究**、randomized→**ランダム化**、treatment effect→**治療効果**、sensitivity analysis→**感度分析**、effect size→**効果サイズ**、hazard ratio→**ハザード比**（HR併記可）、confidence interval→**信頼区間**（95%CI併記可）、meta-analysis→**メタ解析**、systematic review→**システマティックレビュー** または **体系レビュー**、cross-sectional→**横断的**、longitudinal→**縦断的**、bias→**バイアス**、confounder→**交絡変数**、exposure→**曝露**、outcome→**アウトカム**、dementia→**認知症**、frailty→**フレイル**、sarcopenia→**サルコペニア**、gait speed→**歩行速度**、grip strength→**握力**、physical activity→**身体活動**、mediator→**媒介変数**、validation→**検証**、deployment→**実装** または **展開**、benchmark→**ベンチマーク**、framework→**枠組み**、guideline→**ガイドライン**、prediction→**予測**、scoping review→**スコーピングレビュー**
    - **英語のまま許可**：論文タイトル全体、雑誌名、著者名、固有名詞（UK Biobank、TMM、JAGES、Nurses' Health Study等）、略語（HR、OR、AUC、HR、95%CI等）、専門度の高い用語（phase angle、p-hacking、target trial emulation、Mendelian randomization、propensity score、causal forest、synthetic control、staggered DiD、SHAP、TMLE、DR-learner、g-formula、DAG、conformal prediction、causal representation learning、federated learning、foundation model、DINOv2、SAM、CLIP、AlphaFold、Whisper、EEG、MRI、CT、DXA、BIA、FA、MD、CMC、tDCS、tACS、TMS、APOE、GWAS、eQTL、pQTL、RNA-seq、scRNA-seq、ICOPE、IC、FRAIL scale、EWGSOP2、AWGS、SPPB、MoCA、MMSE、CDR、ADNI、NACC、CRP、IL-6、GDF11、GDF15、myostatin、follistatin、GrimAge、DunedinPACE、PhenoAge、OMICmAge、SASP、FAP、senescence、senotherapeutic、Maraviroc、CCR5 等）

    **質チェック手順（自動化済、毎回必ず実行）**：

    1. **質要件の自動検証**（rev9 / 2026-05-10 から強制）：
       ```bash
       python3 scripts/validate_quality.py scripts/{theme}_curated_content.py
       ```
       これで以下が自動チェックされる：
       - 各セクションの最低字数（summary 300字、overview 700字、discovery 300字、…）
       - 1論文の合計字数 ≥ 2,500字
       - 全10論文の合計字数 ≥ 25,000字
       - 日本語ポリシー違反（all-cause mortality、effect size 等の英語残存）

    2. **URL検証（rev7 から強制）**：
       ```bash
       python3 scripts/validate_urls.py scripts/{theme}_curated_content.py
       ```

    3. **生成スクリプトに自動統合済（rev9）**：すべての `generate_{theme}_curated.py` は起動時に validate_urls.py と validate_quality.py を自動実行し、どちらか失敗したら **生成前に exit**。これにより、低品質・fabricated URLのコンテンツでは絶対にレポートが生成されない。

    **本ルール違反は研究倫理違反と同等の重大ミスとして扱い、再発時はユーザーから再度指摘を受ける前に自主的に rev2/rev3 で修正すること**。

    **本ルール違反は研究倫理違反と同等の重大ミスとして扱い、再発時はユーザーから再度指摘を受ける前に自主的に rev2/rev3 で修正すること**。

17. **🟡 コホート多様性のガイドライン（rev14 / 2026-06-02 指示）**。

    **背景**：
    過去のキュレーションで Tuesday の身体活動疫学レポートに UK Biobank ベース論文が 10 本中 7 本まで偏る事象が発生した。UK Biobank は accelerometer 研究の gold standard で含めるべきだが、同一コホートの過剰集中は研究分野の多様性を損なう。

    **指針**：
    - **コホートは特に特定せずに検索する**（特定コホートを除外も優先もしない）
    - 同一コホートに依存する論文は 1 つのレポート内で **目安 3-4 本以下**
    - 検索クエリでは特定コホート名を入れず、テーマで広く検索する（例：「`accelerometer mortality 2026`」「`physical activity older adults 2026`」）
    - 結果として UK Biobank・NHANES・JPHC・JAGES・MESA・ELSA・SHARE・Whitehall II 等のコホートが自然に混在することが望ましい
    - メタ解析・IPD で複数コホートを統合した論文は単一コホート扱いとしない

    **本ルールは soft guideline で違反しても validation で fail はさせない**。エージェント起動時のプロンプトと content 整備時の判断に反映する。

16. **🔴 ジャーナル IF・ジャーナル名・URL の strict 検証（rev13 / 2026-06-01 指示・最重要）**。

    **背景**：
    過去のキュレーションで以下の問題が多発：(1) IF 値を `(IF=確認待ち)` のプレースホルダーのまま放置、(2) ジャーナル名に `/ 関連雑誌` `/ 関連メタ解析` のような曖昧な記述、(3) 日本語化規則がジャーナル名にまで及び `Alzheimer's & Dementia` が `Alzheimer's & 認知症` に化けるバグ、(4) URL が論文と一致していないケース。これらは論文情報の信頼性を根幹から損なう重大ミス。

    **絶対遵守の4点**：

    1. **IF は必ず実値**
       - `(IF=確認待ち)` `(IF=?)` `(IF=未確認)` `(IF=TBD)` 等のプレースホルダー禁止
       - 不明時は WebSearch/SCImago/Clarivate JCR で **必ず実値を取得**
       - 真に IF が存在しないものは `(IF=N/A)` を許容：preprint server（arXiv / bioRxiv / medRxiv）、会議録（NeurIPS / ICML / CVPR）、book/chapter のみ
       - その他のジャーナル査読論文で `IF=N/A` は禁止

    2. **ジャーナル名は publisher 公式表記の verbatim**
       - `/ 関連雑誌` `/ 関連メタ解析` `/ 関連論文` `/ 関連` などの曖昧表記禁止
       - **ジャーナル名は日本語化禁止**（プロパー名のため）：`Alzheimer's & Dementia` を `Alzheimer's & 認知症` にしてはいけない、`Cancer Research` を `ガン Research` にしてはいけない、等
       - 略号も publisher 公式形式（`Eur Heart J` / `JAMA` / `NEJM` / `JAMDA` 等）
       - 巻号・年が判る場合は `Journal Name (IF=X.X), YYYY年（Vol. N, Issue M）` まで明記推奨

    3. **URL は論文と完全一致**
       - DOI / PubMed PMID / 出版社サイト 直リンク
       - 「同分野の論文」「関連 URL」「代表的論文」など曖昧 URL 禁止
       - WebFetch でタイトル・著者を確認し、content の title/authors と一致していることを確かめる
       - 一致しない場合は **論文を差し替える**（URL を捏造しない）

    4. **自動検証（validate_quality.py 強制）**
       - journal フィールドに `IF=確認待ち` `IF=?` `IF=未確認` `IF=TBD` を含む → 違反
       - journal フィールドに `関連雑誌` `関連メタ解析` `関連論文` を含む → 違反
       - journal フィールドの英語部分に `認知症` `ガン` `フレイル` `サルコペニア` 等の日本語混入 → 違反（ジャーナル名は英語のまま保持）
       - IF=N/A は preprint/conference のみ許容、それ以外で `IF=N/A` は違反

    **本ルール違反は研究情報の信頼性損失と同義の重大ミスとして扱う**。

15. **🔴 全レポート共通：論文の公刊年要件（rev12 / 2026-05-13 指示・最重要）**。

    **背景**：
    過去のキュレーションで古い foundational papers（2000-2019）が混在し、研究領域の最新動向が反映されにくい事象が発生した。研究レポートは常に「現在の研究フロンティア」を伝える役割であり、古典的論文ではなく最新エビデンスを中心にすべきという指示を受けた。本ルールは曜日テーマを問わず、すべてのレポート（sunday / monday / tuesday / wednesday / thursday / friday / saturday / pd）に共通して適用する。

    **絶対遵守の3点**：

    1. **直近 3 年以内**：すべての paper の公刊年は `今年 - 3` 以降であること（例：今年が 2026 年なら 2023 年以降）。
    2. **直近 2 週間の論文を 2-3 本**：可能な限り、10 本中 2-3 本は公刊日から 2 週間以内の最新論文を含めること（最低でも 6 か月以内）。
    3. **全体としてできるだけ新しい論文を優先**：「foundational」「古典」「歴史的に重要」だからといって古い論文を入れない。最新論文で同等の知見を提示している論文があれば必ず置換する。

    **3 年以内ルールの例外（極めて限定的に許容）**：
    - 領域の paradigm を最初に確立した論文で、後続にも独立して代替不能なものに限り、最大 1 本だけ 3 年超を許容する。
    - その場合 `tags` に `"foundational"` を入れ、`citation` で「本論文は領域の paradigm を最初に確立した古典であり、近年は X, Y, Z（最新引用）で再評価されている」と明示する。

    **直近 2 週間の論文の探し方（実装プロセス）**：
    - `mcp__plugin_bio-research_consensus__search` で `year_min={今年}` を指定して検索
    - `mcp__plugin_bio-research_consensus__search` で `year_min={今年-1}` で過去 1 年も補完
    - WebSearch で `"<トピック> 2026"` などの最新クエリで補完
    - PubMed の最近インデックスされた PMID（40,000,000台後半-41,000,000台 が 2025-2026 年公刊の目安）を活用
    - **必ず URL を curl で事前検証**（rev7 ルール）してから採用

    **自動検証（validate_quality.py 強制）**：
    - 各 paper の `journal` フィールドから公刊年を抽出（例：`"Nature Aging (IF=17.0), 2025年"` → `2025`）
    - 公刊年が `今年 - 3` 未満（例：今年=2026 で 2023 未満）→ rev12 違反
    - "foundational" タグ付きの paper は例外として扱うが、コホート内で最大 1 本まで
    - `pre-rev11_needs_verification` の paper は移行措置として年チェックを猶予するが、警告を出力

    **全曜日への適用宣言（rev12 確定）**：
    - 旧版（2026-05-10 以前作成）の content は段階的に rev12 準拠に置き換える
    - 新規 paper 採用時は本ルールを strict に適用
    - 既存 paper の保持判断時も「直近 3 年以内かつ最新動向と整合」を基準とする

    **本ルール違反は研究レポートの中核機能（最新研究動向の伝達）の損失と同義の重大ミスとして扱う**。

14. **🔴 著者名・ジャーナル名の verbatim 確認、IF併記、本文読解の義務（rev11 / 2026-05-10 指示・最重要）**。

    **背景**：
    過去のキュレーション content で、私が論文の著者名・ジャーナル名を曖昧記述・想像補完してしまい、実在の情報と齟齬が発生する事象が複数回発生した。論文紹介の信頼性の根幹に関わる重大ミスのため、以下を恒久ルールとして strict に強制する。

    **絶対遵守の3点**：

    1. **著者名は論文本文／URL先の verbatim を使う**
       - PubMed・出版社サイト・PMC で論文タイトル下に表示されている **正式な著者リスト** をそのままコピー
       - 「Various authors」「関連雑誌」「同分野」など**曖昧表記は禁止**
       - 4名以上の場合は「First A, Second B, Third C, et al.」形式で第3著者まで明記＋et al.
       - 著者名のスペル・ミドルイニシャルも論文表記に揃える

    2. **ジャーナル名は publisher 公式表記＋IF併記**
       - フォーマット：`"journal": "Journal Name (IF=X.X), YYYY年"` （例：`"Nature Aging (IF=17.0), 2025年"`）
       - **IF（Impact Factor）は2023年版以降の公式値**を Clarivate / Journal Citation Reports / publisher サイトで確認
       - IF が確認できない場合は `(IF=N/A)` と明記（**推測値は絶対禁止**）
       - 雑誌名は publisher 公式表記（短縮形は使わない、「BMJ」「JAMA」など固有略号は OK）

    3. **本文を必ず読んでから紹介する（rev11 中核）**
       - **全 paper card に必須フィールド** `"fulltext_status"` を追加：
         - `"read_full"` ：本文（PDF または HTML 全文）を実際に読んだ
         - `"read_abstract_only"` ：abstract のみ読んだ（paywall 等で本文未読）
         - `"read_pmc"` ：PMC オープンアクセス版を読んだ
         - `"could_not_read"` ：本文・abstract いずれもアクセスできなかった（この場合は **その論文を採用しない** が原則）
       - **`could_not_read` の論文は採用しない**。代替論文に差し替える。
       - **`read_abstract_only` の論文を採用する場合は明示**：`limitation` セクションに「本紹介はアブストラクト読解に基づき、本文未読」を明記
       - 本文を読まずに「効果サイズ X」「サンプルサイズ N」「ハザード比 Y」など具体数値を書くことを禁止（abstract に明記されている数値のみ可、それ以外は読んでから書く）

    **自動検証（validate_quality.py 強制）**：
    - journal フィールドに `IF=` の文字列がない → 違反
    - 各 paper card に `fulltext_status` フィールドがない → 違反
    - `fulltext_status` の値が4つの allowed values 以外 → 違反

    **既存 content の扱い（rev11 移行措置）**：
    - rev11 制定（2026-05-10）以前に作成された70論文は、`fulltext_status: "pre-rev11_needs_verification"` を一時的に許可
    - 但し将来の更新時には rev11 strict 準拠（read_full / read_pmc / read_abstract_only いずれか）に修正必須

    **本ルール違反は研究倫理違反と同等の重大ミスとして扱う。論文紹介の信頼性は人間の研究者と同等水準でなければならない**。

13. **🔴 summary（一言要約）と importance（重要な点）から PD/Yuji 接続の言及を排除する（rev10 / 2026-05-10 指示・最重要）**。

    **背景**：
    一言要約と重要な点は「論文そのものの内容」と「研究分野全体の方向性」を伝える役割であり、Yuji 自身の研究テーマとの接続点を入れると論文の意義が個人的文脈に矮小化される。Yuji への接続は別セクション（implication／idea）に明確に分離するのが本来の構造。

    **絶対禁止（summary／importance のみ）**：
    - 「Yuji の研究で…」「Yuji の博士論文で…」「Yuji の自前研究で…」「Yuji の核心研究…」などの自己接続フレーズ
    - 「PD 申請書で…」「PD 課題1／2／3で…」「PD 拡張軸で…」「学振 PD で…」などの PD 課題への接続フレーズ
    - 「TMM・JAGES での再現…」「国立長寿の…」「500名コホートで…」「900名コホートで…」など、Yuji の具体的な研究データへの接続
    - 「PD 申請書での参照論文として…」「博士論文での総説的引用として…」など、Yuji の論文執筆への接続

    **書くべき内容（summary／importance のみ）**：
    - **summary**：論文の研究内容（背景・方法・結果・結論の要点）と、その研究が研究分野で持つ位置付け（regulatory／foundational／milestone／benchmark など）
    - **importance**：その研究分野（老年医学、身体活動疫学、筋質研究 等）における意義、既存研究との関係、研究分野全体の方向性への寄与

    **書いてよいセクション**（PD／Yuji 接続を明記）：
    - **implication**：PD 課題1／2／3 もしくは拡張軸への接続を必ず明記（rev9 既定）
    - **idea**：自前データ／TMM／JAGES／UK Biobank への応用案を3案以上（rev9 既定）
    - **citation**：[discussion] で Yuji の自前研究結果との比較として接続を含めることは可

    **本ルール違反は ALWAYS 修正対象**。生成前に summary／importance を読み返し、Yuji／PD への言及がないことを確認すること。

12. **🔴 実在の論文だけを紹介する（rev7 / 2026-05-09 指示・最重要）**。

    **絶対禁止**：
    - DOI／URLを fabricate する（例：将来の偽の DOI、検証していない URL）
    - 論文タイトルを fabricate する（実在の研究領域から「ありそうなタイトル」を作る）
    - 著者名・雑誌名・発表年を fabricate する
    - 「2026年最新版」など実在しない年の論文を作る

    **必須プロセス**：
    1. WebSearch・PubMed・Google Scholar 等で**実在することを確認**してから論文を選定
    2. URL は実際にブラウザで開ける状態であることを確認（HTTP 200/403=paywall は OK、303=redirect/404=not found は NG）
    3. レポート生成前に `python3 scripts/validate_urls.py scripts/{theme}_curated_content.py` を実行し、すべて pass することを確認
    4. validate_urls.py が NG を返した場合は、その論文を**実在のものに差し替え**てから生成

    **背景（rev7制定の経緯）**：
    過去に rev6 で saturday/friday の curated content を作成した際、私が「ありそうな」論文タイトル・DOI・年（2025-2026年の Nature Medicine など）を fabricate してしまい、ユーザーが原本URLにアクセスすると 404/redirect になる問題が発生した。実在しない論文を紹介することは研究倫理に反し、ユーザーの信頼を著しく損なう重大なミス。再発防止のため、本ルールを最優先の絶対遵守ルールとして永続化する。

    **チェック方法（実装済みツール）**：
    ```bash
    python3 scripts/validate_urls.py scripts/{theme}_curated_content.py
    ```
    すべて HTTP 200 または HTTP 403（paywall）であれば pass。HTTP 303 や 404 は fabricate された URL の可能性が高いので、論文自体を差し替える。

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
- [ ] **🆕 本文の日本語化を確認したか**（英語の長文・専門用語の連発を避けたか、初出英語に日本語訳を付けたか）？
- [ ] **🆕 既存papers.jsonと重複していないか**（10本すべて新規論文か、再掲なら明示しているか）？
- [ ] **🔴 実在の論文だけを紹介しているか**（DOI/URL/タイトル/著者をfabricateしていないか）？
- [ ] **🔴 `python3 scripts/validate_urls.py scripts/{theme}_curated_content.py` を実行し、すべての URL が pass したか**？

詳細は `references/critical-rules.md` を参照。

---

## 起動条件

- ユーザーが「研究レポート作って」「daily research report」「今日の研究論文」などと言った時
- スケジュールタスクとして毎朝7:00 JSTに自動実行（ユーザー側で設定する場合）
- **PD研究専用枠の起動**：ユーザーが「PD研究のレポート作って」「PD専用枠」「PD curated」などと言った時
  → 通常の曜日テーマと並列の独立枠として動作（後述の Step 2-PD 参照）

## 実行手順

### Step 1: 必須参照ファイルを最初に読む

スキル実行前に **必ず** 以下を読むこと：

1. `references/critical-rules.md` — 🔴 絶対遵守ルール（最優先）
2. **`references/research-plan/research-plan-extended.md` — 🔴 Yuji の PD 研究計画（PD申請書原本＋遺伝・オミクス拡張版）。PD研究テーマでは特にこれが正典**
3. `references/pd-research-plan.md` — 旧版（簡易・参考扱い）
4. `references/themes-by-day.md` — 曜日別テーマ
5. `references/priority-journals.md` — 優先ジャーナルと検索戦略
6. `references/researcher-profile.md` — Yuji の研究プロフィール
7. `references/output-spec-regular.md` — 通常レポートの詳細仕様（10セクション）
8. `references/file-naming.md` — ファイル命名規則とフォルダ構造
9. `references/website-update-spec.md` — ウェブサイト連携仕様（papers.json / reports.json 追記）

### Step 2: 今日の曜日テーマを確認

`references/themes-by-day.md` を読み、本日の曜日に対応するテーマを特定する。

### Step 2-PD: PD研究専用枠が起動された場合（曜日とは独立）

ユーザーが「PD研究のレポート」を要求した時：
- テーマ: PD研究（jp: "PD研究", en: "pd-research", color: #be123c）
- ファイル名: `docs/reports/{YYYYMMDD}_pd.html`
- reports.json の weekday: "pd"、theme_jp: "PD研究"、theme_en: "pd-research"、report_type: "regular"
- 検索式: `scripts/themes.json` の `pd` エントリ参照（10種類のクエリ）
- **必読**: `references/research-plan/research-plan-extended.md` を最初に読む
- **10本すべて** がPD計画＋拡張テーマに強く該当（曖昧該当・関連薄は除外）
- 全カードに `<span class="task-tag pd">📍 PD研究</span>` バッジ（10本×PDタグ）
- 各論文の **研究への示唆** には「PD計画の課題1／2／3 または 拡張テーマ（遺伝・オミクス・biobank等）のどれに接続するか」を必ず明記
- 各論文の **研究アイデア** には「Yujiのデータ／TMM／UK Biobankで再現・拡張する具体案」を必ず明記
- 木曜の `_PD研究特化.html`（thursday_pd）とは別物。PD専用枠は曜日に依存しない独立カテゴリ
- `<body data-source-theme="pd-research">` 必須

#### 選定優先軸（research-plan-extended.md より）
**コア軸（PD申請書）**:
- 脳構造／機能／脳波 × 身体機能・運動・歩行
- 筋質（echo intensity・phase angle・水分分画・筋間脂肪）× 身体機能・認知
- 説明可能AI（SHAP）× 高齢者・身体機能・脳・認知
- 非侵襲的脳刺激（tDCS/tACS/TMS）× 身体機能・運動学習
- 運動神経・神経筋接合部 × 加齢

**拡張軸（遺伝・オミクス・biobank）**:
- GWAS／PRS／Mendelian randomization × 筋・身体機能・脳
- DNA メチル化／epigenetic clock（GrimAge・DunedinPACE）× 身体機能・健康寿命
- プロテオーム／メタボローム／トランスクリプトーム × 加齢・筋・脳
- 大規模biobank（TMM／UK Biobank／All of Us／HRS／ELSA）× 身体・脳機能
- 24h CoDA（身体活動・座位・睡眠）× 筋質・脳・認知

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
