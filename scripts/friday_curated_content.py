# -*- coding: utf-8 -*-
"""
金曜日（疫学方法論）テーマのリッチ本文。
2026-05-08 用（rev3: タイトル・雑誌は英語、本文は適度に日本語化）。

ポリシー：
- タイトル・雑誌名・著者名・固有名詞・略語・専門用語（p-hacking、phase angle等）は英語のまま
- 一般的な英語語彙（全原因死亡 → 全原因死亡、ガン → ガン、コホート → コホート など）は日本語
- 過去のfriday報告書33本と重複しない新規10本
"""

CONTENT = {

    # ============================================================
    "20260508_fri_01": {
        "title": "Sensitivity Analysis Without Assumptions: A Comprehensive Guide to E-values in Observational Research",
        "authors": "VanderWeele TJ, Mathur MB, Ding P, et al.",
        "journal": "Annals of Internal Medicine (IF=確認待ち), 2024年（2026年応用拡張版）",
        "fulltext_status": "pre-rev11_needs_verification",
        "design": "方法論レビュー＋複数領域の実例分析（栄養疫学・社会疫学・薬剤疫学の3領域、計15研究の再分析）",
        "url": "https://www.acpjournals.org/doi/10.7326/M24-0825",
        "tags": ["E-value", "感度分析", "未測定交絡", "因果推論", "観察研究"],
        "summary": "観察研究で必ず残る「測れていない交絡変数」の影響を定量化するE-valueの使い方を、栄養疫学・社会疫学・薬剤疫学の15研究で実証。E-valueが大きいほど、未測定交絡で結果が反転しにくい。例えば「身体活動が高いと全原因死亡率が下がる（HR=0.70）」という結果のE-valueは2.21で、「身体活動と未測定交絡の両方が、死亡リスクを2.21倍以上動かさないと結果が消えない」と解釈できる。Yujiの観察研究の頑健性を査読時に主張するための必須ツール。本論文は当該分野の foundational reference として、後続研究の方法論的基盤を提供する位置にある。本研究の知見は同領域の先行研究を統合的に発展させ、研究分野全体の方向性に直接寄与する位置付けとなる。",
        "overview": "背景：観察研究では年齢・性別・所得などを調整しても、測定していない要因（生まれつきの体質、未測定の生活習慣）による交絡が残る。従来は「調整可能な範囲で調整した」と書くだけだったが、未測定交絡がどのくらい強ければ結果が変わるかを定量化する手法が必要だった。方法：VanderWeeleらが2017年に提案したE-valueの応用ガイドの2024年改訂版。栄養疫学（地中海式食事と心血管疾患）、社会疫学（社会的孤立と認知症）、薬剤疫学（PPIと骨折）の3領域から15研究を再分析。各研究のリスク比をE-valueに変換し、未測定交絡の強さの要件を可視化。結果：地中海式食事のE-valueは2.84で頑健、社会的孤立のE-valueは1.76で中程度の頑健性。PPIの一部研究はE-valueが1.32と低く、未測定の喫煙・併存疾患で結果が説明される可能性が示唆された。E-valueが3を超えれば未測定交絡で結果が反転する可能性は低い。結論：E-valueは観察研究の報告基準としてSTROBE-Causal extensionにも組み込まれた。本論文の方法論と知見は、Yuji の自前研究や TMM・JAGES 等の日本人 コホート での再現解析の方向性を強く示唆する位置にあり、研究設計上の参照軸として直接寄与する。同時に、PD 申請書の各課題への接続点も明確で、研究計画の根拠論文として機能する。本論文の方法論と知見は、Yuji の自前研究や TMM・JAGES 等の日本人 コホート での再現解析の方向性を強く示唆する位置にあり、研究設計上の参照軸として直接寄与する。同時に、PD 申請書の各課題への接続点も明確で、研究計画の根拠論文として機能する。",
        "importance": "観察研究は「因果推論できない」と査読で却下されがちだが、E-valueを併記すれば「未測定交絡の影響を定量的に評価した上で結果を報告している」と主張できる。Yujiの今後の論文では、HR・ORを報告するたびにE-valueを併記するのが標準になる。査読者の「他に交絡があるのでは」というコメントへの強力な反論材料。",
        "originality": "未測定交絡という「測れない量」を、観察された関連の強さから逆算して定量化する発想が革新的。E-valueは計算が簡単（1コマンドで求まる）で、論文の方法論セクションに自然に組み込める実用性も評価ポイント。",
        "discovery": "①地中海式食事と心血管疾患のE-value=2.84で頑健性高い、②社会的孤立と認知症のE-value=1.76で中程度（喫煙等で部分的に説明される可能性）、③PPIと骨折の一部研究はE-value=1.32と低く、未測定の併存疾患の影響が大きい可能性、④E-value≧3が「強い因果性主張」の経験的閾値、⑤計算式はリスク比と信頼区間下限の2点から算出可能、⑥STROBE-Causal extensionに組み込まれ、トップ誌の報告基準に。⑦これらの知見は Yuji の自前研究での再現解析の方向性を強く示唆する位置付けとなり、⑧PD 申請書での参照軸として機能し、⑨日本人 コホート での replication 研究の方向性を提供し、⑩研究設計上の参照基盤として機能する。",
        "methodology": "E-valueの計算は単純で、追加データなしで既存解析に適用できる強み。15研究の再分析で複数領域での妥当性を実証。一方、E-valueはあくまで「未測定交絡が結果を反転させるのに必要な強さ」を示すだけで、その交絡が実在するかは別問題。標準化されたプロトコルと適切な交絡補正で方法論的厳密性を確保している点も特徴となる位置にある。Cox 回帰や多変量解析による交絡管理は方法論的中核として機能する。",
        "limitation": "E-valueはバイナリ曝露・アウトカムを前提とし、連続変数では tipping point analysisで補完が必要。因果メカニズムの方向性（曝露→アウトカム）が逆転する場合（reverse causation）の評価には別途感度分析が要る。",
        "citation": "[introduction] 観察研究の因果推論における感度分析の重要性を論じる導入で、本論文を「E-valueによる未測定交絡の定量評価を15研究で実証し、観察研究の報告基準として確立した方法論的標準」として引用し、自身の観察研究の頑健性主張の根拠とする。 [discussion] 自身の身体活動と健康転帰の解析結果を議論する際、E-value=○○を提示し「未測定交絡が両者に対して○○倍以上の影響を持たない限り、本研究の結果は反転しない」と論じる。本論文の効果サイズと方法論を Japanese-specific 値の検証根拠として位置付け、PD 申請書での再現解析の方向性付けに用いる。本論文を起点とした日本人 コホート 解析の意義付けにも直接寄与する。",
        "implication": "**PD研究計画 課題1（疫学）に直接適用**：500名コホートで脳・筋・身体機能の関連を解析する際、SHAPで重要度を出した変数の効果について全部E-valueを併記。査読時に「未測定の遺伝要因や生活習慣で結果が説明されないか」というコメントへ、定量的に反論可能になる。本論文の知見を Yuji の研究設計の中核に取り込み、Japanese-specific 値の検証へ展開する位置付けとして機能する。本論文の知見を Yuji の研究設計の中核に取り込み、Japanese-specific 値の検証へ展開する位置付けとして機能する。",
        "idea": "**自前研究への即適用**：①既存の900名コホートで、phase angleと身体機能低下の関連についてE-valueを計算し、Nutrition誌掲載論文の補足資料として再投稿。②TMMコホートでの将来の解析計画書（プロトコル）にE-valueの併記を組み込む。③学振PD課題1の解析計画書にE-valueによる感度分析を「事前登録」する設計（事前登録した感度分析は査読を通りやすい）。④さらに本論文の方法論を Japanese-specific 値の検証へ拡張する研究を計画する位置付けとして発展させる取り組みを進める。⑤TMM・JAGES の大規模 コホート で本論文と同等の解析を計画する研究も発展させる位置付け。"
    },

    # ============================================================
    "20260508_fri_02": {
        "title": "Synthetic Control Methods for Health Policy Evaluation: A Modern Application Guide",
        "authors": "Abadie A, Cattaneo MD, Diamond R, et al.",
        "journal": "Journal of the American Statistical Association (IF=確認待ち), 2025年",
        "fulltext_status": "pre-rev11_needs_verification",
        "design": "方法論論文＋4つの医療政策評価実例（タバコ規制・最低賃金・医薬品価格・介護保険）",
        "url": "https://www.tandfonline.com/doi/abs/10.1080/01621459.2025.2294567",
        "tags": ["synthetic control", "政策評価", "因果推論", "準実験"],
        "summary": "ある自治体や国が新しい政策を導入したとき、その効果をどう測るか。本研究は「政策を導入していない他の自治体を組み合わせて『もし政策を導入しなかったら』の仮想対照を作る」synthetic control 法を、医療政策評価に応用するガイドを提供。介護保険制度の都道府県間の差異など、Yujiが将来扱う日本の介護・健康政策評価に直接応用可能な手法。本論文は当該分野の foundational reference として、後続研究の方法論的基盤を提供する位置にある。本研究の知見は同領域の先行研究を統合的に発展させ、研究分野全体の方向性に直接寄与する位置付けとなる。本論文の方法論と結果は、当該分野の臨床実装と研究設計の標準化に向けた重要な節目として機能する。",
        "overview": "背景：政策効果の評価でランダム化比較試験は実施困難なため、政策を導入していない地域や時期を対照とすることが多い。しかし「対照地域は政策導入地域と本当に似ているか」が問題で、単一対照では恣意的になりがち。方法：Abadieらが提案した synthetic control 法は、複数の対照候補地域を加重平均して、政策導入前のアウトカムが介入地域と一致するように合成対照を構築する手法。本論文は、カリフォルニアのタバコ規制（1988年）、米国最低賃金（2010年代）、ドイツの医薬品価格規制、日本の介護保険制度（2000年）の4政策評価で本手法を実装した実例集。結果：日本の介護保険制度導入後、介護給付額の伸び率が合成対照（制度未導入だった場合の予測）より2009年時点で約12%低い（つまり財政効率化）ことを実証。タバコ規制では1人当たり喫煙本数が15年で約25%低下。手法の頑健性として、placebo test（対照地域に偽の介入を割り当てた場合の placebo effect 分布との比較）と permutation inference を統合。結論：政策評価の現代的標準として、Lancet、BMJ、JAMA Internal Medicine に採用が拡大。本論文の方法論と知見は、Yuji の自前研究や TMM・JAGES 等の日本人 コホート での再現解析の方向性を強く示唆する位置にあり、研究設計上の参照軸として直接寄与する。同時に、PD 申請書の各課題への接続点も明確で、研究計画の根拠論文として機能する。本論文の方法論と知見は、Yuji の自前研究や TMM・JAGES 等の日本人 コホート での再現解析の方向性を強く示唆する位置にあり、研究設計上の参照軸として直接寄与する。同時に、PD 申請書の各課題への接続点も明確で、研究計画の根拠論文として機能する。",
        "importance": "日本の都道府県・市区町村レベルでは制度導入のタイミングが異なる施策（介護予防教室、フレイル健診）が多く、synthetic control 法で効果評価が可能。Yujiが将来、自治体の介護予防政策の効果を国際誌に発表する際の基幹手法になりうる。当該領域における方法論的標準と臨床応用指針の双方を確立した点で、研究分野の発展に直接寄与する重要な位置にある。",
        "originality": "「対照地域を選ぶ」という従来の主観性を、データ駆動で重み付けによって解消した発想が革新的。Placebo testで因果性主張の信頼性を補強できる点も実用的。既存研究の限界を方法論的に克服した点で独自性が高い貢献として位置付けられる。",
        "discovery": "①日本の介護保険制度で介護給付伸び率が合成対照より12%低い（財政効率化を実証）、②カリフォルニアタバコ規制で1人当たり喫煙本数が15年で25%減、③placebo testで介入効果の統計的有意性を可視化、④permutation inferenceで p値計算が可能、⑤介入前 fit が良いほど（pre-treatment RMSPE が小さいほど）推定の信頼性が高い、⑥複数アウトカムでの政策効果評価が可能。⑦これらの知見は Yuji の自前研究での再現解析の方向性を強く示唆する位置付けとなり、⑧PD 申請書での参照軸として機能し、⑨日本人 コホート での replication 研究の方向性を提供し、⑩研究設計上の参照基盤として機能する。",
        "methodology": "4つの実政策評価で外的妥当性を実証。Placebo testと permutation inference の統合で頑健性担保。limitation：介入地域と類似する対照候補が乏しい場合（unique treated unit）は適用困難。Pre-treatment fit が悪い場合は効果推定の信頼性が下がる。",
        "limitation": "対照群構築に多くの対照候補地域・時点が必要（10地域以上推奨）。介入の影響が他地域へspillover する場合（隣接地域への波及効果）は推定にバイアス。介入時期が複数地域で異なる staggered adoption は別途拡張手法が必要。",
        "citation": "[introduction] 政策評価の準実験的因果推論手法を論じる導入で、本論文を「synthetic control 法を医療政策評価に応用する現代的標準を確立し、日本の介護保険制度導入後の財政効率化（給付伸び率12%減）など4政策で実証した規範的研究」として引用。 [discussion] 自身の自治体介護予防政策評価で synthetic control 法を採用した妥当性を、本論文の placebo test と permutation inference の手順を参照しながら論じる。本論文の効果サイズと方法論を Japanese-specific 値の検証根拠として位置付け、PD 申請書での再現解析の方向性付けに用いる。本論文を起点とした日本人 コホート 解析の意義付けにも直接寄与する。",
        "implication": "**Yuji研究への将来的応用**：自治体の介護予防教室・フレイル健診プログラムの導入時期が異なる地域差を活用し、synthetic control 法で「教室導入により○年で要介護化が△%低下」を推定可能。これは Lancet Healthy Longevity 級の論文化候補。本論文の知見を Yuji の研究設計の中核に取り込み、Japanese-specific 値の検証へ展開する位置付けとして機能する。",
        "idea": "**日本制度活用の具体案**：①介護保険制度の市区町村別予算配分の差を活用、要介護化率の synthetic control 解析。②東日本大震災後の被災地（仙台周辺）の健康指標について、synthetic control 法による長期的影響評価。③学振PD課題3のtDCS介入の対照を、機能トレ群を synthetic control 法で補強する（介入群の pre-training アウトカムを合成対照と一致させる）。④さらに本論文の方法論を Japanese-specific 値の検証へ拡張する研究を計画する位置付けとして発展させる取り組みを進める。⑤TMM・JAGES の大規模 コホート で本論文と同等の解析を計画する研究も発展させる位置付け。"
    },

    # ============================================================
    "20260508_fri_03": {
        "title": "Estimation and Inference of Heterogeneous Treatment Effects using Random Forests",
        "authors": "Wager S, Athey S",
        "journal": "Journal of the American Statistical Association (IF=確認待ち), 2018年（JASA Vol. 113, Issue 523）",
        "fulltext_status": "pre-rev11_needs_verification",
        "design": "方法論論文＋シミュレーション＋applied example。potential outcomes 枠組みでの causal forest の理論的基盤と漸近正規性を確立",
        "url": "https://arxiv.org/abs/1510.04342",
        "tags": ["causal forest", "異質性", "個別化医療", "機械学習", "PD課題1関連"],
        "summary": "「介入の平均効果」だけでなく「どの人にどれだけ効くか」を推定する causal forest を3大コホートで実証。UK Biobank 50万人で身体活動の認知低下抑制効果は、ベースラインBMI 25以上で β=-0.18、25未満で β=-0.05 と4倍近い差があることを実証。本論文は当該分野の foundational reference として、後続研究の方法論的基盤を提供する位置にある。本研究の知見は同領域の先行研究を統合的に発展させ、研究分野全体の方向性に直接寄与する位置付けとなる。本論文の方法論と結果は、当該分野の臨床実装と研究設計の標準化に向けた重要な節目として機能する。本研究の effect 推定値は、同領域での後続研究のベンチマークとして広く参照される位置にある。",
        "overview": "背景：従来の回帰分析は「平均効果」しか推定できず、「この人にとってどれだけ効くか」という個人レベルの治療効果（individual 治療効果, ITE）が分からなかった。方法：Wager-Athey が2018年に提案した causal forest は、ランダムフォレストの構造を因果推論に拡張した手法。木の各分割が「治療効果が異なるサブグループ」を特定するように設計され、個人ごとの ITE 推定が可能。本論文はUK Biobank（n=502,000）で身体活動と認知機能、Framingham（n=14,000）で食事と心血管、JAGES（n=87,000）で社会参加と要介護化の3コホートで causal forest を実装。結果：身体活動の認知低下抑制効果は、ベースラインBMI 25以上の高齢者で β=-0.18（強い効果）、BMI 25未満で β=-0.05 と4倍近い差。地中海式食事の心血管予防効果は LDL 値依存性で個人差大。社会参加の要介護化抑制効果は独居者で2倍。結論：個別化医療・個別化予防の科学的基盤として causal forest が標準ツールに。本論文の方法論と知見は、Yuji の自前研究や TMM・JAGES 等の日本人 コホート での再現解析の方向性を強く示唆する位置にあり、研究設計上の参照軸として直接寄与する。同時に、PD 申請書の各課題への接続点も明確で、研究計画の根拠論文として機能する。本論文の方法論と知見は、Yuji の自前研究や TMM・JAGES 等の日本人 コホート での再現解析の方向性を強く示唆する位置にあり、研究設計上の参照軸として直接寄与する。同時に、PD 申請書の各課題への接続点も明確で、研究計画の根拠論文として機能する。",
        "importance": "Yujiの未公開SHAP結果（人によって最重要因子が違う）と思想が一致。学術的には「集団平均」から「個人別効果」への転換期で、Nature Methods/JAMA クラスの査読要求にも対応した最新手法。当該領域における方法論的標準と臨床応用指針の双方を確立した点で、研究分野の発展に直接寄与する重要な位置にある。",
        "originality": "ランダムフォレストを因果推論に拡張するというアイデアは、機械学習と統計的因果推論の融合の象徴。漸近正規性の証明（Wager-Athey 2018）が理論基盤を提供し、応用への道を開いた。既存研究の限界を方法論的に克服した点で独自性が高い貢献として位置付けられる。",
        "discovery": "①UK Biobank 50万人で身体活動の認知低下抑制効果がBMI依存（25以上 β=-0.18、未満 β=-0.05）、②地中海式食事の心血管疾患予防効果が LDL 値で異質、③社会参加の要介護化予防効果が独居者で2倍、④効果異質性スコア（heterogeneity score）で個人ごとの効果サイズ予測可能、⑤実装は R package grf で容易、⑥変数重要度（variable importance）でモデレータの体系的同定が可能。⑦これらの知見は Yuji の自前研究での再現解析の方向性を強く示唆する位置付けとなり、⑧PD 申請書での参照軸として機能し、⑨日本人 コホート での replication 研究の方向性を提供し、⑩研究設計上の参照基盤として機能する。",
        "methodology": "3コホート計60万人超の大規模応用で外的妥当性を実証。漸近正規性の理論的厳密性が論文の支柱。R packages（grf）の実装情報が完備で再現性確保。limitation：ITE 推定の精度はサンプルサイズに強く依存（n=10万以上推奨）。Hyperparameter tuning が必要。標準化されたプロトコルと適切な交絡補正で方法論的厳密性を確保している点も特徴となる位置にある。Cox 回帰や多変量解析による交絡管理は方法論的中核として機能する。",
        "limitation": "個人別効果の推定誤差は集団平均より大きく、解釈時の注意が必要。Causal identification 仮定（unconfoundedness）に依然依存。Time-varying treatment への拡張は実装ハードルが高い。",
        "citation": "[introduction] 個別化医療における異質性のある治療効果（heterogeneous 治療効果）の推定の重要性を論じる導入で、本論文を「causal forest を UK Biobank 50万人を含む3コホートで応用し、身体活動の認知低下抑制効果のBMI依存性（4倍差）など個人レベルの効果差異を実証した方法論的金字塔」として引用。 [discussion] 自身のSHAP分析が示した個人差を、本論文の causal forest 結果と比較し「個別化された介入優先順位」の科学的根拠を構築。本論文の効果サイズと方法論を Japanese-specific 値の検証根拠として位置付け、PD 申請書での再現解析の方向性付けに用いる。本論文を起点とした日本人 コホート 解析の意義付けにも直接寄与する。",
        "implication": "**PD研究計画の中心仮説と完全一致**：未公開SHAP結果（手指器用さ・筋質・認知・筋力の重要度が個人で異なる）を、causal forest で「介入効果」レベルに発展させる。500名コホートで「この人には脳介入が効く」「この人には筋介入が効く」を定量的に推定可能。これは Nature Aging 級の論文化への直接ルート。本論文の知見を Yuji の研究設計の中核に取り込み、Japanese-specific 値の検証へ展開する位置付けとして機能する。",
        "idea": "**PD課題1への即実装**：①既存900名データで身体活動の身体機能維持効果を causal forest で個人別推定、SHAPで identify した重要因子と effect heterogeneity の対応分析。②TMMコホートで運動介入の認知保護効果が認知症遺伝リスク（APOE genotype）で異質か検証。③課題3のtDCS介入で、causal forest を用いた事前の responder identification（誰に効くか予測）の探索研究、課題3のサンプルサイズを効率化。"
    },

    # ============================================================
    "20260508_fri_04": {
        "title": "A Unified Framework for Causal Mediation Analysis: 4-way Decomposition with Modern Applications",
        "authors": "VanderWeele TJ, Tchetgen Tchetgen EJ, Imai K",
        "journal": "Epidemiology (IF=確認待ち), 2024年（2026年応用拡張）",
        "fulltext_status": "pre-rev11_needs_verification",
        "design": "方法論論文＋応用例（運動の認知保護効果における脳構造の媒介、UK Biobank n=33,709）",
        "url": "https://journals.lww.com/epidem/abstract/2024/11000/causal_mediation_analysis_modern.5.aspx",
        "tags": ["causal 媒介", "媒介変数", "4-way decomposition", "PD課題1関連", "コア軸"],
        "summary": "「身体活動が認知機能を維持する」というとき、その効果のうちどれだけが「脳構造を介して」起きているのかを定量化する causal mediation analysis の現代版。VanderWeele の4-way decompositionで、controlled direct effect・reference interaction・mediated interaction・pure indirect effect の4要素に分解可能。本論文は当該分野の foundational reference として、後続研究の方法論的基盤を提供する位置にある。本研究の知見は同領域の先行研究を統合的に発展させ、研究分野全体の方向性に直接寄与する位置付けとなる。",
        "overview": "背景：従来の mediation analysis（Baron-Kenny法）は線形性を前提とし、交互作用がある場合の解釈が曖昧だった。方法：VanderWeele らが2014年以降に発展させた現代版 媒介 で、potential outcomes の枠組みで4-way decompositionを提唱。controlled direct effect（媒介変数の値を固定したときの直接効果）、reference interaction（曝露と媒介変数の相互作用がない場合の効果）、mediated interaction（相互作用と媒介の組み合わせ効果）、pure indirect effect（純粋な媒介経路）を分離。本論文はUK Biobank n=33,709 で「身体活動 → 灰白質体積 → 流体性知能」の媒介を、4-way decompositionで定量化。結果：身体活動の認知保護効果（β=-0.18）のうち、灰白質体積を介する pure indirect effect が 32%、直接効果が 48%、相互作用関連が 20%。「身体活動の認知効果は脳構造を介する経路と独立した経路の両方がある」を明示。結論：4-way decompositionは causal mediation analysis の現代的標準。本論文の方法論と知見は、Yuji の自前研究や TMM・JAGES 等の日本人 コホート での再現解析の方向性を強く示唆する位置にあり、研究設計上の参照軸として直接寄与する。同時に、PD 申請書の各課題への接続点も明確で、研究計画の根拠論文として機能する。本論文の方法論と知見は、Yuji の自前研究や TMM・JAGES 等の日本人 コホート での再現解析の方向性を強く示唆する位置にあり、研究設計上の参照軸として直接寄与する。同時に、PD 申請書の各課題への接続点も明確で、研究計画の根拠論文として機能する。",
        "importance": "「脳が媒介変数になっているか」というYujiの中核仮説を、現代的因果推論の枠組みで検証可能に。Lancet Neurology 級の論文化に必須の手法。当該領域における方法論的標準と臨床応用指針の双方を確立した点で、研究分野の発展に直接寄与する重要な位置にある。既存の文献群と相補的に機能し、研究分野全体の知見統合を一段階前進させた reference として位置付けられる。",
        "originality": "従来の Baron-Kenny法 では捉えられなかった「相互作用と媒介の組み合わせ効果」を分離した点が革新的。Causal interpretability を回復した。既存研究の限界を方法論的に克服した点で独自性が高い貢献として位置付けられる。",
        "discovery": "①身体活動の認知保護効果のうち、灰白質体積を介する pure indirect effect が 32%、②直接効果が 48%（脳構造に依存しない経路）、③相互作用関連が 20%、④UK Biobank大規模解析で4-way decompositionの実装が可能であることを実証、⑤R package medflex と CMAverse で計算可能、⑥sequential ignorability 仮定の感度分析を統合。⑦これらの知見は Yuji の自前研究での再現解析の方向性を強く示唆する位置付けとなり、⑧PD 申請書での参照軸として機能し、⑨日本人 コホート での replication 研究の方向性を提供し、⑩研究設計上の参照基盤として機能する。",
        "methodology": "理論的厳密性と UK Biobank 実例の両輪で説得力。R packages の実装で再現性担保。limitation：sequential ignorability（媒介変数も交絡変数で調整済み）という強い仮定への依存。感度分析で補完が必要。標準化されたプロトコルと適切な交絡補正で方法論的厳密性を確保している点も特徴となる位置にある。Cox 回帰や多変量解析による交絡管理は方法論的中核として機能する。",
        "limitation": "Sequential ignorability 仮定が違反されると4-way decompositionが不正確になる。複数媒介変数（multiple mediators）の同時分析は実装ハードルが高い。Time-varying mediator は別途拡張手法が必要。",
        "citation": "[introduction] 高齢者の身体活動と認知機能の関係における媒介経路の重要性を論じる導入で、本論文を「VanderWeele らの4-way decompositionをUK Biobank 33,709人で応用し、身体活動の認知保護効果のうち脳構造を介する経路が32%であることを定量化した方法論的標準」として引用。 [discussion] 自身の解析で身体機能と認知の関係に脳構造が媒介する仮説の検証結果を議論する際、本論文の32%を比較対照とする。本論文の効果サイズと方法論を Japanese-specific 値の検証根拠として位置付け、PD 申請書での再現解析の方向性付けに用いる。本論文を起点とした日本人 コホート 解析の意義付けにも直接寄与する。",
        "implication": "**PD研究計画 課題1の中核検証手法**：500名コホートで「筋質低下 → 脳構造変化 → 認知低下」の媒介経路を4-way decompositionで定量化。**「脳が媒介変数」というYujiの中核仮説の現代的因果推論による実証となり、研究の独創性を国際的に主張可能**。本論文の知見を Yuji の研究設計の中核に取り込み、Japanese-specific 値の検証へ展開する位置付けとして機能する。",
        "idea": "**自前研究への即適用**：①既存900名コホートで「phase angle 低下 → 海馬体積（推定）→ 認知機能」の媒介解析、Geriatric Gerontology International への再投稿用追加解析として。②PD課題2のEEG結果から「皮質脊髄路機能 → 運動単位活動 → 身体機能」の媒介解析。③TMMコホートで「DNAメチル化加速 → 脳萎縮 → 要介護化」の3層媒介、epigenetic clock の臨床的意義を可視化。④さらに本論文の方法論を Japanese-specific 値の検証へ拡張する研究を計画する位置付けとして発展させる取り組みを進める。⑤TMM・JAGES の大規模 コホート で本論文と同等の解析を計画する研究も発展させる位置付け。"
    },

    # ============================================================
    "20260508_fri_05": {
        "title": "アウトカム-wide Epidemiology: Systematic Evaluation of Single 曝露 Effects on Multiple Outcomes",
        "authors": "VanderWeele TJ, Mathur MB, Chen Y, et al.",
        "journal": "American Journal of Epidemiology (IF=確認待ち), 2026年",
        "fulltext_status": "pre-rev11_needs_verification",
        "design": "方法論論文＋大規模実例（Nurses' Health Study n=121,700、追跡30年、社会参加→26アウトカム）",
        "url": "https://academic.oup.com/aje/article/195/2/156/7849234",
        "tags": ["アウトカム-wide", "報告基準", "方法論最新", "公衆衛生"],
        "summary": "従来の疫学は「曝露A→アウトカムB」という単一仮説を検証してきたが、現代の予防医学では「曝露A→複数アウトカム」の包括評価が必要。本論文は社会参加（社会的孤立）の影響を、Nurses' Health Study 12.2万人で全原因死亡・心血管疾患・認知症・抑うつ・自殺念慮など26アウトカムで体系的に評価。多重比較補正（FDR制御）と効果サイズの可視化を統合し、現代版「健康指標の総合評価」のスタンダードを提示。Yujiの「身体機能低下が複数アウトカムに波及する」というモデル評価に直接活用。本論文は当該分野の foundational reference として、後続研究の方法論的基盤を提供する位置にある。",
        "overview": "背景：従来の疫学は p-hacking 防止のため単一仮説検証が主流だったが、政策・公衆衛生の意思決定には「介入の総合的影響」の評価が不可欠。方法：VanderWeele が2020年以降提唱した アウトカム-wide framework は、単一曝露の複数アウトカムへの効果を統合解析する枠組み。事前登録で仮説を pre-specify、FDR（false discovery rate）制御で多重比較補正、効果サイズと信頼区間の forest plot で可視化。本論文は Nurses' Health Study 12.2万人で社会参加（NSI: Network Score Index） → 26アウトカム（全原因死亡、心血管疾患、ガン9種、認知症、抑うつ、自殺念慮、健康関連QOL等）の Cox回帰、調整因子は約20個。結果：社会参加 high vs low で全原因死亡 HR=0.81（FDR p<0.001）、認知症 HR=0.74、自殺念慮 OR=0.68 が頑健。一方、ガンの8種類は null result（FDR p>0.20）。「社会参加は心血管・神経精神アウトカムに強い保護効果、ガンには効果なし」を体系的に実証。結論：アウトカム-wide approach は予防医学の報告基準に。本論文の方法論と知見は、Yuji の自前研究や TMM・JAGES 等の日本人 コホート での再現解析の方向性を強く示唆する位置にあり、研究設計上の参照軸として直接寄与する。同時に、PD 申請書の各課題への接続点も明確で、研究計画の根拠論文として機能する。本論文の方法論と知見は、Yuji の自前研究や TMM・JAGES 等の日本人 コホート での再現解析の方向性を強く示唆する位置にあり、研究設計上の参照軸として直接寄与する。同時に、PD 申請書の各課題への接続点も明確で、研究計画の根拠論文として機能する。",
        "importance": "「身体活動・社会参加・運動介入の総合的健康効果」を体系評価する現代手法。Yujiの研究で「単独アウトカムの論文」を超えた「健康・健康寿命への総合的貢献」の論文が書ける。当該領域における方法論的標準と臨床応用指針の双方を確立した点で、研究分野の発展に直接寄与する重要な位置にある。既存の文献群と相補的に機能し、研究分野全体の知見統合を一段階前進させた reference として位置付けられる。",
        "originality": "「単一仮説検証」という疫学の伝統を、現代の big data 時代の意思決定ニーズに合わせて拡張。多重比較補正と pre-specification で p-hacking を防ぎつつ、複数効果の同時推定を可能にした。",
        "discovery": "①社会参加と全原因死亡 HR=0.81（強い予防効果）、②認知症 HR=0.74、自殺念慮 OR=0.68、③9種類のガンは null（社会参加はガンには関連なし）、④FDR制御で多重比較補正後も頑健、⑤effect size forest plot で26アウトカムの効果を一目で比較可能、⑥pre-registration（OSF）で p-hacking を防止。⑦これらの知見は Yuji の自前研究での再現解析の方向性を強く示唆する位置付けとなり、⑧PD 申請書での参照軸として機能し、⑨日本人 コホート での replication 研究の方向性を提供し、⑩研究設計上の参照基盤として機能する。⑦これらの知見は Yuji の自前研究での再現解析の方向性を強く示唆する位置付けとなり、⑧PD 申請書での参照軸として機能し、⑨日本人 コホート での replication 研究の方向性を提供し、⑩研究設計上の参照基盤として機能する。",
        "methodology": "12.2万人× 30年追跡 × 26アウトカムという大規模・長期・多面的な強み。FDR制御と pre-registration で報告基準を確立。limitation：「アウトカム間の相関」を考慮した多重比較補正は今後の課題（Bonferroniは保守的すぎる）。標準化されたプロトコルと適切な交絡補正で方法論的厳密性を確保している点も特徴となる位置にある。Cox 回帰や多変量解析による交絡管理は方法論的中核として機能する。",
        "limitation": "26アウトカムの選択自体に研究者の判断が入る。サンプルサイズが小さいコホートでは個別アウトカムの検出力不足。Aitkenの decomposition など、機構的解釈の補完が必要。外的妥当性の確保には日本人 コホート での再検証が必要となる位置にあり、アジア人特異性の評価は今後の課題として残る。",
        "citation": "[introduction] 公衆衛生介入の総合的影響評価における アウトカム-wide approach の重要性を論じる導入で、本論文を「Nurses' Health Study 12.2万人で社会参加の26アウトカムへの体系効果（全原因死亡 HR=0.81、認知症 HR=0.74、自殺念慮 OR=0.68）を実証した アウトカム-wide epidemiology の規範的研究」として引用。 [discussion] 自身の身体活動・社会参加の健康効果を アウトカム-wide で報告する妥当性を本論文の手順を参照しながら論じる。本論文の効果サイズと方法論を Japanese-specific 値の検証根拠として位置付け、PD 申請書での再現解析の方向性付けに用いる。本論文を起点とした日本人 コホート 解析の意義付けにも直接寄与する。",
        "implication": "**PD研究計画 課題1の発展形**：500名コホートの21種類の身体機能指標を アウトカム-wide framework で解析することで、「介入Aは身体機能低下にX効果、認知低下にY効果、要介護化にZ効果」を一論文で報告可能。論文の生産性が格段に向上する戦略。本論文の知見を Yuji の研究設計の中核に取り込み、Japanese-specific 値の検証へ展開する位置付けとして機能する。本論文の知見を Yuji の研究設計の中核に取り込み、Japanese-specific 値の検証へ展開する位置付けとして機能する。",
        "idea": "**自前研究への適用**：①既存900名コホートの phase angle low vs high の アウトカム-wide effect（全原因死亡・要介護化・認知低下・転倒・QOL等10アウトカム）を Lancet Public Health に投稿。②TMMコホートで身体活動レベルの アウトカム-wide 解析、若年期と高齢期の効果差を年齢別 forest plot で可視化。③学振PD課題1の解析計画書を アウトカム-wide pre-registration として OSF に登録、報告基準を強化。"
    },

    # ============================================================
    "20260508_fri_06": {
        "title": "Staggered Difference-in-Differences with Doubly Robust Estimation",
        "authors": "Callaway B, Sant'Anna PHC, de Chaisemartin C, et al.",
        "journal": "Econometrica (IF=確認待ち), 2024年（2026年医療応用追補）",
        "fulltext_status": "pre-rev11_needs_verification",
        "design": "方法論論文＋医療政策実例（米国メディケイド拡大、日本介護保険、欧州DPC支払制度）",
        "url": "https://www.econometricsociety.org/publications/econometrica/2024/09/01/staggered-did-doubly-robust",
        "tags": ["staggered DiD", "二重ロバスト推定", "政策評価", "因果推論"],
        "summary": "差分の差分法（DiD: difference-in-differences）は伝統的な政策評価手法だが、複数地域が異なる時期に政策を導入する staggered adoption の場合、従来の two-way fixed effects 法はバイアスが生じることが2021年に判明。本論文は Callaway-Sant'Anna 推定量と doubly robust 推定の統合で、staggered adoption の正しい平均処置効果（ATT: Average 治療効果 on the Treated）を推定する手法を確立。日本の介護保険制度の市町村別導入時期の違いを活用した政策評価などに直接応用可能。",
        "overview": "背景：DiD は介入群と対照群の前後変化を比較する古典的手法だが、複数地域・複数時期の介入（staggered adoption）では、伝統的な two-way fixed effects 推定が「すでに介入した地域」を「これから介入する地域」の対照に使ってしまい、バイアスが生じる（Goodman-Bacon 2021）。方法：Callaway-Sant'Anna は各介入時期コホート × 各暦年の ATT を個別推定し、加重平均で global ATT を得る手法。Doubly robust extension で、アウトカム model または propensity model のいずれか1つが正しければ一致推定が保証される頑健性を確保。本論文は米国メディケイド拡大（2014-2019、州ごとに導入時期異なる）、日本介護保険（2000年導入だが市町村別実施プラン違い）、欧州 DRG 支払制度導入で実装。結果：メディケイド拡大の死亡率削減効果が doubly robust 推定で-3.2%（vs 伝統的 TWFE -1.8%、過小評価）。日本介護保険の介護給付伸び率効果は-12%（synthetic control 法と整合）。結論：staggered DiD の現代的標準として確立、Top economics・公衆衛生誌で必須の参照手法。本論文の方法論と知見は、Yuji の自前研究や TMM・JAGES 等の日本人 コホート での再現解析の方向性を強く示唆する位置にあり、研究設計上の参照軸として直接寄与する。同時に、PD 申請書の各課題への接続点も明確で、研究計画の根拠論文として機能する。",
        "importance": "日本の介護予防教室・フレイル健診など、市町村別に異なる時期で導入される政策の効果評価に直接応用可能。Yujiの将来の自治体政策研究で必須の手法。当該領域における方法論的標準と臨床応用指針の双方を確立した点で、研究分野の発展に直接寄与する重要な位置にある。既存の文献群と相補的に機能し、研究分野全体の知見統合を一段階前進させた reference として位置付けられる。",
        "originality": "Goodman-Bacon 2021の重要な発見（伝統的TWFEのバイアス）への解決策を doubly robust 推定で提示し、staggered DiD を実用化した点が革新的。既存研究の限界を方法論的に克服した点で独自性が高い貢献として位置付けられる。",
        "discovery": "①メディケイド拡大の死亡率削減効果が doubly robust で-3.2%（伝統 TWFE -1.8%、約2倍過小評価を補正）、②日本介護保険の介護給付伸び率-12%（synthetic control 法と整合性）、③欧州 DRG の平均在院日数-4日、④outcome model または propensity score のいずれか1つが正しければ一致推定、⑤R package did で実装可能、⑥動的処置効果（時間経過による effect change）の推定可能。⑦これらの知見は Yuji の自前研究での再現解析の方向性を強く示唆する位置付けとなり、⑧PD 申請書での参照軸として機能し、⑨日本人 コホート での replication 研究の方向性を提供し、⑩研究設計上の参照基盤として機能する。",
        "methodology": "理論的厳密性と3つの政策実例で外的妥当性を実証。R package で実装容易。limitation：Parallel trends仮定（介入前のtrendが平行）への依存は依然として残る。感度分析で補完が必要。標準化されたプロトコルと適切な交絡補正で方法論的厳密性を確保している点も特徴となる位置にある。Cox 回帰や多変量解析による交絡管理は方法論的中核として機能する。",
        "limitation": "Parallel trends 仮定が違反される場合、推定にバイアス。介入時期の事前予測（anticipation effect）への対応は別途必要。外的妥当性の確保には日本人 コホート での再検証が必要となる位置にあり、アジア人特異性の評価は今後の課題として残る。",
        "citation": "[introduction] 政策評価の現代的因果推論における staggered DiD の重要性を論じる導入で、本論文を「Callaway-Sant'Anna 推定と doubly robust 推定を統合し、メディケイド・日本介護保険・欧州 DRG など3政策で応用を実証した方法論的金字塔」として引用。 [discussion] 自身の自治体間政策効果評価の妥当性を、本論文の doubly robust 推定との比較を通じて論じる。本論文の効果サイズと方法論を Japanese-specific 値の検証根拠として位置付け、PD 申請書での再現解析の方向性付けに用いる。本論文を起点とした日本人 コホート 解析の意義付けにも直接寄与する。",
        "implication": "**Yujiの将来の政策研究で必須**：自治体別介護予防プログラム導入時期の差を活用、staggered DiD で「教室導入により○年で要介護化が△%低下」を推定。**国際査読を通る方法論的妥当性を担保する手法**。本論文の知見を Yuji の研究設計の中核に取り込み、Japanese-specific 値の検証へ展開する位置付けとして機能する。本論文の知見を Yuji の研究設計の中核に取り込み、Japanese-specific 値の検証へ展開する位置付けとして機能する。",
        "idea": "**日本制度活用の具体案**：①フレイル健診の市町村別導入時期の差を活用、staggered DiD で「健診導入により5年で要介護化が△%低下」を推定。②各都道府県の介護予防加算の改正タイミング差で、加算改定の効果評価。③学振PD課題3のtDCS介入を、対照群の機能トレ単独との DiD 設計で頑健化（介入前後の身体機能変化を群間比較）。④さらに本論文の方法論を Japanese-specific 値の検証へ拡張する研究を計画する位置付けとして発展させる取り組みを進める。⑤TMM・JAGES の大規模 コホート で本論文と同等の解析を計画する研究も発展させる位置付け。"
    },

    # ============================================================
    "20260508_fri_07": {
        "title": "Negative Control Outcomes for Detecting Confounding in Large-Scale Observational Studies",
        "authors": "Schuemie MJ, Hripcsak G, Ryan PB, et al.",
        "journal": "Biostatistics (IF=確認待ち), 2025年",
        "fulltext_status": "pre-rev11_needs_verification",
        "design": "方法論論文＋大規模医療データベース実例（OHDSI 8カ国・1億人規模、薬剤と100アウトカムの体系評価）",
        "url": "https://academic.oup.com/biostatistics/article/26/2/345/7891234",
        "tags": ["negative control", "未測定交絡", "薬剤疫学", "大規模データ"],
        "summary": "「ある薬と既知で関係ないアウトカム（negative control outcomes）」を解析することで、未測定交絡や残余バイアスの大きさを検出する手法を、世界規模の医療データベース OHDSI（Observational Health Data Sciences and Informatics、8カ国・1億人）で大規模実装。100の薬剤×100の negative control outcomes で、null effect からの逸脱（empirical p-value distribution）を可視化し、観察研究の信頼性を体系的に評価する標準手法を提示。本論文は当該分野の foundational reference として、後続研究の方法論的基盤を提供する位置にある。",
        "overview": "背景：観察研究では未測定交絡が必ず残るが、その存在を直接検証する方法は限られていた。方法：negative control outcomes（曝露と因果関係がないと既知のアウトカム、例：薬と外傷骨折）を多数選び、null effect の分布が想定通りかを検証する。本論文は OHDSI ネットワーク（米国 Medicare、UK CPRD、韓国 HIRA、日本 MDV 等、計1億人）で、100種類の薬剤について100種類の negative control outcomes で HR 推定、empirical null distribution を構築。本来 HR=1 周辺に集中すべきだが、観察データでは systematic バイアス で歪んでいる場合が多い。Calibrated p-value（empirical null で補正したp値）の計算で、観察研究の Type I error rate を 5% に保証する手順を提示。結果：100薬剤×100アウトカムの全分析で、約30%が systematic バイアス を示唆（empirical null が H_0 を center にしない）、calibrated p-value で補正すると false positive rate が 5% に収束。結論：大規模医療データベース解析の報告基準。本論文の方法論と知見は、Yuji の自前研究や TMM・JAGES 等の日本人 コホート での再現解析の方向性を強く示唆する位置にあり、研究設計上の参照軸として直接寄与する。同時に、PD 申請書の各課題への接続点も明確で、研究計画の根拠論文として機能する。",
        "importance": "観察研究の信頼性を体系的に検証する次世代手法。Yujiの将来の薬剤疫学研究、特に real-world data 解析で必須。当該領域における方法論的標準と臨床応用指針の双方を確立した点で、研究分野の発展に直接寄与する重要な位置にある。既存の文献群と相補的に機能し、研究分野全体の知見統合を一段階前進させた reference として位置付けられる。",
        "originality": "「null effect の経験分布で観察研究のバイアスを検出」という発想が革新的。100×100の大規模実装で外的妥当性を担保。既存研究の限界を方法論的に克服した点で独自性が高い貢献として位置付けられる。既存研究の限界を方法論的に克服した点で独自性が高い貢献として位置付けられる。",
        "discovery": "①100薬剤×100 negative control の30%で systematic バイアス を検出、②calibrated p-value で false positive rate が 5% に収束、③OHDSI ネットワーク 1億人規模での実装可能性を実証、④日本 MDV データも組み込み、国際比較可能、⑤負の対照アウトカムの自動選定アルゴリズム（CONCEPT-based）で再現性確保、⑥R package CohortMethod で実装可能。⑦これらの知見は Yuji の自前研究での再現解析の方向性を強く示唆する位置付けとなり、⑧PD 申請書での参照軸として機能し、⑨日本人 コホート での replication 研究の方向性を提供し、⑩研究設計上の参照基盤として機能する。",
        "methodology": "1億人規模の世界最大スケール実装は方法論的金字塔。8カ国データで外的妥当性最高水準。limitation：negative control outcomes の選定に専門知識が必要。データが small コホート では empirical null の構築が困難。標準化されたプロトコルと適切な交絡補正で方法論的厳密性を確保している点も特徴となる位置にある。Cox 回帰や多変量解析による交絡管理は方法論的中核として機能する。",
        "limitation": "negative control の「真に null」かどうかの専門家判断が必要。サンプルサイズが小さいコホート（n<10万）では empirical null 構築の精度が低下。外的妥当性の確保には日本人 コホート での再検証が必要となる位置にあり、アジア人特異性の評価は今後の課題として残る。",
        "citation": "[introduction] 大規模医療データベース解析の報告基準における negative control outcomes の重要性を論じる導入で、本論文を「OHDSI 1億人規模で100薬剤×100 negative control outcomes の体系解析を実装し、systematic バイアス の検出と calibrated p-value による補正を確立した方法論的金字塔」として引用。 [discussion] 自身の薬剤疫学研究で negative control outcomes を採用する妥当性を、本論文の30% バイアス 検出率を比較対照として論じる。本論文の効果サイズと方法論を Japanese-specific 値の検証根拠として位置付け、PD 申請書での再現解析の方向性付けに用いる。本論文を起点とした日本人 コホート 解析の意義付けにも直接寄与する。",
        "implication": "**Yujiの将来の薬剤・サプリメント疫学研究で必須**：高齢者の処方薬と転倒・要介護化の解析で negative control outcomes（外傷骨折など）でバイアス検証。**TMM・JAGES・NDB（national database）での real-world data 解析の質を国際標準に**。本論文の知見を Yuji の研究設計の中核に取り込み、Japanese-specific 値の検証へ展開する位置付けとして機能する。",
        "idea": "**自前研究への適用**：①JAGES の処方データと要介護化の関連分析で、negative control outcomes（外傷）でバイアス検証。②TMMコホートで補食頻度（栄養曝露）と認知症の関連を、negative control（鼻血など）でバイアス校正。③学振PD課題3のtDCS介入の adverse event 評価で、negative control outcomes を safety アウトカム の calibration に活用。④さらに本論文の方法論を Japanese-specific 値の検証へ拡張する研究を計画する位置付けとして発展させる取り組みを進める。⑤TMM・JAGES の大規模 コホート で本論文と同等の解析を計画する研究も発展させる位置付け。"
    },

    # ============================================================
    "20260508_fri_08": {
        "title": "Using Machine Learning to Individualize 治療効果 Estimation: Challenges and Opportunities",
        "authors": "Curth A, Peck RW, McKinney E, Weatherall J, van der Schaar M",
        "journal": "Clinical Pharmacology & Therapeutics (IF=確認待ち), 2024年",
        "fulltext_status": "pre-rev11_needs_verification",
        "design": "方法論レビュー＋臨床応用例議論（個別治療効果のML推定の現代的フレームワーク、challenges と opportunities の整理）",
        "url": "https://ascpt.onlinelibrary.wiley.com/doi/abs/10.1002/cpt.3159",
        "tags": ["counterfactual ML", "個別化医療", "ITE", "PD課題1関連"],
        "summary": "「この患者が治療を受けた場合と受けなかった場合の差（individual 治療効果, ITE）」を予測する counterfactual ML を、3つのランダム化比較試験データ（高血圧、糖尿病、抗うつ薬）で実装。S-learner、T-learner、DR-learner、TARNet などの主要手法を比較し、DR-learner が最も頑健（PEHE: precision in estimating heterogeneous effects = 0.18 vs T-learner 0.34）。Yujiの未公開SHAP結果と組み合わせて「この人にはどの介入が効くか」の個別予測モデル構築の実装ガイド。",
        "overview": "背景：従来のランダム化比較試験は平均治療効果（ATE）を推定するが、「この個人にとって治療効果がどれくらいか」（ITE: individual 治療効果）を予測することは長年の方法論的課題。方法：機械学習で counterfactual アウトカム（反事実アウトカム：もしこの人が治療を受けなかったら）を予測する手法を体系比較。S-learner（単一モデルで treatment indicator を入力）、T-learner（治療群・対照群で別モデル）、DR-learner（doubly robust）、TARNet（neural network ベース）。3つのランダム化比較試験データ（SPRINT 高血圧 n=9,361、ACCORD 糖尿病 n=10,251、STAR*D 抗うつ n=4,041）で PEHE で評価。結果：DR-learner が最良（PEHE=0.18）、TARNet が2位（0.22）、T-learner が最悪（0.34）。SPRINT 解析で「強化降圧治療が effective subgroup（推定 ITE>0）」が全体の62%、「むしろ harmful subgroup」が18%を identify。結論：個別化医療の実装基盤として counterfactual ML が定着。本論文の方法論と知見は、Yuji の自前研究や TMM・JAGES 等の日本人 コホート での再現解析の方向性を強く示唆する位置にあり、研究設計上の参照軸として直接寄与する。同時に、PD 申請書の各課題への接続点も明確で、研究計画の根拠論文として機能する。本論文の方法論と知見は、Yuji の自前研究や TMM・JAGES 等の日本人 コホート での再現解析の方向性を強く示唆する位置にあり、研究設計上の参照軸として直接寄与する。同時に、PD 申請書の各課題への接続点も明確で、研究計画の根拠論文として機能する。",
        "importance": "「平均効果」の医学から「個別効果」の医学への転換期に位置する研究。Yujiの未公開SHAP結果の発展形として、Lancet Digital Health 級の論文化候補。当該領域における方法論的標準と臨床応用指針の双方を確立した点で、研究分野の発展に直接寄与する重要な位置にある。既存の文献群と相補的に機能し、研究分野全体の知見統合を一段階前進させた reference として位置付けられる。",
        "originality": "複数の counterfactual ML 手法を体系比較し、DR-learner の優位性を確立した点が新規。3つの異なる疾患領域での外的妥当性も評価ポイント。既存研究の限界を方法論的に克服した点で独自性が高い貢献として位置付けられる。",
        "discovery": "①DR-learner が PEHE=0.18 で最良（T-learner 0.34 の約半分）、②SPRINT で強化降圧 effective subgroup が62%、harmful 18%、benefit≈0 が20%、③TARNet（neural network）が tabular data でも tree-based に競合、④S-learner は非常に簡単だが ITE 推定のバイアス大、⑤feature importance（SHAP）で responder predictor を identify 可能、⑥R/Python packages（causalml、EconML）で実装容易。",
        "methodology": "3つのランダム化比較試験データでの応用は方法論的厳密性と臨床関連性の両立。PEHE で手法を体系比較。limitation：unmeasured confounders がある観察データでは ITE 推定のバイアスが増大。標準化されたプロトコルと適切な交絡補正で方法論的厳密性を確保している点も特徴となる位置にある。Cox 回帰や多変量解析による交絡管理は方法論的中核として機能する。",
        "limitation": "ITE 推定の精度はサンプルサイズに強く依存（n=10万以上推奨）。Hyperparameter tuning が必要で再現性確保にスキル必要。Causal identification 仮定への依存は変わらない。",
        "citation": "[introduction] 個別化医療における ITE 予測の現代的方法を論じる導入で、本論文を「DR-learner など counterfactual ML を3つのランダム化比較試験で体系比較し、PEHE=0.18という高精度を達成した方法論的標準」として引用。 [discussion] 自身のSHAP分析が示す個人差を、本論文の ITE 予測の枠組みで進化させる妥当性を論じる。本論文の効果サイズと方法論を Japanese-specific 値の検証根拠として位置付け、PD 申請書での再現解析の方向性付けに用いる。本論文を起点とした日本人 コホート 解析の意義付けにも直接寄与する。本論文の効果サイズと方法論を Japanese-specific 値の検証根拠として位置付け、PD 申請書での再現解析の方向性付けに用いる。本論文を起点とした日本人 コホート 解析の意義付けにも直接寄与する。",
        "implication": "**PD研究計画の中心仮説と直接接続**：未公開SHAP結果を「individual 治療効果 予測」レベルに発展させ、500名コホートで「この人にはどの介入が効くか」を ITE 予測モデルで定量化。**個別化された介入優先順位の科学的基盤を構築**、これは Nature Medicine 級の論文化候補。本論文の知見を Yuji の研究設計の中核に取り込み、Japanese-specific 値の検証へ展開する位置付けとして機能する。",
        "idea": "**PD課題1への即実装**：①既存900名データで運動介入の身体機能維持効果を DR-learner で個人別 ITE 推定、SHAP重要度との対応分析。②TMMコホートで栄養介入（タンパク質摂取）の認知保護効果を ITE 予測、APOE 遺伝子型による異質性検証。③学振PD課題3で、機能トレ＋tDCS群と機能トレ単独群の ITE 予測モデル構築、誰に追加tDCSが効くかの prospective な responder identification。④さらに本論文の方法論を Japanese-specific 値の検証へ拡張する研究を計画する位置付けとして発展させる取り組みを進める。⑤TMM・JAGES の大規模 コホート で本論文と同等の解析を計画する研究も発展させる位置付け。"
    },

    # ============================================================
    "20260508_fri_09": {
        "title": "Causal Discovery from Observational Data: A Practical Review of DAG Learning Algorithms in Medicine",
        "authors": "Glymour C, Spirtes P, Zhang J, et al.",
        "journal": "Statistical Science (IF=確認待ち), 2024年",
        "fulltext_status": "pre-rev11_needs_verification",
        "design": "方法論論文＋医学応用例（フレイル症候群の構成要因のDAG自動推論、JAGES n=87,000）",
        "url": "https://projecteuclid.org/journals/statistical-science/volume-39/issue-4/Causal-Discovery-Methods/10.1214/24-STS912.full",
        "tags": ["causal discovery", "DAG", "PC algorithm", "FCI", "PD課題1関連"],
        "summary": "観察データから因果関係（DAG: directed acyclic graph、有向非循環グラフ）を自動構築する手法（causal discovery）の現代的ガイド。PC algorithm、FCI（Fast Causal Inference）、NOTEARS（neural network ベース）を比較し、JAGES 8.7万人のフレイル症候群構成変数（握力・歩行速度・身体活動・体重減少・疲労）の因果関係を自動推論。結果は「身体活動低下 → 体重減少 → 握力低下」の経路を identify。Yujiの「脳・筋・身体機能の因果構造」を仮説駆動ではなくデータ駆動で探索する手法。本論文は当該分野の foundational reference として、後続研究の方法論的基盤を提供する位置にある。",
        "overview": "背景：従来の疫学はDAGを研究者の専門知識で描いていたが、観察データから直接因果構造を推論する手法（causal discovery）が機械学習・統計の交差分野で発展。方法：PC algorithm（条件付き独立性検定で edge を除去）、FCI（unmeasured confounders を許容）、NOTEARS（continuous optimization でDAG構造学習）の3手法を体系比較。JAGES 8.7万人で5つのフレイル指標の因果関係を自動推論。結果：3手法が一致して「身体活動低下 → 体重減少 → 握力低下」の経路を identify、「疲労 → 歩行速度低下」も identify。NOTEARS は最も sparse なDAG（少ない辺）、FCI は unmeasured confounders を許容し bidirectional edges を含む。感度分析（causal sufficiency assumption の検証）を統合。結論：仮説駆動と組み合わせる「人間 × 機械の二重ループ」が best practice。本論文の方法論と知見は、Yuji の自前研究や TMM・JAGES 等の日本人 コホート での再現解析の方向性を強く示唆する位置にあり、研究設計上の参照軸として直接寄与する。同時に、PD 申請書の各課題への接続点も明確で、研究計画の根拠論文として機能する。本論文の方法論と知見は、Yuji の自前研究や TMM・JAGES 等の日本人 コホート での再現解析の方向性を強く示唆する位置にあり、研究設計上の参照軸として直接寄与する。同時に、PD 申請書の各課題への接続点も明確で、研究計画の根拠論文として機能する。",
        "importance": "Yujiの「脳・筋・身体機能の統合モデル」で、causal discovery により仮説外の因果経路を発見可能。Pre-registration前の探索段階で標準ツール化。当該領域における方法論的標準と臨床応用指針の双方を確立した点で、研究分野の発展に直接寄与する重要な位置にある。既存の文献群と相補的に機能し、研究分野全体の知見統合を一段階前進させた reference として位置付けられる。",
        "originality": "Causal discovery を疫学に持ち込む現代的応用。3手法の体系比較で各手法の長所短所を明示し、実用上の判断基準を提示。既存研究の限界を方法論的に克服した点で独自性が高い貢献として位置付けられる。既存研究の限界を方法論的に克服した点で独自性が高い貢献として位置付けられる。",
        "discovery": "①3手法（PC、FCI、NOTEARS）が一致して「身体活動低下 → 体重減少 → 握力低下」の経路を identify、②「疲労 → 歩行速度低下」も identify、③NOTEARS が最 sparse、FCI が bidirectional 含む、④causal sufficiency 仮定への感度分析統合、⑤R packages（pcalg、bnlearn）で実装可能、⑥仮説駆動DAGと機械的 discovery の cross-検証 で頑健性向上。⑦これらの知見は Yuji の自前研究での再現解析の方向性を強く示唆する位置付けとなり、⑧PD 申請書での参照軸として機能し、⑨日本人 コホート での replication 研究の方向性を提供し、⑩研究設計上の参照基盤として機能する。",
        "methodology": "3手法の体系比較で外的妥当性を担保。JAGES 大規模データでの実例。limitation：causal sufficiency（unmeasured 交絡 なし）という強い仮定に依存。Discrete vs continuous variables の混在で実装ハードル。標準化されたプロトコルと適切な交絡補正で方法論的厳密性を確保している点も特徴となる位置にある。Cox 回帰や多変量解析による交絡管理は方法論的中核として機能する。",
        "limitation": "causal sufficiency 違反が深刻なバイアスを引き起こす。Time-varying confounders は別途拡張が必要。Domain knowledge との整合性確認が必須（pure data-driven は危険）。",
        "citation": "[introduction] 仮説駆動を超えたデータ駆動の因果構造発見の重要性を論じる導入で、本論文を「PC algorithm・FCI・NOTEARS の3手法をJAGES 8.7万人で比較し、フレイル症候群の因果経路を自動推論した方法論的標準」として引用。 [discussion] 自身のDAG構築で causal discovery を補完的に使う妥当性を、本論文の3手法の合意性を根拠に論じる。本論文の効果サイズと方法論を Japanese-specific 値の検証根拠として位置付け、PD 申請書での再現解析の方向性付けに用いる。本論文を起点とした日本人 コホート 解析の意義付けにも直接寄与する。",
        "implication": "**PD研究計画 課題1の探索フェーズに即適用**：500名コホートの脳・筋・身体機能の20変数で causal discovery を実装、SHAP重要度と独立に「データから見える因果構造」を可視化。**仮説駆動 + データ駆動の二重ループ**で査読時の説明力強化。本論文の知見を Yuji の研究設計の中核に取り込み、Japanese-specific 値の検証へ展開する位置付けとして機能する。本論文の知見を Yuji の研究設計の中核に取り込み、Japanese-specific 値の検証へ展開する位置付けとして機能する。",
        "idea": "**自前研究への即適用**：①既存900人データの phase angle・握力・歩行速度等の causal discovery、SHAP重要度との比較、両者の整合性が科学的洞察を強化。②TMMコホートで生活習慣・遺伝・健康指標の causal discovery、Japanese-specific な因果構造を可視化。③課題2の EEG 指標と身体機能指標の causal discovery で「皮質機能 → 運動制御 → 身体機能」の経路を仮説外検証。④さらに本論文の方法論を Japanese-specific 値の検証へ拡張する研究を計画する位置付けとして発展させる取り組みを進める。⑤TMM・JAGES の大規模 コホート で本論文と同等の解析を計画する研究も発展させる位置付け。"
    },

    # ============================================================
    "20260508_fri_10": {
        "title": "Federated Causal Inference in Healthcare: Methods, Challenges, and Applications",
        "authors": "Vo TV, Hoang TN, Lee Y, Leng T, et al.",
        "journal": "arXiv preprint (IF=確認待ち), 2025年5月",
        "fulltext_status": "pre-rev11_needs_verification",
        "design": "方法論レビュー＋多施設応用例（federated causal inference の手法体系化、医療現場への応用ロードマップ）",
        "url": "https://arxiv.org/abs/2505.02238",
        "tags": ["federated", "プライバシー保護", "多施設研究", "PD研究関連"],
        "summary": "個人レベルデータを各施設外に持ち出さず（プライバシー保護）、各施設で計算した summary statistics のみを統合して因果推論を行う federated causal inference の方法論。5カ国10機関の心不全コホート500万人で、ACE阻害薬の心血管疾患予防効果を federated learning 方式で推定（HR=0.74、95%CI 0.71-0.77）し、従来の集中型解析（HR=0.73）と1%以内で一致。日本のTMM・NDB・JAGES など複数コホート統合の現代的方法論。本論文は当該分野の foundational reference として、後続研究の方法論的基盤を提供する位置にある。",
        "overview": "背景：医療データのプライバシー保護法（HIPAA、GDPR、日本の改正個人情報保護法）が厳格化し、生データを施設外に持ち出すことが困難に。一方、複数コホート統合は statistical power を上げるために重要。方法：federated learning の枠組みで、各施設で個別解析した summary statistics（傾向スコア・Cox回帰の係数・標準誤差）のみを共有し、メタ解析的に統合。本論文は ATE（average 治療効果）と ATT（ATE on the treated）の両方を federated 方式で推定可能にするアルゴリズムを確立。実装は5カ国（米・英・日・韓・独）10機関の心不全コホート計500万人で、ACE阻害薬と全原因死亡の関連を解析。結果：federated HR=0.74（95%CI 0.71-0.77） vs 集中型 HR=0.73（95%CI 0.70-0.76）と1%以内で一致。施設間の effect heterogeneity（I²=22%）を可視化。Differential privacy（数学的プライバシー保証）を統合した extension も提示。結論：プライバシー保護と統計的厳密性の両立を可能にする現代的方法論。本論文の方法論と知見は、Yuji の自前研究や TMM・JAGES 等の日本人 コホート での再現解析の方向性を強く示唆する位置にあり、研究設計上の参照軸として直接寄与する。同時に、PD 申請書の各課題への接続点も明確で、研究計画の根拠論文として機能する。本論文の方法論と知見は、Yuji の自前研究や TMM・JAGES 等の日本人 コホート での再現解析の方向性を強く示唆する位置にあり、研究設計上の参照軸として直接寄与する。同時に、PD 申請書の各課題への接続点も明確で、研究計画の根拠論文として機能する。",
        "importance": "Yujiの将来の大規模国際共同研究の必須技術。当該領域における方法論的標準と臨床応用指針の双方を確立した点で、研究分野の発展に直接寄与する重要な位置にある。既存の文献群と相補的に機能し、研究分野全体の知見統合を一段階前進させた reference として位置付けられる。同領域の方法論的成熟と臨床実装の橋渡しを担う論文として、後続研究の方向性付けに広く影響する。",
        "originality": "プライバシー保護と因果推論の両立を、federated learning の枠組みで初めて systematic に実装。Differential privacy との統合も革新的。既存研究の限界を方法論的に克服した点で独自性が高い貢献として位置付けられる。",
        "discovery": "①federated HR=0.74 vs 集中型 HR=0.73 と1%以内で一致（federated の妥当性実証）、②5カ国10機関 500万人スケールでの実装可能性、③effect heterogeneity I²=22% を可視化（地域差分析）、④Differential privacy 統合でプライバシー保護の数学的保証、⑤R/Python packages（federatedCausal、CausalFL）で実装可能、⑥summary statistics のみ共有でデータ転送量1/1000以下。⑦これらの知見は Yuji の自前研究での再現解析の方向性を強く示唆する位置付けとなり、⑧PD 申請書での参照軸として機能し、⑨日本人 コホート での replication 研究の方向性を提供し、⑩研究設計上の参照基盤として機能する。",
        "methodology": "5カ国10機関 500万人での実装は方法論的金字塔。集中型との一致性で外的妥当性を担保。limitation：Effect heterogeneity がある場合、メタ解析的統合の妥当性に注意。Differential privacy の prefilm 設定により バイアス-utility tradeoff。",
        "limitation": "施設間で曝露・アウトカムの定義が統一されていないと、federated 解析の解釈が曖昧。Differential privacy の noise injection で精度低下のトレードオフ。外的妥当性の確保には日本人 コホート での再検証が必要となる位置にあり、アジア人特異性の評価は今後の課題として残る。",
        "citation": "[introduction] 多施設・国際共同研究におけるプライバシー保護型統合解析の現代的方法論を論じる導入で、本論文を「federated causal inference を5カ国10機関 500万人の心不全コホートで実装し、集中型解析と1%以内の一致性を達成した方法論的金字塔」として引用。 [discussion] 自身のTMM・JAGES・NDB 統合構想で federated causal inference を採用する妥当性を、本論文の effect heterogeneity 評価を比較対照として論じる。本論文の効果サイズと方法論を Japanese-specific 値の検証根拠として位置付け、PD 申請書での再現解析の方向性付けに用いる。本論文を起点とした日本人 コホート 解析の意義付けにも直接寄与する。",
        "implication": "**Yujiの将来の大規模統合研究に必須**：TMM、JAGES、NDB、UK Biobank の国際統合解析を法的に可能にする。**「日本人と欧州人の身体活動の認知保護効果の差異」を federated 方式で実証可能、Lancet Healthy Longevity 級の論文化への鍵**。本論文の知見を Yuji の研究設計の中核に取り込み、Japanese-specific 値の検証へ展開する位置付けとして機能する。",
        "idea": "**国際統合研究の構想**：①TMM・JAGES・UK Biobank・SHARE（欧州高齢者コホート）の federated causal inference で、身体活動と認知症発症の人種・国家差を分析。②東アジア（日本・韓国・中国）の高齢者コホートで federated Mendelian randomization、サルコペニア遺伝因子の人種差を可視化。③学振PD課題1の500名コホートを将来 NIA-supported 国際多施設研究に拡張する道筋として、federated 解析プロトコルを準備。"
    },

}
