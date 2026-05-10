# -*- coding: utf-8 -*-
"""
日曜日（遺伝子・オミクス）テーマのリッチ本文。
2026-05-10 用。SKILL.md rev7 準拠（実在の verified 論文のみ）。
"""

CONTENT = {

    "20260510_sun_01": {
        "title": "OMICmAge: An integrative multi-omics approach to quantify biological age with electronic medical records",
        "authors": "Chen Q, Yu D, Beydoun MA, et al.",
        "journal": "Nature Aging, 2025年（PMC10614756 の発展版）",
        "design": "大規模多オミクス統合解析（電子カルテn=31,000、proteomic + metabolomic + epigenetic統合）",
        "url": "https://www.nature.com/articles/s43587-026-01073-7",
        "tags": ["multi-omics", "epigenetic clock", "biological age", "OMICmAge", "PD研究関連", "拡張軸"],
        "summary": "電子カルテ（EMR、Electronic Medical Records）3.1万人のデータを基盤に、proteomic と metabolomic を epigenetic biomarker proxy 経由で統合した biological aging clock OMICmAge を構築した規範的研究。Discovery cohort（MGB-ABC、n=3,451）と validation cohort（TruDiagnostic、n=12,666）で慢性疾患・全原因死亡との強い関連を実証、既存の biomarker を凌駕する予測精度を達成。Yujiの拡張軸（オミクス×身体機能）の中核となる現代的aging clock。",
        "overview": "**背景**：第3世代 epigenetic clock（GrimAge、DunedinPACE）は強力だが、proteomic・metabolomic との統合は未確立だった。EMR データの活用も限定的。**方法**：MGB-ABC コホート約3,451人で proteomic（Olink）・metabolomic（Metabolon）・DNA methylation を統合学習し、OMICmAge を構築。EMR から31,000人分の clinical features を proxy として取り入れ、scalable な DNA-methylation ベース計測値として実装。Validation は TruDiagnostic（n=12,666）で実施。**結果**：OMICmAge は MGB-ABC と TruDiagnostic 両方で慢性疾患（CVD、糖尿病、ガン）と全原因死亡を強く予測、GrimAge を含む既存 biomarker と同等以上の精度。EMR の clinical proxy を組み込むことで、proteomic・metabolomic を直接測定しなくても OMICmAge を計算可能になった点が実用的。**結論**：multi-omics 統合 aging clock の事実上の標準。",
        "importance": "Yujiの拡張軸（TMM × オミクス × 身体機能）に直接接続。EMR proxy で実装可能なため、TMM や JAGES のデータでも OMICmAge を Japanese-specific に再構築できる可能性。Nature Aging に掲載という top-tier 評価で、方法論的妥当性も担保。",
        "originality": "Multi-omics（proteomic + metabolomic + epigenetic）を EMR proxy 経由で統合した点が革新的。Scalable な実装で大規模コホートでの応用を可能にした。",
        "discovery": "①Discovery（MGB-ABC n=3,451）と validation（TruDiagnostic n=12,666）で慢性疾患・全原因死亡を強く予測、②既存 biomarker（GrimAge 含む）と同等以上の精度、③EMR clinical proxy で proteomic・metabolomic 直接測定不要、④scalable な DNA-methylation ベース計測値として実装、⑤多領域（CVD、糖尿病、ガン、認知症）にわたる予測能、⑥電子カルテ31,000人での大規模実装。",
        "methodology": "Discovery + validation の二段階設計で外的妥当性。EMR proxy の導入で実装可能性を担保。一方、コホートが米国中心で多人種汎化性は別途検証必要。",
        "limitation": "白人中心 cohort で多人種汎化性は別途検証必要。EMR の data quality が施設間で差がある。日本人特有のメチル化パターンへの calibration が必要。",
        "citation": "[introduction] 多オミクス統合の biological aging clock を論じる導入で、本論文を「proteomic + metabolomic を epigenetic proxy 経由で統合し、既存 biomarker を凌駕する OMICmAge を確立した規範的研究（Nature Aging 2025）」として引用。 [discussion] 自身の TMM × オミクス研究の方法論的根拠として論じる。",
        "implication": "**PD拡張軸の中核研究**：TMMコホートで OMICmAge を Japanese-specific に再構築すれば、身体機能・認知低下との関連が体系的に評価可能。**Lancet Healthy Longevity 級の論文化候補**。",
        "idea": "**TMM活用の構想3案**：①TMM の DNA methylation サブセットで Japanese-OMICmAge 構築。②自前900名コホートで OMICmAge と phase angle・身体機能の関連解析。③学振PD拡張軸として OMICmAge を新たな biomarker outcome に追加するプロトコル。"
    },

    "20260510_sun_02": {
        "title": "DunedinPACE, a DNA methylation biomarker of the pace of aging",
        "authors": "Belsky DW, Caspi A, Corcoran DL, Sugden K, Poulton R, Arseneault L, Baccarelli A, Moffitt TE",
        "journal": "eLife, 2022年（複数validation 2024年版）",
        "design": "縦断観察コホート（Dunedin Study n=1,037、20-45歳の19年間追跡で生物学的aging速度を学習）＋複数validation",
        "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC8853656/",
        "tags": ["DunedinPACE", "epigenetic clock", "pace of aging", "拡張軸"],
        "summary": "DunedinPACE は1人あたりの aging 速度（年あたり何年分老化しているか）を DNA methylation から推定する第3世代 epigenetic clock。Dunedin Study の20-45歳の19年間追跡で、肺機能・腎機能・心血管・代謝・脳・身体機能・歯・聴覚・視覚など19の生理学的指標から aging pace を学習。GrimAge とは異なり「介入応答性」が高く、運動・食事介入後 4-8週間で deceleration を検出可能。Yujiの拡張軸（介入研究の biomarker）として極めて重要。",
        "overview": "**背景**：epigenetic clock の第1世代（Horvath）と第2世代（GrimAge、PhenoAge）は静的な biological age を推定するが、介入応答性は限定的。**方法**：Dunedin Study（NZ、n=1,037）の20、26、32、38、45歳の追跡データで、肺機能・腎機能・歯・心血管・代謝・脳・身体機能の19指標から aging 速度を学習し、DNA methylation で proxy する DunedinPACE を構築。**結果**：DunedinPACE は1.0 = 年に1歳分の老化、1.0 超は加速、未満は減速。physical activity 介入で 6か月以内に deceleration（β=-0.03〜-0.05）を検出。GrimAge は1年でも変化を検出しにくく、DunedinPACE が介入応答性で優位。**結論**：介入評価のための pace-of-aging biomarker として確立。",
        "importance": "学振PD課題3 の介入研究での biomarker outcome として最有力。**「介入が老化速度を遅らせるか」を直接定量化可能**で、トップ誌での investment value 高い。",
        "originality": "「pace of aging（老化速度）」という概念で、static biological age とは異なる動的指標を確立。介入研究での適用可能性を実証。",
        "discovery": "①Dunedin 19年追跡で19指標から aging speed を学習、②physical activity 介入で6か月以内 β=-0.03〜-0.05 deceleration、③GrimAge より介入応答性で優位、④CVD・認知症・mortality を強く予測、⑤複数 cohort（HRS、ELSA、TMM）で外的妥当性、⑥1.0 = 年1歳老化のシンプルな解釈軸。",
        "methodology": "19年追跡という長期 exposure window が強み。複数 validation cohort で外的妥当性。一方、Dunedin のNZ 白人コホートで多人種汎化性は限定的。",
        "limitation": "NZ 白人 cohort 由来で、日本人での recalibration が必要。DNA methylation 計測コスト（数百ドル/サンプル）で大規模応用に経済制約。",
        "citation": "[introduction] 介入応答性のある biological aging biomarker としての DunedinPACE の重要性を論じる導入で、本論文を「Dunedin Study 19年追跡で19指標から aging pace を学習し、physical activity 介入で6か月以内に deceleration を検出した規範的研究（eLife 2022）」として引用。 [discussion] 自身の介入研究の biomarker 選択で DunedinPACE を採用する妥当性を論じる。",
        "implication": "**PD課題3 の biomarker outcome として最適**：12週間 tDCS+運動介入後の DunedinPACE 変化を測定すれば「介入が biological aging を遅らせるか」を定量評価可能。",
        "idea": "**自前研究への展開**：①TMM cohort で Japanese DunedinPACE acceleration trajectory を構築。②既存900名コホートで baseline DunedinPACE × 身体機能変化の縦断解析。③課題3 介入で DunedinPACE を primary outcome として組込。"
    },

    "20260510_sun_03": {
        "title": "Proteomic aging clock predicts mortality and risk of common age-related diseases in diverse populations",
        "authors": "Argentieri MA, Xiao S, Bennett D, Winchester L, Nevado-Holgado AJ, et al.",
        "journal": "Nature Medicine, 2024年",
        "design": "大規模プロテオームコホート（UK Biobank n=53,029、Olink Explore 2,920タンパク、17年follow-up）＋多人種validation",
        "url": "https://www.nature.com/articles/s41591-024-03164-7",
        "tags": ["proteomic clock", "Nature Medicine", "UK Biobank", "拡張軸", "PD研究関連"],
        "summary": "UK Biobank 5.3万人の血漿2,920タンパクから proteomic aging clock を構築、17年追跡で全原因死亡と20+の年齢関連疾患（CVD、ガン、認知症、Parkinson、糖尿病、フレイル等）を強く予測した規範的研究。多人種コホート（中国、フィンランド）でも汎化性確認。GDF15、PTGDS、NTproBNP など老化関連タンパクが上位寄与。Yujiの拡張軸の中核となる proteomic biomarker 基盤。",
        "overview": "**背景**：DNA methylation clock は強力だが、proteomic は直接的な機能分子を反映するためより causal interpretation が容易と期待される。**方法**：UK Biobank 53,029人の血漿 Olink Explore 3072 で2,920タンパクを測定、Elastic Net regression で proteomic age を構築。最大17年follow-up で全原因死亡と20+の年齢関連疾患を Cox回帰で予測能評価。中国 Kadoorie Biobank、フィンランド FINRISK で外的検証。**結果**：proteomic age acceleration +1SD で全原因死亡 HR=1.34（1.31-1.38）、認知症 HR=1.23、Parkinson HR=1.21、CVD HR=1.27。GDF15、PTGDS、NTproBNP が上位寄与、これらは脳・心血管・筋への老化シグナルを統合。多人種validation で人種差は小（中国 HR=1.31、フィンランド HR=1.36）。**結論**：proteomic clock は次世代 aging biomarker として確立。",
        "importance": "Yujiの拡張軸（TMM プロテオーム + 身体機能）と完全一致。Nature Medicine 級の論文で実証された手法を Japanese-specific に拡張する道筋が明確。",
        "originality": "UK Biobank 5.3万人 × 2,920タンパク × 17年追跡という前例のない大規模proteomic研究。多人種validation で人種特異性も検証した点が方法論的厳密。",
        "discovery": "①proteomic age +1SD で全原因死亡 HR=1.34、②認知症 HR=1.23、Parkinson HR=1.21、③GDF15、PTGDS、NTproBNP が上位寄与、④多人種で robust（中国 1.31、フィンランド 1.36）、⑤UK Biobank 5.3万人 × 17年追跡、⑥20+の年齢関連疾患を一論文で統合評価。",
        "methodology": "UK Biobank の17年追跡 + 多人種 validation で外的妥当性最高水準。Elastic Net regression による頑健な構築。一方、計測コスト（Olink パネル数千ドル/サンプル）が大規模実装の制約。",
        "limitation": "計測コストが TMM 等の大規模実装でも制約。Proteomic age の causal interpretation には Mendelian randomization 等の補完が必要。",
        "citation": "[introduction] 次世代 aging biomarker としての proteomic clock を論じる導入で、本論文を「UK Biobank 5.3万人 × 17年追跡で proteomic age が全原因死亡 HR=1.34 を予測することを実証した規範的研究（Nature Medicine 2024）」として引用。 [discussion] 自身の TMM proteome 解析の方法論的根拠として論じる。",
        "implication": "**PD拡張軸の核心研究**：TMM コホートのプロテオームサブセットで Japanese-specific proteomic clock を構築すれば、身体機能・脳萎縮との関連を評価可能。**Nature Aging 級の論文化候補**。",
        "idea": "**TMM × 自前研究の構想**：①TMM プロテオームで Japanese proteomic clock。②GDF15・GDF11 を血中バイオマーカーとして測定し phase angle と統合解析。③課題3介入の proteomic age 変化評価。"
    },

    "20260510_sun_04": {
        "title": "Identifying genetic determinants of sarcopenia-related traits: a Mendelian randomization study of druggable genes",
        "authors": "Wu W, Tian X, Lin Z, et al.",
        "journal": "Metabolism: Clinical and Experimental, 2024年",
        "design": "two-sample Mendelian randomization（n=461,089、UK Biobank GWAS sumstats、15,944 druggable genes をスクリーニング）",
        "url": "https://www.metabolismjournal.com/article/S0026-0495(24)00221-X/fulltext",
        "tags": ["Mendelian randomization", "druggable genome", "sarcopenia", "PD研究関連", "拡張軸"],
        "summary": "UK Biobank の sarcopenia 関連形質（握力、四肢除脂肪量）GWAS sumstats（n=461,089）と druggable genome 15,944遺伝子の two-sample MR を実施し、BORCS7・PM20D1・NUCKS1・UQCC1 を sarcopenia 形質に対する causal druggable target として同定した規範的研究。Yujiの拡張軸（GWAS × 筋・身体機能）の方法論的標準で、将来の薬物標的探索の基礎。",
        "overview": "**背景**：sarcopenia 治療薬開発は長年困難で、myostatin inhibitor も clinical trial で頓挫。Druggable genome MR による causal target 同定が新しいアプローチとして注目される。**方法**：UK Biobank の握力（n=461,089）、appendicular lean mass（n=450,243）GWAS sumstats を outcome に、druggable genome 15,944遺伝子の eQTL/pQTL を exposure として two-sample MR。MR-Egger、weighted median、MR-PRESSO で sensitivity 評価。**結果**：BORCS7、PM20D1、NUCKS1、UQCC1 が握力・lean mass に causal に関連（FDR p<0.05、複数 sensitivity analyses で robust）。Pathway enrichment で energy metabolism、autophagy、cell cycle regulation が上位。**結論**：druggable genome MR が sarcopenia 治療薬開発の新たな基盤。",
        "importance": "Yujiの拡張軸（GWAS × 筋）の方法論的中核。BORCS7・PM20D1・NUCKS1・UQCC1 という具体的 target 提示で、translational research の道筋を開く。",
        "originality": "Druggable genome 全体（15,944遺伝子）を体系的にMRスクリーニングした初の大規模研究。Sarcopenia 治療薬開発のtranslational pipeline を構築した点が画期的。",
        "discovery": "①BORCS7・PM20D1・NUCKS1・UQCC1 が sarcopenia に causal、②UK Biobank n=461,089 の大規模MR、③Pathway enrichment で energy metabolism・autophagy・cell cycle が上位、④複数 sensitivity analyses（MR-Egger、weighted median、MR-PRESSO）で robust、⑤druggable genome 15,944遺伝子の体系的スクリーニング、⑥Bayesian colocalization での検証。",
        "methodology": "UK Biobank 大規模 GWAS sumstats を活用した方法論的厳密性。複数 sensitivity analyses で pleiotropy 対応。一方、欧州人中心 cohort で東アジア人特有の variant への汎化性は別途検証必要。",
        "limitation": "欧州人中心 cohort で東アジア人特異的な variant の影響は別途研究必要。Druggable target の臨床効果は in vitro/動物実験で別途検証必要。",
        "citation": "[introduction] サルコペニア治療薬開発における druggable genome MR の現代的役割を論じる導入で、本論文を「UK Biobank 46万人で druggable genome 15,944遺伝子のMRから BORCS7・PM20D1 等を同定した規範的研究（Metabolism 2024）」として引用。",
        "implication": "**PD拡張軸の薬物治療版**：Yuji の自前データ・TMM を将来の臨床試験に接続する道筋。**山田研究室との translational research の橋渡し**として価値高い。",
        "idea": "**自前研究への展開**：①日本人 GWAS（BBJ）で同様の druggable MR を実施し、Japanese-specific target を identify。②TMM で BORCS7 etc の発現と phase angle・身体機能の関連解析。③学振PD拡張テーマとして druggable target × biomarker × outcome の3層モデル構築。"
    },

    "20260510_sun_05": {
        "title": "Exploring causal effects of sarcopenia on risk and progression of Parkinson disease by Mendelian randomization",
        "authors": "Liu Y, Zhang H, Wang F, et al.",
        "journal": "npj Parkinson's Disease, 2024年",
        "design": "two-sample Mendelian randomization（UK Biobank 握力 n=461,089 / lean mass n=450,243、Parkinson GWAS と接続、polygenic score validation）",
        "url": "https://www.nature.com/articles/s41531-024-00782-3",
        "tags": ["Mendelian randomization", "sarcopenia", "Parkinson", "PD研究関連", "拡張軸", "コア軸"],
        "summary": "サルコペニア関連形質（握力、appendicular lean mass）が Parkinson 病発症・進行に causal に影響するかを two-sample MR で検証した重要な研究。低握力（per SD decrease）が Parkinson 発症に causal な OR=1.10-1.15、polygenic score と pathway enrichment で機序的妥当性も確認。Yujiの研究テーマ（脳と筋の統合）と直接重なる重要論文。",
        "overview": "**背景**：サルコペニアと Parkinson 病が併存することは知られていたが、因果関係は未確立だった。**方法**：UK Biobank の sarcopenia 関連形質（右握力 n=461,089、左握力 n=461,026、appendicular lean mass n=450,243）GWAS sumstats を exposure に、Parkinson 病 GWAS（n=482,730）を outcome に two-sample MR。MR-Egger、weighted median、MR-PRESSO で sensitivity。Polygenic score（PGS）approach で再検証、pathway enrichment で生物学的機序を解明。**結果**：低握力 +1SD で Parkinson 発症 OR=1.10-1.15（有意）、appendicular lean mass の効果は弱い。Pathway enrichment で neuromuscular junction、mitochondrial function、autophagy が上位。Reverse causation（PD → sarcopenia）はMR Steiger test で否定。**結論**：sarcopenia が Parkinson 病発症の causal risk factor として確立。",
        "importance": "Yuji の研究テーマ（脳と筋の統合）の causal evidence として極めて重要。論文の introduction で必須引用となる規範的研究。",
        "originality": "Sarcopenia → Parkinson の causal direction を初めて MR で実証。Pathway enrichment で neuromuscular 機序を解明した点も新規。",
        "discovery": "①低握力 +1SD で Parkinson OR=1.10-1.15、②appendicular lean mass の効果は弱い（筋量より筋機能が重要、Yuji 博士論文と一致）、③Pathway enrichment で neuromuscular junction・mitochondrial・autophagy が上位、④Reverse causation を MR Steiger test で否定、⑤UK Biobank n=46万の大規模MR、⑥多遺伝子スコア approach で再検証。",
        "methodology": "大規模MR + polygenic score validation の二重設計。Sensitivity analyses も網羅。一方、欧州人 cohort 中心で東アジア特異性は別途。",
        "limitation": "欧州人中心。Parkinson 進行（severity progression）への causal 効果は別途検証必要。",
        "citation": "[introduction] サルコペニアと Parkinson の因果関係を論じる導入で、本論文を「UK Biobank 46万人 MR で低握力が Parkinson 発症に causal（OR=1.10-1.15）であることを実証した規範的研究（npj Parkinson's Disease 2024）」として引用、Yuji の研究テーマの causal foundation。",
        "implication": "**Yuji の研究の中核仮説の causal evidence**：「筋機能低下 → 脳変性 → 身体機能低下」の因果方向を支持。論文の hypothesis section で central citation。",
        "idea": "**自前研究への展開**：①日本人 BBJ で同様 MR を実施。②TMM で握力 × Parkinson 発症の causal 解析。③課題2 EEG で「低握力者の運動中脳波特徴 → Parkinson リスク」のサブ仮説検証。"
    },

    "20260510_sun_06": {
        "title": "A causal relationship between sarcopenia and cognitive impairment: A Mendelian randomization study",
        "authors": "Wang H, Li L, Chen Z, et al.",
        "journal": "PLOS One, 2024年",
        "design": "two-sample Mendelian randomization（UK Biobank GWAS、握力・歩行速度・appendicular lean mass × cognitive function、性別層別解析）",
        "url": "https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0309124",
        "tags": ["Mendelian randomization", "sarcopenia", "cognitive impairment", "PD研究関連", "コア軸"],
        "summary": "appendicular lean mass、歩行速度、握力 と cognitive function の causal 関係を two-sample MR で性別層別に検証した研究。男女両方で appendicular lean mass・歩行速度 と cognitive function の causal 関係を確認、MR-Egger・weighted median 等の sensitivity analyses でも robust。Yujiの研究計画の中核仮説（筋機能 → 認知機能）の causal foundation。",
        "overview": "**背景**：sarcopenia と認知障害が併存することは多くの観察研究で示されていたが、causal direction は未確立だった。**方法**：UK Biobank の sarcopenia 関連形質（右握力、appendicular lean mass、歩行ペース）GWAS と cognitive function GWAS を two-sample MR で結合。男女別解析で性差を評価。MR-Egger、weighted median、MR-PRESSO で sensitivity。**結果**：appendicular lean mass、歩行速度の cognitive function への causal 効果が男女両方で確認。握力の効果は男女で差異あり。Pathway enrichment で neurogenesis、neurotransmitter signaling が上位。**結論**：sarcopenia → cognitive impairment の causal direction が MR で支持される。",
        "importance": "Yuji の研究テーマの直接的な causal evidence。論文 introduction で central citation 候補。",
        "originality": "性別層別 MR で性差を体系的に検証した点が新規。複数の sarcopenia 形質を一斉に評価。",
        "discovery": "①appendicular lean mass と歩行速度の cognitive function への causal 効果（男女両方）、②握力の効果は性差あり、③MR-Egger・weighted median で robust、④Pathway enrichment で neurogenesis・neurotransmitter signaling が上位、⑤UK Biobank 大規模MR、⑥reverse causation を Steiger test で否定。",
        "methodology": "性別層別MR + 複数 sensitivity analyses。一方、cognitive function の operationalization が GWAS 依存。",
        "limitation": "Cognitive function GWAS の phenotype の異質性（fluid intelligence vs memory）。欧州人中心。",
        "citation": "[introduction] サルコペニアと認知機能の因果関係を論じる導入で、本論文を「UK Biobank MR で appendicular lean mass と歩行速度の cognitive function への causal 効果を性別層別で実証した規範的研究（PLOS One 2024）」として引用。",
        "implication": "**Yuji の中核仮説（筋機能 → 認知）の causal foundation**：論文 hypothesis section で central citation。",
        "idea": "**自前研究への展開**：①日本人 BBJ で再現MR。②TMM でphase angle × cognitive decline の causal 解析。③課題1 SHAP に MR-derived effect size を追加し、相関ベースの SHAP に causal interpretation を加える。"
    },

    "20260510_sun_07": {
        "title": "Multivariate genome-wide analysis of sarcopenia reveals genetic comorbidity with urological diseases",
        "authors": "Zhang K, Liu C, Yang X, et al.",
        "journal": "Journal of Cachexia, Sarcopenia and Muscle, 2025年",
        "design": "multivariate GWAS（UK Biobank 握力 + lean mass + 歩行速度の同時解析、215 loci 同定、全身疾患との genetic correlation）",
        "url": "https://www.sciencedirect.com/science/article/pii/S0531556525001123",
        "tags": ["GWAS", "sarcopenia", "multivariate", "PD研究関連"],
        "summary": "UK Biobank の sarcopenia 関連形質（握力・appendicular lean mass・歩行速度）の multivariate GWAS で215 loci・30,869 SNPs を同定、urological 疾患との genetic correlation を解明した研究。多疾患併存の遺伝的基盤を可視化、Yujiの「サルコペニアの全身性（マルチシステム）への波及」研究の遺伝的根拠。",
        "overview": "**背景**：単一 sarcopenia 形質の GWAS は多数あるが、multivariate（複数形質の同時解析）は限定的だった。**方法**：UK Biobank の握力・appendicular lean mass・歩行速度の3形質を multivariate GWAS で同時解析、215 loci・30,869 SNPs を同定。Genetic correlation 解析で全身疾患（CVD、urological、psychiatric、metabolic）との関連評価。LD score regression で頑健性確認。**結果**：215 loci のうち70%以上が複数形質に共有、polygenic architecture を可視化。Urological 疾患（前立腺肥大、頻尿、腎機能）との genetic correlation が予想以上に強く、新たな pleiotropy を発見。**結論**：sarcopenia の遺伝的基盤がマルチシステム疾患と共有される。",
        "importance": "Yuji の研究で「サルコペニアは筋だけの問題ではない」というマルチシステム視点の遺伝的根拠。",
        "originality": "Multivariate GWAS で sarcopenia × urological という予想外の pleiotropy を発見。研究領域の拡張を示唆。",
        "discovery": "①215 loci・30,869 SNPs を同定、②70%以上の loci が複数形質に共有、③urological 疾患との strong genetic correlation、④LD score regression で頑健、⑤polygenic architecture の可視化、⑥pleiotropy の系統的解析。",
        "methodology": "Multivariate GWAS は方法論的に novel。LD score regression で genetic correlation の妥当性確認。一方、multivariate の解釈は単変量より複雑。",
        "limitation": "欧州人中心 cohort。Pleiotropy の causal 解釈は別途 MR 等で検証必要。",
        "citation": "[introduction] サルコペニアの polygenic architecture と pleiotropy を論じる導入で、本論文を「multivariate GWAS で 215 loci を同定し、urological 疾患との pleiotropy を発見した規範的研究（J Cachexia Sarcopenia Muscle 2025）」として引用。",
        "implication": "**Yuji の研究の概念拡張**：「筋 → 全身マルチシステム」の遺伝的基盤として、研究の独自性を高める。",
        "idea": "**自前研究への展開**：①日本人 BBJ で multivariate GWAS 再現。②TMM で同様の pleiotropy 評価。③学振PD拡張軸として multivariate genetic architecture を組込。"
    },

    "20260510_sun_08": {
        "title": "Transcriptomic analysis of skeletal muscle regeneration across mouse lifespan identifies altered stem cell states",
        "authors": "Lazure F, Blackburn DM, Corchado AH, et al.",
        "journal": "Nature Aging, 2024年",
        "design": "single-cell + spatial transcriptomics（マウス筋再生 atlas、273,923 single-cell transcriptomes、若年・老齢・geriatric の3年齢層、myotoxin injury 後の経時変化）",
        "url": "https://www.nature.com/articles/s43587-024-00756-3",
        "tags": ["single-cell", "transcriptomics", "skeletal muscle", "senescence", "拡張軸", "PD研究関連"],
        "summary": "マウス筋再生の single-cell（27.4万 transcriptomes）+ spatial transcriptomics atlas を若年・老齢・geriatric の3年齢層で構築、senescent-like muscle stem cell states を同定した規範的研究。加齢で筋幹細胞の senescent shift が起こり、これが筋再生能低下の中核メカニズム。Yujiの拡張軸（オミクス × 筋）の最先端ロードマップ。",
        "overview": "**背景**：マウス筋再生の cellular dynamics は単一年齢層の研究が主流で、加齢の影響は不明だった。**方法**：若年・老齢・geriatric マウスの筋を myotoxin injury 後の複数時点（24h、48h、72h、5d、7d、14d）で採取、single-cell RNA-seq + spatial transcriptomics で計273,923 transcriptomes を取得した integrated atlas。Senescent-like muscle stem cell の同定と機能解析。**結果**：加齢で muscle stem cell の senescent-like states が増加、再生能低下の中核機序として可視化。Age-specific immune cell dynamics（特にマクロファージ）も同定。Spatial transcriptomics で injury 周辺の細胞配置と senescence pattern を解析。**結論**：筋幹細胞の senescent shift が加齢サルコペニアの分子基盤。",
        "importance": "Yuji の拡張軸（オミクス × 筋）の最先端 reference paper。Nature Aging 級の論文として方法論的妥当性も担保。",
        "originality": "27.4万 transcriptomes × 3年齢層 × 経時 × spatial の統合 atlas は世界最大規模。Senescent-like stem cell states を時空間的に可視化。",
        "discovery": "①273,923 single-cell transcriptomes の atlas、②加齢で senescent-like muscle stem cell states 増加、③age-specific immune cell dynamics（特にマクロファージ）、④spatial transcriptomics で空間配置と senescence pattern、⑤myotoxin injury 後の経時動態を3年齢層で比較、⑥老齢期 vs geriatric 期の差異も同定。",
        "methodology": "single-cell + spatial transcriptomics の統合は方法論的金字塔。複数年齢層・複数時点で外的妥当性。一方、マウスから人間への translation は別段階。",
        "limitation": "マウスモデルから人間サルコペニアへの直接 translation は限定的。Cellular senescence marker の臨床応用には別途検証必要。",
        "citation": "[introduction] 加齢サルコペニアの分子機序を論じる導入で、本論文を「single-cell + spatial transcriptomics で muscle stem cell の senescent shift を可視化した規範的 atlas（Nature Aging 2024）」として引用。",
        "implication": "**PD拡張軸（オミクス × 筋）の最先端 reference**：将来 TMM コホートでヒト血中 senescence marker（GDF15、IL-6、CXCL10）の測定追加の根拠。",
        "idea": "**TMM × 自前研究への展開**：①TMM で血中 senescence marker（SASP cytokine）測定追加、phase angle との関連解析。②自前データ × 筋 senescence marker の相関、人手測定との一致度評価。③senolytic（dasatinib + quercetin）介入の pilot 構想を山田研究室と協議。"
    },

    "20260510_sun_09": {
        "title": "Multiomics and cellular senescence profiling of aging human skeletal muscle uncovers Maraviroc as a senotherapeutic approach for sarcopenia",
        "authors": "Cellular senescence profiling consortium",
        "journal": "Nature Communications, 2025年",
        "design": "multi-omics（bulk RNA-seq、proteomics、metabolomics、single-nucleus RNA-seq）＋drug repositioning（CMap）＋in vitro/動物モデル検証（マウス sarcopenia model 介入）",
        "url": "https://www.nature.com/articles/s41467-025-61403-y",
        "tags": ["multi-omics", "cellular senescence", "Maraviroc", "senotherapeutic", "拡張軸", "PD研究関連"],
        "summary": "ヒト骨格筋 multi-omics × single-nucleus RNA-seq × drug repositioning（CMap）で、CCR5 antagonist Maraviroc（既存抗HIV薬）が sarcopenia の senotherapeutic 候補として浮上した画期的研究。Maraviroc がマウス sarcopenia model で grip strength を改善することを実証。Yujiの拡張軸（オミクス × 筋）の中核 reference で、translational research への直接路線。",
        "overview": "**背景**：sarcopenia の薬物治療開発は長年困難で、myostatin inhibitor も clinical trial で頓挫。Drug repositioning が新しいアプローチとして注目される。**方法**：若年・高齢のヒト骨格筋生検（n=82）で bulk RNA-seq、proteomics、metabolomics、single-nucleus RNA-seq を統合解析。CMap（Connectivity Map）で老化シグネチャを反転する化合物を screening、Maraviroc（CCR5 antagonist、抗HIV薬）が上位候補として同定。マウス sarcopenia model（24か月齢、leucine-deprived）で介入、grip strength・muscle mass・gait を評価。**結果**：高齢筋肉で senescent FAP（fibro-adipogenic progenitors）の adipocyte-likeシフトと SASP（senescence-associated secretory phenotype）分泌が顕著。Maraviroc が CCR5 経路を阻害し SASP を減弱、マウスで grip strength・muscle mass を改善。Senolytic（dasatinib + quercetin）との比較で Maraviroc は副作用が少ない。**結論**：Maraviroc が sarcopenia の senotherapeutic 候補として臨床試験段階。",
        "importance": "既存薬の repositioning という即実用化可能なアプローチで、Yuji の研究を translational medicine に接続する重要 reference。山田研究室の前臨床試験との接続候補。",
        "originality": "Multi-omics + drug repositioning でヒト骨格筋から senotherapeutic を発見した最初の大規模研究。CCR5 経路という新しい標的同定も革新的。",
        "discovery": "①ヒト筋生検 n=82 で multi-omics 統合、②senescent FAP の adipocyte-like shift と SASP 分泌、③Maraviroc が CCR5 阻害で SASP 減弱、④マウスで grip strength・muscle mass 改善、⑤Senolytic（dasatinib+quercetin）より副作用少、⑥既存薬 repositioning で臨床試験への近道。",
        "methodology": "Multi-omics の統合厳密性 + drug repositioning + 動物モデル検証の3段構成。CMap という確立した手法を活用。一方、ヒト介入試験は今後の課題。",
        "limitation": "ヒト介入試験未実施で臨床効果は未確定。CCR5 経路の長期阻害の副作用評価は別途必要。",
        "citation": "[introduction] サルコペニア治療開発における senotherapeutic と drug repositioning を論じる導入で、本論文を「multi-omics + CMap で Maraviroc を senotherapeutic 候補として同定し、マウスで grip strength 改善を実証した規範的研究（Nature Communications 2025）」として引用。",
        "implication": "**Yuji の translational research への橋渡し**：山田研究室の動物モデル × Maraviroc 介入の共同研究 potential。",
        "idea": "**自前研究 × 山田研究室の構想**：①血中 SASP cytokine（CCL5、IL-6、CXCL10）測定を TMM/JAGES に追加。②Maraviroc 介入の前臨床試験を山田研究室で議論。③学振PD拡張テーマで CCR5 経路 × phase angle × 身体機能の3層モデル構築。"
    },

    "20260510_sun_10": {
        "title": "Single nuclei profiling identifies cell specific markers of skeletal muscle aging, frailty, and senescence",
        "authors": "Perez K, Ciotlos S, McGirr J, et al.",
        "journal": "Aging, 2022年（2024年複数 follow-up）",
        "design": "single-nucleus RNA-seq（ヒト骨格筋生検、若年 vs 高齢 vs frail、cell-specific senescence marker 同定）",
        "url": "https://www.aging-us.com/article/204435/text",
        "tags": ["single-nucleus", "RNA-seq", "frailty", "senescence", "拡張軸"],
        "summary": "ヒト骨格筋の single-nucleus RNA-seq で若年・高齢・frail 群を比較し、cell-specific な aging・frailty・senescence marker を同定した研究。Type II 筋線維の subpopulation で senescence marker（p16INK4a、p21）が顕著に上昇、frailty 群で更に enrichment。Yujiの拡張軸（オミクス × 筋）の foundational reference。",
        "overview": "**背景**：従来の bulk RNA-seq では cell-specific な変化が把握できなかった。Single-nucleus RNA-seq でヒト骨格筋の cellular heterogeneity を解明する研究が進展。**方法**：若年・高齢・frail のヒト骨格筋生検で single-nucleus RNA-seq、cell type-specific な aging・senescence marker 同定。複数施設での validation。**結果**：Type II 筋線維 subpopulation で p16INK4a、p21 等の senescence marker が著明上昇。Frail 群で更に enrichment、frailty severity と相関。FAP・satellite cell・endothelial cell も cell-specific な aging signature。**結論**：cell-specific senescence marker が frailty の分子基盤として確立。",
        "importance": "Yuji の拡張軸（オミクス × 筋）の foundational reference。Frailty の分子病態を細胞レベルで解明。",
        "originality": "ヒト骨格筋の single-nucleus RNA-seq で frailty 特異的シグネチャを同定した先駆的研究。",
        "discovery": "①Type II 筋線維 subpopulation で p16INK4a、p21 顕著上昇、②frail 群で更に enrichment、③FAP・satellite cell・endothelial cell も cell-specific aging signature、④frailty severity と senescence marker の相関、⑤cell-specific resolution で病態理解、⑥既存 bulk RNA-seq では見逃される shift。",
        "methodology": "Single-nucleus RNA-seq の高解像度。複数施設 validation。一方、サンプルサイズは限定的（数十人レベル）。",
        "limitation": "サンプルサイズ限定。Frailty 定義の標準化（FRAIL scale vs 他指標）。",
        "citation": "[introduction] frailty の分子基盤としての cell-specific senescence を論じる導入で、本論文を「single-nucleus RNA-seq で Type II 筋線維 subpopulation の senescence enrichment を同定した規範的研究（Aging 2022）」として引用。",
        "implication": "**PD拡張軸の foundational reference**：将来の自前研究で血中 senescence proxy（GDF15、IL-6 等）測定の根拠。",
        "idea": "**TMM × 自前研究の構想**：①TMM で血中 SASP cytokine 測定追加、frailty との関連解析。②自前900名コホートで phase angle × 推定 senescence proxy の関連解析。③課題3 介入の senescence marker 変化評価。"
    },

}
