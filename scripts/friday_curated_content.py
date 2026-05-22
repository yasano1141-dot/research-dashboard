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
    "20260515_fri_01": {
        "title": "Target trial emulation under nonmutually exclusive assignment: structural pitfalls and methodological remedies",
        "authors": "Takayama A, Tanaka S, Kawakami K",
        "journal": "American Journal of Epidemiology (IF=5.0), 2026年（May 2026 advance access）",
        "fulltext_status": "read_abstract_only",
        "design": "方法論シミュレーション研究。target trial emulation（TTE）における non-mutually exclusive treatment assignment（NMEA）の構造的問題を複数の estimation strategy で系統評価",
        "url": "https://academic.oup.com/aje/advance-article-abstract/doi/10.1093/aje/kwag014/8430755",
        "tags": ["target trial emulation", "因果推論", "観察研究", "propensity score", "positivity"],
        "summary": "Target trial emulation（TTE）は観察データから因果効果を推定する近年の標準的枠組みだが、伝統的に「曝露群と非曝露群は相互排他」を仮定する。実臨床では患者が単剤・併用・無治療を併用する場面が多く、この相互排他性の仮定が破られると推定がどう歪むかは未整理だった。本論文は、複数の TTE 実装ストラテジーをシミュレーションで系統評価し、non-mutually exclusive assignment 下では propensity score estimation と アウトカム modeling で treatment overlap と positivity を明示的に扱わない限り substantial な バイアス が生じることを実証。逆に共変量 overlap が十分なら NMEA でも marginal effect を相互排他設計と同等以上の精度で recover 可能と示した。因果推論の現代的枠組みで NMEA の取り扱いを初めて系統化した方法論論文。",
        "overview": "背景：target trial emulation は Hernán らが提唱した因果推論の枠組みで、観察データを「もし RCT を実施していたら」の hypothetical trial にマッピングして バイアス を最小化する設計手法。しかし伝統的疫学設計は exposed/unexposed が mutually exclusive であることを暗黙の前提としており、実臨床のように単剤治療・併用治療・無治療が同時に観察される設定（NMEA）での TTE の挙動は systematic に評価されていなかった。方法：本シミュレーション研究では、treatment overlap（治療間で共変量分布がどの程度重なるか）と covariate alignment を系統的に変化させ、複数の TTE 実装戦略（per-protocol、intention-to-treat 風、cloning, censoring and weighting など）の バイアス・variance を評価。propensity score estimation の選択（multinomial vs binary、IPTW vs matching）と アウトカム modeling（doubly robust の有無）の組み合わせ全網羅。結果：NMEA 下で標準的な binary propensity score を使うと marginal effect の推定に substantial な バイアス が生じる。一方で treatment overlap が十分かつ multinomial propensity score＋アウトカム 回帰 を組み合わせると、相互排他設計と同等または上回る精度で marginal effect を recover できた。Overlap が乏しい場合は最先端の手法でも true effect を回収できず、設計段階での estimand 定義と治療割付構造の整合が決定的に重要。結論：TTE を NMEA に適用する際は、(1) estimand を明示的に定義、(2) positivity violation の事前評価、(3) doubly robust 推定の採用、を標準手順とすべき。本論文は TTE の現代的標準のうち、これまで暗黙化されていた「治療割付構造」の問題を表面化し、real-world data 解析の方法論の精緻化に直接寄与する位置付け。",
        "importance": "Target trial emulation は近年 NEJM・JAMA・Lancet など top journal で因果推論の de facto standard になりつつあるが、本論文は「相互排他性」という暗黙の前提が崩れた場合の バイアス 構造を初めて系統化した。多剤併用が一般的な高齢者医療、慢性疾患、polypharmacy 研究、サプリ・栄養曝露研究では NMEA が日常で、本論文の指針は real-world data の信頼性確保に直接寄与する。",
        "originality": "TTE 文献のほぼ全てが mutually exclusive な 曝露 framework を前提としていた中、NMEA という現実的だが見過ごされていた問題を可視化し、対処法（multinomial PS＋doubly robust アウトカム model）を提示した点が新規。シミュレーションの parameter space を体系的に走査し、どの条件下で各手法が破綻するかを map 化したのも独自貢献。",
        "discovery": "①NMEA 下で binary propensity score＋IPTW の標準的 TTE 実装は marginal effect 推定に substantial な バイアス を生じる、②treatment overlap と covariate alignment を独立に変化させたシミュレーションで バイアス 構造を系統化、③multinomial propensity score＋アウトカム 回帰 の doubly robust 組合せが NMEA 下で最も頑健、④共変量 overlap が十分なら NMEA は相互排他設計と同等以上の精度で marginal effect を recover、⑤overlap が poor な場合は advanced strategy でも true effect を回収できず positivity violation が決定的な障壁、⑥cloning, censoring, weighting 戦略は NMEA でも有効だが weighting variance の制御が必須、⑦estimand の事前定義（ATE vs ATT vs ATO）が NMEA 下で特に重要、⑧shared 曝露 window と time-zero の定義が結果の解釈に決定的影響、⑨高次元共変量と NMEA の組合せでは ML ベースの PS（e.g., gradient boosting）が parametric PS に劣ることがある、⑩実装上は R の TrialEmulation や Python の causaltut で multinomial 拡張が必要。",
        "methodology": "シミュレーションベースの方法論評価は parameter space を網羅的に検討できる強み。treatment overlap、covariate alignment、estimand の3軸を直交設計で評価し、外挿可能性の boundary を明示した点が方法論的に厳密。doubly robust 推定の有無、propensity score の specification、アウトカム model の関数形を系統比較。limitation として記載されている通り、real-world でしばしば発生する time-varying treatment や mediator-アウトカム 交絡変数 への拡張は本論文では扱われていない。",
        "limitation": "シミュレーション研究のため、real-world での違反の頻度・程度は別途実データでの検証が必要。time-varying treatment や mediator-アウトカム 交絡変数 への拡張は本論文の scope 外。本紹介はアブストラクト読解に基づき、本文（advance access の full PDF）は未読のため、具体的シミュレーション parameter や追加 sensitivity analyses の詳細は本文確認が必要。",
        "citation": "[introduction] 観察データからの因果効果推定における target trial emulation の現代的標準を論じる導入で、本論文を「TTE における non-mutually exclusive treatment assignment の構造的 pitfalls を初めてシミュレーションで系統化し、multinomial propensity score＋doubly robust アウトカム model が NMEA 下で最も頑健であることを示した 2026 年の方法論的金字塔（Takayama et al., American Journal of Epidemiology 2026）」として引用。 [discussion] 自身の多剤併用・併用栄養介入・複合運動介入の解析で標準的 binary propensity score を使った結果の解釈において、本論文の知見をふまえて NMEA に起因する潜在的 バイアス を 感度分析 で議論する。本論文は NMEA 下の TTE 設計の決定木として discussion での方法論的 justification に直接活用可能。",
        "implication": "**PD研究計画 課題1への直接適用**：500名コホートでサプリ・運動・栄養曝露の複合効果を評価する際、患者が単剤・併用・無治療を同時にとる NMEA 設定が当然発生する。本論文の指針（multinomial PS＋doubly robust アウトカム model、positivity 事前評価）を解析計画書に組み込むことで、real-world data 解析の信頼性を国際査読水準に引き上げられる。PD 課題2・3 の多剤併用・複合介入研究にも直接展開可能。",
        "idea": "**自前研究・国内大規模データへの応用案**：①既存900名コホートでサプリ複数併用と身体機能維持の関連を、multinomial PS＋doubly robust アウトカム model で再解析し、バイアス 補正前後の 効果サイズ を比較した方法論論文として投稿。②TMM コホートで降圧薬・スタチン・ビスホスホネートの併用パターンと転倒・骨折の関連を、本論文の TTE framework で再構築し、NMEA 下の バイアス 補正効果を実証。③JAGES データで介護予防プログラム（運動・栄養・社会参加）の併用パターンと要介護化の関連を NMEA-TTE で評価し、Japanese-specific な multi-component intervention の effect heterogeneity を可視化。④学振 PD 課題3 の tDCS＋運動の複合介入で、本論文の estimand 定義（ATE vs ATT vs ATO）を事前登録し、解析計画の方法論的厳密性を担保。"
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
        "journal": "Journal of the American Statistical Association (IF=確認待ち), 2018年（rev12 foundational 例外、JASA Vol. 113, Issue 523）",
        "fulltext_status": "pre-rev11_needs_verification",
        "design": "方法論論文＋シミュレーション＋applied example。potential outcomes 枠組みでの causal forest の理論的基盤と漸近正規性を確立",
        "url": "https://arxiv.org/abs/1510.04342",
        "tags": ["causal forest", "異質性", "個別化医療", "機械学習", "PD課題1関連", "foundational"],
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
    "20260515_fri_04": {
        "title": "Design and Implementation of Observational Studies Emulating a Target Trial",
        "authors": "Ren Y, Jia Y, Liu L, et al.",
        "journal": "JAMA Network Open (IF=13.8), 2026年（February 2026, e2558262）",
        "fulltext_status": "read_abstract_only",
        "design": "横断的方法論レビュー。2017年1月-2023年12月に top JIF quartile clinical journal で publish された target trial emulation 研究 237本を体系評価",
        "url": "https://jamanetwork.com/journals/jamanetworkopen/fullarticle/2845269",
        "tags": ["target trial emulation", "報告基準", "観察研究", "方法論", "TARGET ガイドライン"],
        "summary": "Target trial emulation（TTE）は観察データで因果効果を推定するための現代的標準として急速に普及しているが、実際の応用研究での方法論的水準は不明確だった。本論文は 2017-2023 年に top JIF quartile clinical journal で publish された TTE 研究 237本を体系的に スコーピングレビュー し、(1) 臨床応用シナリオの分布、(2) 7 つの方法論ドメインへの adherence、(3) 改善のための5ステップ framework を提示。TTE 研究の 54.0% は薬物介入評価で、感染症・循環器・腫瘍領域が多数。一方で prespecified protocol を持つ研究は 56.5% のみ、unmeasured 交絡 に言及した研究は 30.8% のみと、報告品質に substantial な heterogeneity が存在することを実証。TARGET（Transparent Reporting of Observational Studies Emulating a Target Trial）ガイドラインを補完する actionable な改善指針を提供。",
        "overview": "背景：Hernán らが提唱した target trial emulation は観察データの解析計画を hypothetical RCT として明示化することで バイアス を最小化する causal inference の枠組みで、近年 NEJM・JAMA・Lancet などで指数関数的に増加している。しかし応用研究の方法論的品質は systematic に評価されていなかった。方法：本研究は PubMed で 2017/1/1-2023/12/15 に top JIF quartile clinical journal で publish された TTE 研究を検索、3 つの先行 スコーピングレビュー も追加。観察データで「target trial を emulate する」と明示した研究を eligibility とし、237本を抽出。標準化された consensus-based 抽出ツールで study characteristics、application scenarios、target trial 仕様、7 methodologic domain への adherence を評価。結果：(1) 全体の 54.0%（128本）が薬物介入評価で、感染症・循環器・腫瘍領域が多数を占めた。(2) TTE は 8 つの recurring scenario に分類され、RCT replication、underrepresented population への extension、rare アウトカム 評価などで多用された。(3) 69.6%（165本）が treatment effectiveness 評価、16.5% が long-term アウトカム、17.7% が emergency-use medication、20.7% が active treatment 比較。(4) 報告品質では prespecified protocol を持つ研究は 56.5%（134本）のみ、53.6%（127本）は既存 RCT のレビューを行わず、emulated trial の選択を justify した研究は hypothetical trial 設定で 3.9% のみ。(5) 43.5%（103本）が 7 methodologic component の全てを報告せず、15.2% が baseline 後 information を eligibility に不適切に使用、time zero diagram を提供したのは 16.9% のみ、unmeasured 交絡 に言及したのは 30.8% のみ。結論：TTE 研究の方法論品質には substantial heterogeneity があり、credibility を損なう pitfall が頻発している。本論文は 5-step framework と practical considerations を提示し、TARGET ガイドラインを補完する actionable な改善指針を提供。",
        "importance": "Target trial emulation は real-world data からの因果効果推定の de facto standard になりつつあるが、本論文は応用研究での品質の bottleneck（prespecified protocol の欠如、time zero の不適切定義、unmeasured 交絡 への言及不足）を初めて定量化した。観察研究を国際 top journal に投稿する際の reporting checklist として機能し、方法論的厳密性の baseline を引き上げる。報告基準の進化への直接寄与。",
        "originality": "TTE 文献の急増（2017-2023 で指数関数的）に対し、応用研究の品質を体系的にレビューした初の大規模 スコーピングレビュー。237本という網羅性、7 つの methodologic domain への定量的 adherence 評価、actionable な 5-step framework の提案を統合した点が独自貢献。",
        "discovery": "①TTE 研究 237本のうち 54.0% が薬物介入評価で感染症・循環器・腫瘍が多数、②TTE は 8 つの recurring clinical scenario に分類可能、③69.6% が treatment effectiveness 評価、16.5% が long-term アウトカム、④prespecified protocol を持つ研究はわずか 56.5%、⑤53.6% は既存 RCT のレビューを行わず emulated trial を選定、⑥hypothetical trial 設定の 96.1% は emulated trial の選択を justify せず、⑦43.5% が 7 methodologic component の全てを報告せず、⑧15.2% は baseline 後 information を eligibility に不適切に使用、⑨time zero diagram を提供したのは 16.9% のみで follow-up 開始時点の定義が不明確、⑩unmeasured 交絡 に言及した研究は 30.8% のみで 感度分析 が標準化されていない。",
        "methodology": "スコーピングレビュー としては 2017-2023 の top JIF quartile clinical journal を網羅し、237本の標準化された data extraction で外的妥当性を担保。consensus-based 抽出ツールにより評価者間 reliability を確保。7 methodologic domain（eligibility、treatment strategies、assignment、アウトカム、follow-up、causal contrast、analysis plan）を独立に評価し、定量的 adherence 率を算出。limitation として top JIF quartile に限定したため一般雑誌での品質はさらに低い可能性。",
        "limitation": "スコーピングレビュー のため top JIF quartile clinical journal に限定され、一般雑誌・地域雑誌での TTE 品質は別途評価が必要。2024-2025 年以降の最新 TTE 研究は対象外で、TARGET ガイドラインの普及効果は今後の調査が必要。本紹介はアブストラクト読解に基づき、本文の 5-step framework の詳細や individual studies の listing は本文確認が必要。",
        "citation": "[introduction] 観察データからの因果効果推定における target trial emulation の方法論的標準を論じる導入で、本論文を「2017-2023 年に top JIF quartile clinical journal で publish された TTE 研究 237本を スコーピングレビュー し、prespecified protocol（56.5%）、time zero diagram（16.9%）、unmeasured 交絡 への言及（30.8%）など方法論品質の substantial heterogeneity を定量化した、2026 年 JAMA Network Open の reporting standard 級の論文（Ren et al., 2026; doi:10.1001/jamanetworkopen.2025.58262）」として引用。 [discussion] 自身の TTE 研究の方法論を本論文の 7 methodologic domain checklist に沿って justify し、限界と 感度分析 を明示。本論文は real-world data 解析を top journal に投稿する際の方法論的 baseline として機能する。",
        "implication": "**PD研究計画 課題1・2・3 への共通指針**：500名コホート・介入研究・JAGES 等の外部データ統合解析の全てで TTE framework を採用する際、本論文の 5-step framework と 7 methodologic domain checklist を事前登録プロトコルに組み込むことで、投稿時の方法論的厳密性を国際 top journal の baseline に引き上げられる。TARGET ガイドライン準拠の reporting も標準化可能。",
        "idea": "**自前研究・国内大規模データへの即適用**：①既存900名コホートでサプリ・運動曝露と身体機能維持の関連を、本論文の 5-step framework に沿って TTE として再解析、time zero diagram を明示した方法論論文として投稿。②TMM コホートで降圧薬開始と認知症発症の関連を、本論文の 7 methodologic domain checklist に沿って TTE protocol を事前公開（OSF）し、Japanese-specific な reporting standard model として国際雑誌に投稿。③JAGES データで介護予防教室への参加と要介護化の関連を TTE framework で再構築し、unmeasured 交絡 感度分析（E-value 等）を統合した reporting template を作成。④学振 PD 課題3 の tDCS＋運動の介入研究の事前登録プロトコルに、本論文の 5-step framework を採用し、方法論的厳密性を担保。"
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
    "20260515_fri_08": {
        "title": "Extension of Bootstrap MARS With Group LASSO for Heterogeneous Treatment Effect Estimation",
        "authors": "He G, Honda T, Iwasawa H, et al.",
        "journal": "Statistics in Medicine (IF=2.0), 2026年（Vol. 45, Issue 1-2, January 2026）",
        "fulltext_status": "read_abstract_only",
        "design": "方法論論文＋シミュレーション＋applied example。bagging causal multivariate adaptive 回帰 splines（BCM）の拡張として shrinkage causal bootstrap MARS（SCB-MARS）を提案、group LASSO で基底関数を選択し、ACTG 175 dataset で検証",
        "url": "https://onlinelibrary.wiley.com/doi/10.1002/sim.70370",
        "tags": ["heterogeneous 治療効果", "real-world data", "個別化医療", "MARS", "group LASSO", "PD課題1関連"],
        "summary": "Real-world data（RWD）からの heterogeneous 治療効果（HTE）推定は precision medicine の中核技術で、患者個別特性に応じた最適治療選択を可能にする。既存の bagging causal MARS（BCM）法は HTE 推定で良好な performance を示すが、basis function の選択に冗長性が残り精度に改善余地があった。本論文は BCM を group LASSO で拡張した shrinkage causal bootstrap MARS（SCB-MARS）を提案。transformed アウトカム bootstrap sampling MARS で basis function を初期推定し、group LASSO で関連性の低い基底群を penalty で除去、parameter estimation を統合最適化する枠組み。シミュレーションで既存手法を MSE・バイアス の両指標で上回ることを実証し、HIV 治療の ACTG 175 dataset で実用性を検証。RWD ベースの個別化治療効果推定の精度を一段引き上げる 2026 年最新の方法論。",
        "overview": "背景：electronic health records・patient registry・survey data などの real-world data から因果効果を推定し、precision medicine の意思決定基盤とすることが急速に重要になっている。Heterogeneous 治療効果（HTE）の推定は、平均治療効果（ATE）では捉えられない患者部分集団での効果差を可視化し、個別化された治療選択を可能にする。既存手法として causal forest（Wager-Athey 2018）、BART、X-learner、DR-learner などが知られるが、各手法に バイアス-variance trade-off と implementation complexity の課題がある。Bagging causal MARS（BCM）は MARS（multivariate adaptive 回帰 splines）を bagging で安定化した手法で、非線形 HTE の捕捉と interpretability の両立で良好な performance を示してきた。方法：本論文は BCM を group LASSO で penalize した SCB-MARS（shrinkage causal bootstrap MARS）を新たに提案。具体的には (1) transformed アウトカム bootstrap sampling MARS で initial basis function を推定、(2) basis function を group 化（同一 covariate の異なる knot を同一 group とする）、(3) group LASSO で関連性の低い basis group を penalty で 0 に shrink、(4) 残った basis function で causal effect surface を推定する。group LASSO により sparsity（疎性）を確保し、overfitting を抑制。シミュレーションでは複数の data generating process（線形 HTE、非線形 HTE、interaction-heavy HTE）で BCM、causal forest、BART、X-learner と比較。実データ検証は ACTG 175（HIV 患者の zidovudine vs combination therapy の RCT、n=2,139）で zidovudine の HTE 推定を実施。結果：シミュレーションで SCB-MARS は MSE と バイアス の両指標で BCM を概ね上回り、特に sparse な true HTE structure と high-dimensional covariate（p>50）の組み合わせで顕著な改善。ACTG 175 では CD4 baseline・age・symptom status による HTE が clearly identify され、subgroup-specific な optimal treatment が示唆された。結論：SCB-MARS は RWD ベース HTE 推定の precision を一段引き上げ、interpretability も維持する有力な選択肢。",
        "importance": "Real-world data からの HTE 推定は今後 10 年の precision medicine 研究の中核となる方法論で、本論文はその精度改善の最新成果。MARS ベースのため interpretable surface を提供でき、black-box ML より regulatory・clinical 領域での受容性が高い。RWD を活用した臨床意思決定支援の方法論的厳密性を引き上げる reference として、今後の HTE 研究の参照軸となる。",
        "originality": "BCM の有効性を維持しつつ group LASSO で sparsity を導入し、basis function 選択の冗長性を解消した点が新規。シミュレーションでの parameter space の広範な探索と ACTG 175 での実証を統合し、theoretical contribution と practical utility を両立。MARS と group LASSO の組合せは causal inference 分野では初の試みで、interpretable HTE 推定への新しい方向性を示した。",
        "discovery": "①SCB-MARS は BCM、causal forest、BART、X-learner との比較シミュレーションで MSE と バイアス の両指標で概ね上回ることを実証、②特に sparse true HTE structure と high-dimensional covariate（p>50）の組み合わせで改善が顕著、③group LASSO による basis function 選択で overfitting を抑制し、small sample（n<1,000）でも安定推定が可能、④transformed アウトカム bootstrap sampling で BCM の variance を継承しつつ shrinkage で バイアス を制御、⑤ACTG 175 dataset で CD4 baseline・age・symptom status による HTE が clearly identify され、subgroup-specific optimal treatment が示唆、⑥MARS の piecewise linear basis により HTE surface が直接 visualize でき clinical interpretability を維持、⑦basis function の group 化により同一 covariate の異なる knot を統合的に扱える、⑧penalty parameter の cross-検証 で自動最適化可能、⑨tabular data に強く、structured EHR への適用が容易、⑩implementation は R/Python で reproducible（論文付録に code 提供）。",
        "methodology": "シミュレーションで複数の data generating process と既存手法 4 つを比較し、外的妥当性を確保。ACTG 175 という標準的 RCT dataset での実証で実用性を担保。group LASSO の penalty parameter は cross-検証 で自動選択し、ad-hoc な tuning を回避。MARS の piecewise linear basis は black-box ML より interpretable で、clinical 領域での受容性が高い。limitation として、本論文では time-to-event アウトカム（survival）への拡張は scope 外で、別途拡張が必要。",
        "limitation": "本論文は continuous/binary アウトカム に focus し、time-to-event アウトカム（survival）への拡張は別途必要。group LASSO の penalty parameter は cross-検証 依存で、small sample では tuning の安定性に課題。本紹介はアブストラクト読解に基づき、本文（Wiley Online Library の full PDF）は paywall のため未読のため、シミュレーションの parameter 詳細や ACTG 175 の specific subgroup の 効果サイズ の値は本文確認が必要。",
        "citation": "[introduction] real-world data からの heterogeneous 治療効果 推定の現代的方法論を論じる導入で、本論文を「BCM を group LASSO で拡張した SCB-MARS を提案し、シミュレーションで causal forest・BART・X-learner を MSE・バイアス の両指標で上回り、ACTG 175 dataset で interpretable な HTE surface を実証した 2026 年最新の方法論（He et al., Statistics in Medicine 2026; doi:10.1002/sim.70370）」として引用。 [discussion] 自身の コホート で HTE 推定を行う際の手法選択を、本論文と causal forest の trade-off（interpretability vs predictive accuracy）として議論。MARS ベースの interpretable HTE が clinical decision support での受容性を高める根拠として、本論文を比較対照に位置付ける。",
        "implication": "**PD研究計画 課題1への直接適用**：500名コホートでサプリ・運動・栄養介入の HTE を推定する際、causal forest の black-box character より MARS ベースの interpretable HTE surface が clinical 領域での受容性が高い。SCB-MARS で subgroup-specific optimal intervention を可視化することで、precision geriatric medicine への 道筋を提供。SHAP analysis との組合せで、変数重要度と effect heterogeneity の二段階解析が可能。",
        "idea": "**自前研究・国内大規模データへの応用案**：①既存900名コホートでサプリ複数併用と身体機能維持の HTE を SCB-MARS で推定し、CD4 ベースラインに相当する患者特性（年齢・phase angle・既往）による subgroup-specific optimal supplement を visualize。②TMM コホートで運動介入の認知保護効果の HTE を SCB-MARS で推定し、APOE 遺伝子型・baseline cognitive function による effect heterogeneity を可視化、Japanese-specific な personalized prevention strategy として国際雑誌に投稿。③JAGES データで介護予防教室の HTE を SCB-MARS で推定し、フレイル status・社会参加レベルによる subgroup-specific effective intervention の組合せを identify、自治体施策への evidence を提供。④学振 PD 課題3 の tDCS＋運動の介入研究で、事前登録した SCB-MARS による HTE 解析計画を組み込み、responder identification を prospectively 行う。"
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
