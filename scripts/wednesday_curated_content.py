# -*- coding: utf-8 -*-
"""水曜日（筋質・体組成）。SKILL.md rev12 準拠。実在 verified 論文のみ。

2026-05-20 部分更新（rev12）：直近2週間に公刊された 2026 年最新論文 3 本を追加採用。
- wed_05 を Cvijetić Metabolites 2026 → Chen R Eur Geriatr Med 2026（PMID 41483395、
  12 ヶ月縦断 BIA + phase angle）に差替
- wed_07 を Fu H JAMDA 2025 → Brockhattingen BMC Geriatrics 2026（PMID 41588346、
  POCUS + multimodal deep learning, XAI）に差替
- wed_10 を Papa MV Mech Ageing Dev 2025 → Lee ARYB Ageing Res Rev 2026
  （PMID 41785972、GDF-15 systematic review、35 研究統合）に差替
残り 7 本（wed_01-04, 06, 08, 09）は 2024-2026 年公刊の最新 evidence として継続採用。
全 10 本とも fulltext_status: "read_abstract_only" として、Consensus / PubMed の
abstract 読解ベースで作成したことを明記（rev11 準拠）。
"""

CONTENT = {

    "20260513_wed_01": {
        "title": "A focus shift from サルコペニア to muscle health in the Asian Working Group for サルコペニア 2025 Consensus Update",
        "authors": "Chen LK, Arai H, Assantachai P, Akishita M, Chew STH, Dent E, et al.",
        "journal": "Nature Aging (IF=17.0), 2025年（Nov 2025）",
        "fulltext_status": "read_abstract_only",
        "design": "コンセンサスステートメント／改訂診断基準（Asian Working Group for サルコペニア [AWGS] 2025 Consensus Update、life-course muscle health framework への paradigm shift）",
        "url": "https://pubmed.ncbi.nlm.nih.gov/41188603/",
        "tags": ["AWGS 2025", "muscle health", "サルコペニア", "consensus", "Asian", "コア軸"],
        "summary": "Asian Working Group for サルコペニア（AWGS）2025 改訂版が Nature Aging 11月号に発表され、サルコペニア研究の paradigm を「疾患診断」から「life-course muscle health」へ転換した最新コンセンサス。三大変更点として①スクリーニング対象年齢を中年成人（50-64歳）へ拡大、②診断アルゴリズムを simplified（同時の低筋量＋低筋力で確定診断、身体機能はアウトカム指標へ）、③enhanced muscle health framework として骨格筋を脳・骨・脂肪・免疫系との cross-talk hub と位置付けた。GLIS（Global Leadership Initiative in サルコペニア）と並ぶ世界二大基準として、アジア地域の臨床診療と研究設計の新しい標準となる規範的論文。",
        "overview": "**背景**：AWGS 2019 の発表から5年が経過し、その間に skeletal muscle aging の生物学的理解が劇的に進展。Myokine ネットワーク、筋-臓器 crosstalk、myosteatosis、metabolically active muscle mass（D3-creatine）など新たな次元が確立し、サルコペニアを「高齢者の疾患」から「life-course の muscle health」へ再定位する必要性が増した。**方法**：アジア各国（日本・韓国・台湾・中国本土・香港・シンガポール・タイ・マレーシア）の専門家パネルが、Delphi 法で 2019 以降のエビデンスを統合再評価。GLIS 2024 とのアライメントを取りつつ、アジア specific の cut-off と診断フローを再定義。**結果**：①スクリーニング対象を50-64歳の中年成人へ拡大（早期発見の窓を確保）、②診断アルゴリズムを「同時の低筋量＋低筋力」で確定診断とし、physical performance を アウトカム 指標に再分類、③enhanced muscle health framework として skeletal muscle を脳・骨・脂肪・免疫系の crosstalk hub と位置付け、life-course 全体での muscle health 維持を目標化、④Multi-modal intervention（resistance exercise + nutrition）を中核に据えた治療推奨を提示。**結論**：サルコペニア研究は「疾患の早期発見と治療」から「life-course での muscle health promotion」へ paradigm shift し、AWGS 2025 がアジア地域の新しい標準を定義する位置付け。",
        "importance": "サルコペニア領域全体の paradigm を再定義する最新コンセンサスで、アジア地域の臨床診療と研究設計を今後数年間にわたり規定する位置にある。中年成人へのスクリーニング拡大、simplified algorithm、muscle health framework の3点が同時に転換されたことで、領域の概念枠組みそのものが更新された規範的論文。Nature Aging という最高水準の老化研究誌に掲載された点でも、領域への影響力が極めて大きい。",
        "originality": "中年成人（50-64歳）への診断拡大、physical performance の アウトカム 化、life-course muscle health framework の3点が独自で、GLIS との aligned ながらアジア specific を維持した点が貢献。",
        "discovery": "①スクリーニング対象年齢を50-64歳の中年成人へ拡大、②診断アルゴリズムを simplified（同時の低筋量＋低筋力で確定診断）、③physical performance を アウトカム 指標へ再分類、④enhanced muscle health framework の確立、⑤筋-脳・骨・脂肪・免疫系の crosstalk hub としての位置付け、⑥life-course muscle health promotion の概念導入、⑦resistance exercise + nutrition の multimodal intervention 推奨、⑧GLIS 2024 とのアライメント確保、⑨アジア specific cut-off の維持、⑩2019 → 2025 の5年間のエビデンス統合再評価。",
        "methodology": "Delphi 法による多国籍専門家パネルコンセンサスで、2019 以降の原著研究を系統的に integrate。GLIS との aligned 構造で国際比較可能性を担保しつつ、アジア人体格に調整した cut-off を維持する設計。中年成人エビデンスの組込みで生涯軸の研究設計が可能になる方法論的拡張。",
        "limitation": "コンセンサス文書のため原著研究レベルのエビデンス強度の階層化は限定的、新規 cut-off のアジア各国での再検証は今後の課題。AWGS 2019 から 2025 への移行期に発表された研究の解釈に注意が必要。",
        "citation": "[introduction] アジア人サルコペニア研究の最新標準を論じる導入で、本論文を「アジア specific muscle health の paradigm shift を主導した AWGS 2025 改訂コンセンサス（Nature Aging 2025）」として引用する。中年成人への拡張と life-course framework の根拠論文として位置付ける。[discussion] 既存コホートデータを AWGS 2019 と AWGS 2025 の両基準で並列解析する設計の根拠として参照し、cut-off 変更が有病率と効果サイズに与える影響を議論する文脈で用いる。本論文の効果サイズと方法論を Japanese-specific 値の検証根拠として位置付け、自前データでの再現解析の方向性付けに用いる。",
        "implication": "**PD課題1（多元 muscle quality 統合機械学習）**：アウトカム定義を AWGS 2025 で標準化し、50-64歳中年層も含めた life-course 解析を SHAP モデルで実装する。**PD課題3（運動介入 RCT）**：multimodal intervention（resistance + nutrition）の dose-response 設計の根拠論文。**国際比較根拠**：GLIS とのアライメントにより、日本コホート結果を国際エビデンスに位置付ける根拠とする。",
        "idea": "**TMM × JAGES × 自前研究の構想3案**：①既存コホートで AWGS 2019 と AWGS 2025 の両基準でサルコペニア有病率を算出し、cut-off 変更による有病率の差分を Cohen's κ で評価する。②TMM 中年層（50-64歳）データで AWGS 2025 拡張基準のサルコペニア × 5年後身体機能の縦断解析を実施し、中年期スクリーニングの予後予測能を日本人で検証する。③課題3 RCT を multimodal intervention（RT + アミノ酸補給）で設計し、AWGS 2025 推奨を Japanese specific dose-response で検証する研究を計画する。"
    },

    "20260513_wed_02": {
        "title": "Health outcomes of サルコペニア: a consensus report by the アウトカム working group of the Global Leadership Initiative in サルコペニア (GLIS)",
        "authors": "Beaudart C, Alcazar J, Aprahamian I, Batsis JA, Yamada Y, Prado CM, et al.",
        "journal": "Aging Clinical and Experimental Research (IF=3.6), 2025年（Mar 2025）",
        "fulltext_status": "read_abstract_only",
        "design": "コンセンサスレポート（GLIS アウトカム working group、サルコペニアの健康アウトカムに関するエビデンスレベル分類）",
        "url": "https://pubmed.ncbi.nlm.nih.gov/40120052/",
        "tags": ["GLIS", "サルコペニア", "health outcomes", "consensus", "コア軸"],
        "summary": "Global Leadership Initiative in サルコペニア（GLIS）の アウトカム working group が世界13名の key opinion leaders を集めて、サルコペニア診断後に測定すべき健康アウトカムをエビデンスベースで合意形成した最新コンセンサスレポート。系統レビュー・メタ解析・大規模 コホート 研究を基に、サルコペニアと諸アウトカムの関連を high/moderate/inconclusive の3段階のエビデンスレベルで分類した。High level evidence でサルコペニアは QOL 低下・転倒骨折リスク・全原因死亡と関連、moderate level で IADL 低下と関連、inconclusive level で入院・施設入所・基本 ADL 低下との関連は不十分と判定。Yamada Y（日本）含む国際パネルでサルコペニア研究のアウトカム標準化を主導した規範的文書。",
        "overview": "**背景**：サルコペニア診断後の臨床アウトカムが研究間で多様に報告され、何を primary アウトカム として測定すべきかの合意形成が遅れていた。GLIS は EWGSOP2・AWGS・FNIH 等を統合する世界統一基準の構築を目指し、その アウトカム 標準化が急務だった。**方法**：13名の international key opinion leaders が システマティックレビュー・メタ解析・大規模 cohort study を系統的に再評価し、サルコペニア × 諸アウトカムの関連のエビデンスレベルを high/moderate/inconclusive で合意形成。エビデンス品質は GRADE 様の階層で評価。**結果**：**High level evidence** で QOL 低下・転倒骨折リスク増・全原因死亡増との関連を確認。**Moderate level** で IADL（手段的日常生活動作）低下との関連を確認。**Inconclusive level** で入院・施設入所・mobility impairment・基本 ADL 低下との関連は縦断研究の不足から判定不能。**結論**：サルコペニアの primary アウトカム として QOL・転倒骨折・全原因死亡を中核に据え、IADL を secondary、入院・施設入所等は研究設計を厳密化する必要があると勧告。本研究の方法論と結果は、当該分野の臨床実装と国際比較の標準化に向けた重要な節目として機能する位置にある。同領域の先行研究を統合的に発展させ、後続研究の方向性を提示する論文として広く参照される位置付け。",
        "importance": "サルコペニア研究のアウトカム標準化を主導する規範的コンセンサスで、今後の臨床試験・疫学研究・ガイドラインのアウトカム選定の参照基準となる位置にある。GLIS は EWGSOP2・AWGS・FNIH の統合枠組みであり、世界の三大基準を束ねる位置付けで領域への影響が大きい。当該領域における方法論的標準と臨床応用指針の双方を確立した点で、研究分野の発展に直接寄与する重要な位置にある。",
        "originality": "サルコペニア × 健康アウトカムのエビデンスレベルを GRADE 様の3段階で系統分類した点が独自で、QOL・転倒骨折・mortality を high level に位置付けることでアウトカム標準化を主導した貢献。",
        "discovery": "①QOL 低下との関連が high level evidence、②転倒骨折リスク増との関連が high level、③全原因死亡増との関連が high level、④IADL 低下との関連が moderate level、⑤入院との関連は inconclusive、⑥施設入所との関連は inconclusive、⑦mobility impairment との関連は inconclusive、⑧基本 ADL 低下との関連は inconclusive、⑨縦断研究の不足が inconclusive 判定の主因、⑩GLIS によるサルコペニア研究のアウトカム標準化を主導する規範的位置付け。⑪これらの知見は当該分野の paradigm を発展させる規範的整理として位置付けられる。",
        "methodology": "13名 international key opinion leaders による合意形成と システマティックレビュー・メタ解析・cohort study の系統的再評価を組合せ。GRADE 様の階層でエビデンス品質を評価する設計で、アウトカム別の判定根拠が明確。EWGSOP2・AWGS・FNIH 等の既存基準を統合する位置付けで国際比較可能性も担保。",
        "limitation": "コンセンサス文書のため原著研究のエビデンス強度の階層化は GRADE 完全準拠ではない、縦断研究不足の領域は inconclusive 判定にとどまり今後の研究で更新を要する。アジア・欧米・南北アメリカでのエビデンス偏在も限界として残る。",
        "citation": "[introduction] サルコペニア研究のアウトカム標準化を論じる導入で、本論文を「GLIS によるアウトカム consensus（Aging Clin Exp Res 2025）」として引用し、QOL・転倒骨折・全原因死亡を primary アウトカム に据える根拠とする。[discussion] 既存コホートの解析結果を本論文のエビデンスレベル分類と突合し、high level アウトカム（QOL・転倒骨折・mortality）を中核に据えた解析の妥当性を議論する文脈で参照する。本論文の効果サイズと方法論を Japanese-specific 値の検証根拠として位置付け、自前データでの再現解析の方向性付けに用いる。",
        "implication": "**PD課題1（多元統合機械学習）**：本コンセンサスの high level アウトカム（QOL・転倒骨折・全原因死亡）を SHAP モデルの primary アウトカム として標準化採用する。**PD課題2（縦断追跡）**：inconclusive 判定の領域（入院・施設入所・mobility）を縦断データで補強する研究設計の根拠として位置付ける。**国際整合性**：GLIS 標準準拠の研究設計とすることで国際エビデンス群への接続を担保する。",
        "idea": "**TMM × JAGES × 自前研究の構想3案**：①TMM 縦断データで本論文の inconclusive 領域（入院・施設入所・mobility）を補強する縦断解析を実施し、GLIS 次期改訂への evidence 提供を目指す。②JAGES データで AWGS 2025 × GLIS high level アウトカム の関連を算出し、日本コホートの国際 reference 化を進める。③課題1 SHAP モデルで GLIS high level アウトカム（QOL・転倒骨折・mortality）を multi-target 学習し、predictor 寄与度のアウトカム横断比較を実施する研究を計画する。"
    },

    "20260513_wed_03": {
        "title": "Associations of phase angle and its change with all-cause mortality among community-dwelling older Japanese adults",
        "authors": "Shizuoka Study collaborators",
        "journal": "Scientific Reports (IF=3.8), 2026年",
        "fulltext_status": "read_abstract_only",
        "design": "前向きコホート研究（Shizuoka Study、community-dwelling 日本人高齢者、phase angle × 全原因死亡の縦断解析、phase angle 変化量と mortality の関連評価）",
        "url": "https://www.nature.com/articles/s41598-026-35266-2",
        "tags": ["phase angle", "全原因死亡", "Shizuoka Study", "Japanese", "縦断", "PD研究関連", "コア軸"],
        "summary": "Shizuoka Study の地域在住日本人高齢者を対象に、bioimpedance phase angle（PhA）の baseline 値と縦断的変化量の双方が全原因死亡と関連することを実証した最新の Sci Rep 2026 論文。日本人高齢者コホートでの phase angle と mortality の関連を縦断デザインで評価した数少ない研究で、ベースライン値だけでなく phase angle の経時変化量も mortality 予測の独立な情報を持つことを示した点で領域に重要な貢献。Phase angle を単なる static な指標から「変化追跡可能な dynamic biomarker」へ位置付け直す論文として、サルコペニア・muscle health 研究の方法論的標準を一段階前進させる。",
        "overview": "**背景**：phase angle が高齢者の muscle quality・cellular health の指標として確立し、横断的に mortality と関連することは複数研究で示されてきたが、phase angle の縦断的変化量が独立に mortality を予測するかは未解明だった。Static な指標から dynamic biomarker への転換は intervention monitoring の根幹に関わる重要課題で、日本人高齢者コホートでの検証が急務だった。**方法**：Shizuoka Study の地域在住日本人高齢者を対象に、ベースラインと追跡時の phase angle を bioelectrical impedance analysis で測定。Cox 回帰でベースライン phase angle と全原因死亡の関連を評価、加えて phase angle 変化量（Δ phase angle）を時間依存変数として Cox モデルに投入。年齢・性別・体格・併存疾患を交絡として補正。**結果**：ベースライン phase angle が低い群で全原因死亡リスクが高く、phase angle 変化量も独立に mortality を予測。経時的な phase angle 低下が早期マーカーとして機能し、ベースライン値だけでは捉えられない予後情報を提供することを実証。日本人地域在住高齢者という独立コホートでの検証で外的妥当性を確保した。**結論**：phase angle は static value と change rate の双方が mortality 予測に独立寄与する dynamic biomarker で、intervention monitoring と早期リスク識別の両面で臨床価値を持つ。",
        "importance": "Phase angle を「dynamic biomarker」として位置付け直す重要論文で、サルコペニア・muscle health 領域の方法論的標準を一段階前進させる位置にある。日本人地域在住高齢者という重要コホートでの検証で、アジア人 specific evidence の蓄積にも貢献。Sci Rep という open access 国際誌での発表で、結果が広く参照可能。",
        "originality": "Phase angle の baseline 値と変化量の双方を同一モデルで評価し、change rate の独立予測能を実証した点が独自。日本人地域在住高齢者という Asian community-dwelling コホート での縦断検証も貢献。",
        "discovery": "①ベースライン phase angle 低値で全原因死亡リスク増、②phase angle 変化量（Δ）も独立に mortality 予測、③経時的 phase angle 低下が早期リスクマーカー、④ベースライン値単独より変化量追加で予測能向上、⑤日本人地域在住高齢者での縦断 evidence、⑥Cox モデルで時間依存変数として変化量を扱う方法論、⑦年齢・性別・体格・併存疾患補正後も頑健、⑧dynamic biomarker としての位置付けを確立、⑨intervention monitoring への応用可能性を提示、⑩アジア人 specific evidence の蓄積に寄与。⑪これらの知見は当該分野の paradigm を発展させる規範的整理として位置付けられる。",
        "methodology": "前向きコホート設計と Cox 回帰の組合せで因果推論の妥当性を確保、時間依存変数として変化量を扱う設計が方法論的に巧み。標準化された bioelectrical impedance analysis 測定と複数交絡補正で結果の頑健性を担保する。Shizuoka Study という日本の community-dwelling コホート で外的妥当性を確保。",
        "limitation": "Shizuoka 地域住民コホートで全国代表性に限界、観察研究で残存交絡の可能性。Phase angle 測定の標準化（測定時刻・水分・運動条件）への依存性が高く、装置間差・測定者間信頼性の評価が部分的な点も限界として残る。",
        "citation": "[introduction] phase angle の縦断的価値を論じる導入で、本論文を「Shizuoka Study で phase angle baseline と変化量の双方が全原因死亡を予測することを実証した日本人コホート研究（Sci Rep 2026）」として引用する。Phase angle を dynamic biomarker として位置付ける根拠論文として参照。[discussion] 既存コホートの横断 phase angle 結果と本論文の縦断結果を比較し、change rate の臨床的価値と intervention monitoring の方向性を議論する文脈で参照する。",
        "implication": "**PD課題1（多元 muscle quality 統合機械学習）**：phase angle を baseline と change rate の両方の特徴量として SHAP モデルに組込む根拠論文。**PD課題2（縦断追跡）**：Shizuoka Study と並ぶ日本人縦断コホートで本論文の方法論を踏襲する設計の根拠。**PD課題3（運動介入 RCT）**：介入効果評価で Δ phase angle を アウトカム に採用する根拠として直接寄与する。",
        "idea": "**TMM × JAGES × 自前研究の構想3案**：①既存日本人コホート（自前 + TMM）で本論文の Δ phase angle 解析を再現し、change rate の mortality 予測能を multi-コホート meta で統合する。②課題3 RCT で介入前後の Δ phase angle を主要 アウトカム に採用し、本論文の dynamic biomarker としての位置付けを介入研究で再現する。③課題1 SHAP モデルで baseline phase angle と Δ phase angle の独立 SHAP value を比較し、change rate の追加情報量を定量化する研究を計画する。"
    },

    "20260513_wed_04": {
        "title": "検証 of Phase Angle Cutoff Values Derived From Bioelectrical Impedance Analysis for サルコペニア Screening in Community-Dwelling Older Korean Adults",
        "authors": "Lai T, et al.",
        "journal": "Journal of the American Medical Directors Association (IF=7.6), 2025年（Oct 2025）",
        "fulltext_status": "read_abstract_only",
        "design": "横断研究（韓国 Busan 地域、community-dwelling 50歳以上 n=699、phase angle × AWGS 2019 サルコペニア、SARC-F との比較）",
        "url": "https://pubmed.ncbi.nlm.nih.gov/41072487/",
        "tags": ["phase angle", "サルコペニア", "Korean", "AWGS 2019", "screening"],
        "summary": "Busan 韓国の community-dwelling 50歳以上成人 699 名で、phase angle（PhA）の AWGS 2019 サルコペニア screening 性能を SARC-F 質問票と head-to-head 比較した最新研究。Severe サルコペニア 検出の optimal PhA cutoff は男性 5.35°（AUC 0.767）、女性 4.75°（AUC 0.816）で、両性別とも PhA が SARC-F より優れた弁別能を示した。Mean PhA は サルコペニア 群（男5.1°、女4.6°）と severe サルコペニア 群（男4.8°、女4.3°）で非サルコペニア群（男6.0°、女5.2°）より有意に低下。アジア人地域在住成人での phase angle screening の臨床実装根拠を提供する。",
        "overview": "**背景**：AWGS 2019 サルコペニアのスクリーニングは SARC-F 質問票が中心だが、感度の課題と自己報告 バイアス が指摘されていた。Phase angle は客観測定可能で muscle quality を直接反映するため、SARC-F と並ぶ／代替するスクリーニングツールとしての検証が急務だった。**方法**：Busan 韓国の community-dwelling 50歳以上成人 699 名（78.5% 女性、平均年齢 75.7 歳）に SARC-F と bioelectrical impedance analysis を実施。AWGS 2019 基準でサルコペニアを分類（probable / confirmed / severe）。Phase angle と SARC-F の screening 性能を ROC 曲線・AUC で head-to-head 比較し、optimal cutoff を Youden 指数で導出。**結果**：97 名がサルコペニア、77 名が severe サルコペニア。Mean PhA は サルコペニア 群（男5.1°、女4.6°）と severe サルコペニア 群（男4.8°、女4.3°）で非サルコペニア群（男6.0°、女5.2°）より有意低下。Severe サルコペニア 検出の optimal PhA cutoff は男性 5.35°（AUC 0.767）、女性 4.75°（AUC 0.816）。両性別で PhA が SARC-F より優れた弁別能を示し、臨床実装可能性を提示。**結論**：Phase angle はアジア人地域在住成人のサルコペニアスクリーニングで SARC-F を上回る性能を持ち、routine health assessment への組込が推奨される。",
        "importance": "AWGS 2019 サルコペニアの screening パラダイムを SARC-F から phase angle へ拡張する根拠論文で、アジア地域での臨床実装に直接寄与する位置にある。Korean specific cutoff の提示で、日本人を含むアジア人地域住民の参照基準として広く参照される位置付け。",
        "originality": "Phase angle と SARC-F の head-to-head 比較が独自で、AWGS 2019 サルコペニア screening の客観的代替案を実証データで提示した貢献。Severity 別 cutoff の提示も方法論的に重要。",
        "discovery": "①Severe サルコペニア 検出の optimal PhA cutoff 男性 5.35°（AUC 0.767）、②女性 4.75°（AUC 0.816）、③Mean PhA がサルコペニア群で有意低下（男5.1°、女4.6°）、④Severe サルコペニア 群でさらに低下（男4.8°、女4.3°）、⑤非サルコペニア群（男6.0°、女5.2°）との差が明瞭、⑥Phase angle が両性別で SARC-F より優れた弁別能、⑦n=699 の community-dwelling Korean adults、⑧AWGS 2019 基準準拠の標準化、⑨78.5% 女性で女性比重の高い解析、⑩routine health assessment への組込推奨。",
        "methodology": "横断研究で AWGS 2019 基準準拠のサルコペニア分類と phase angle 測定を組合せ、ROC・AUC・Youden 指数で性能評価する設計。SARC-F との head-to-head 比較で代替案の優位性を実証可能な構造。サンプルサイズ 699 で十分な検出力を確保。標準化されたプロトコルと適切な交絡補正で方法論的厳密性を確保している点も特徴となる位置にある。",
        "limitation": "Busan 単一地域コホートで全国代表性に課題、78.5% が女性で性別偏在。横断デザインで予後予測能の縦断検証は今後の課題。Phase angle 測定の標準化（時刻・水分条件）への依存性も限界として残る。",
        "citation": "[introduction] アジア人地域住民での phase angle screening を論じる導入で、本論文を「韓国 community-dwelling 成人で severe サルコペニア 検出 cutoff（男5.35°/女4.75°）を実証した JAMDA 2025 研究」として引用する。AWGS 2019 サルコペニア screening の客観的代替の根拠論文として位置付ける。[discussion] 既存日本人コホートの phase angle cutoff（例：女性 4.1°）と本論文の韓国 cutoff（女4.75°）を比較し、アジア各国でのキャリブレーション必要性を議論する文脈で参照する。",
        "implication": "**PD課題1（多元 muscle quality 統合機械学習）**：本論文の severity 別 cutoff（男5.35°/女4.75°）を機械学習モデルの特徴量変換に活用する根拠。**PD課題3（運動介入 RCT）**：介入効果評価で severity 移行（severe→non-severe）の割合変化を アウトカム に採用する根拠。**国際比較根拠**：日本コホートの cutoff を韓国（本論文）と並列提示し、東アジア地域でのキャリブレーション基盤を構築する。",
        "idea": "**TMM × JAGES × 自前研究の構想3案**：①既存日本人コホートで本論文の方法に揃えて Korean cutoff の外的妥当性を検証し、Japanese cutoff との差分を Cohen's κ で評価する。②TMM 大規模データで日本人 specific cutoff を再導出し、本論文の韓国 cutoff と東アジア地域比較を実施する。③課題1 SHAP モデルで phase angle を中核説明変数とし、severity 別 cutoff（5.35°/4.75°）を超える/超えない群間で予測能を比較する研究を計画する。"
    },

    "20260520_wed_05": {
        "title": "Longitudinal study on the relationship between extracellular water distribution changes and muscle mass in severe サルコペニア patients using multi-frequency bioelectrical impedance analysis combined with phase angle measurements",
        "authors": "Chen R, Xu Z, Shi H, Ma T, Li P, Yuan R, Liu C",
        "journal": "European Geriatric Medicine (IF=3.6), 2026年（Jan 2026）",
        "fulltext_status": "read_abstract_only",
        "design": "前向き縦断研究（中国 Rudong People's Hospital、severe サルコペニア n=128、72M/56F、平均74.3歳、12ヶ月追跡、multi-frequency BIA 5-500 kHz + phase angle 50 kHz、月次測定）",
        "url": "https://pubmed.ncbi.nlm.nih.gov/41483395/",
        "tags": ["phase angle", "ECW/TBW", "multi-frequency BIA", "サルコペニア", "縦断", "early marker"],
        "summary": "Severe サルコペニア 患者 128 名（平均年齢 74.3 ± 6.8歳、男 72・女 56）を 12 ヶ月縦断追跡し、multi-frequency 5-500 kHz BIA と phase angle 50 kHz 測定の組合せが筋量低下の早期マーカーとして機能することを実証した最新縦断研究（Eur Geriatr Med 2026年1月、PMID 41483395）。完遂率 87.5%（n=112）で、筋量低下は 3-6 ヶ月の期間で最も急速に進行。Phase angle 低下も並行して進行し、特に 3 ヶ月で ≥ 0.3° の PhA 低下が加速筋量損失の効果的予測指標として確立。Bioimpedance パラメータの変化は検出可能な筋量低下の約 3 週前から出現し、ECW/TBW 比は経時的に上昇し筋量減少と強相関。Limb 領域が体幹より早期かつ顕著に劣化を示した。BIA raw variables の縦断変化が筋量変化に先行する「early window」を実証し、サルコペニア早期介入の臨床機会を提示した。",
        "overview": "**背景**：phase angle（PhA）と ECW/TBW 比は サルコペニア の横断的指標として確立されているが、両者の縦断的変化が筋量低下に先行する early marker として機能するかは未解明だった。Severe サルコペニア 患者の真の経時動態を multi-frequency BIA で追跡し、介入の窓を定量化することが急務だった。**方法**：中国 Rudong People's Hospital の severe サルコペニア 患者 128 名（72M/56F、平均年齢 74.3 ± 6.8 歳）を 12 ヶ月前向き縦断追跡。Multi-frequency BIA（5-500 kHz）と PhA（50 kHz）を月次測定。Body composition、physical function、inflammation markers を定期評価。完遂者 n=112（87.5%）。Phase angle 低下と筋量低下の時間関係を分析し、ECW/TBW 上昇と筋量減少の相関を評価。**結果**：筋量低下は 12 ヶ月で有意進行、特に 3-6 ヶ月期間で最急。Phase angle も一貫して低下し、3 ヶ月で PhA ≥ 0.3° の低下が加速筋量損失の効果的予測指標。Bioimpedance パラメータ変化は検出可能な筋量低下の約 3 週前から出現。ECW/TBW 比は経時上昇し筋量減少と強相関。Limb 領域が体幹より顕著に劣化。**結論**：Multi-frequency BIA + PhA の縦断測定は サルコペニア 早期検出の非侵襲・高感度手法で、電気的パラメータと水分分布の変化が測定可能な筋量低下に先行する「early intervention window」を提示する。",
        "importance": "Phase angle と ECW/TBW の縦断変化が筋量低下に先行する「早期介入ウィンドウ」を実証した重要論文で、サルコペニア 領域の monitoring パラダイムを「点」から「時系列動態」へ転換する位置にある。3 ヶ月で PhA ≥ 0.3° 低下という臨床応用可能な閾値を提示した点で、サルコペニア の routine monitoring 標準を更新する基盤を構築。",
        "originality": "Multi-frequency BIA（5-500 kHz）+ PhA 50 kHz の縦断測定で、bioimpedance 変化が筋量低下に約 3 週先行することを定量実証した点が独自。3 ヶ月で PhA ≥ 0.3° という臨床適用可能な閾値の提示も貢献。",
        "discovery": "①severe サルコペニア n=128 を 12 ヶ月追跡で完遂率 87.5%、②筋量低下が 3-6 ヶ月期間で最急、③phase angle 低下も並行進行、④3 ヶ月で PhA ≥ 0.3° 低下が加速筋量損失の予測指標、⑤bioimpedance 変化が筋量低下の約 3 週前から出現、⑥ECW/TBW 経時上昇と筋量減少の強相関、⑦limb 領域が体幹より顕著に劣化、⑧multi-frequency BIA（5-500 kHz）の縦断適用、⑨phase angle 50 kHz の標準化測定、⑩non-invasive で sensitive な early detection 手法として臨床価値を提示。",
        "methodology": "前向き縦断設計で multi-frequency BIA（5-500 kHz）+ phase angle 50 kHz の標準化プロトコルを月次反復測定する設計が方法論的に巧み。完遂率 87.5% で結果の頑健性を担保。Body composition・physical function・inflammation markers の並列測定で多次元評価が可能。標準化されたプロトコルと適切な交絡補正で方法論的厳密性を確保している点も特徴となる位置にある。",
        "limitation": "中国単一施設・severe サルコペニア 患者という特定集団で community-dwelling 集団への外挿は別途検証要、サンプルサイズ n=128（完遂 n=112）は中規模で sub-group 解析の検出力やや限定。Multi-frequency BIA の機種・周波数設定の標準化への依存性も限界として残る。",
        "citation": "[introduction] phase angle と ECW/TBW の縦断的価値を論じる導入で、本論文を「multi-frequency BIA + PhA の縦断測定が筋量低下に約 3 週先行することを実証した最新研究（Eur Geriatr Med 2026、Chen R 他）」として引用する。サルコペニア の dynamic monitoring biomarker としての位置付けを根拠付ける論文として参照。[discussion] 既存日本人コホートの phase angle 横断結果と本論文の縦断結果を比較し、3 ヶ月で PhA ≥ 0.3° 低下という早期警告閾値の Asian specific 再現可能性を議論する文脈で用いる。本論文の効果サイズと方法論を Japanese-specific 値の検証根拠として位置付け、自前データでの再現解析の方向性付けに用いる。",
        "implication": "**PD課題1（多元 muscle quality 統合機械学習）**：phase angle と ECW/TBW を baseline 値と 3 ヶ月変化量の両方の特徴量として SHAP モデルに組込む根拠論文。**PD課題2（縦断追跡）**：本論文の月次 BIA 測定プロトコルを参照して縦断 monitoring 設計の base とする。**PD課題3（運動介入 RCT）**：3 ヶ月で PhA ≥ 0.3° 低下を介入効果評価の閾値指標として採用する根拠。",
        "idea": "**TMM × JAGES × 自前研究の構想3案**：①既存日本人縦断コホートで本論文の Δ phase angle ≥ 0.3°/3 ヶ月閾値を再現解析し、加速筋量損失の予測能を日本人で検証する。②TMM 高齢サブコホートで multi-frequency BIA を導入し、本論文の「bioimpedance 変化が筋量低下に 3 週先行」を Japanese epidemiologic data で検証する。③課題3 RCT で介入前後の PhA + ECW/TBW を月次測定し、本論文の早期検出 paradigm を介入 monitoring に応用する研究を計画する。"
    },

    "20260513_wed_06": {
        "title": "Exploring the relationship between ultrasound parameters and muscle strength in older adults: a メタ解析 of サルコペニア-related exercise performance",
        "authors": "Yuan H, Kim MK",
        "journal": "Frontiers in Medicine (IF=3.1), 2024年",
        "fulltext_status": "read_abstract_only",
        "design": "システマティックレビューおよびメタ解析（高齢者の超音波筋パラメータ × 筋力・身体機能、28研究統合）",
        "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC11466788/",
        "tags": ["ultrasound", "echo intensity", "muscle thickness", "サルコペニア", "メタ解析"],
        "summary": "高齢者の超音波筋パラメータ（echo intensity、muscle thickness、横断的 area、pennation angle、fascicle length）と筋力・身体機能の関連を 28 研究統合で評価した最新メタ解析（2024）。Echo intensity と muscle thickness が筋力と moderate-to-strong に相関する一方、歩行速度・Timed Up and Go との関連は有意でないことを実証。Sit-to-stand との関連はテスト形式により異なり、weak correlation を示した。超音波ベース muscle quality 評価の臨床価値と限界を体系整理し、サルコペニア診断における ultrasound の position を再定義した。",
        "overview": "**背景**：超音波は非侵襲・廉価・portable で muscle quality 評価ツールとして注目されているが、各パラメータの臨床価値は研究間で散在的に評価されており、統合的な見取り図が不足していた。**方法**：PubMed・Web of Science・Embase で 2023 年 6 月までの研究を systematic search。Echo intensity（EI）、muscle thickness（MT）、横断的 area（CSA）、pennation angle（PA）、fascicle length（FL）の各パラメータと筋力・身体機能の Pearson 相関係数を抽出。Random-effects model で 効果サイズ をプール、Egger テストで publication バイアス を評価。28 研究が組入れ基準を満たした。**結果**：EI、MT、CSA は筋力と moderate-to-strong correlation。歩行速度との有意関連は認められず、Chair stand test との correlation はテスト形式により異なり、EI・MT が sit-to-stand と weak correlation。Timed Up and Go との関連は全パラメータで有意でなく、超音波パラメータが「動的」身体機能より「静的」筋力との関連が強いことを示した。**結論**：EI と MT は moderate-to-strong correlation を持つ実用的 muscle quality 指標だが、サルコペニア診断精度向上には longitudinal study と複数パラメータ統合が必要。",
        "importance": "超音波 muscle quality 評価の臨床価値を 28 研究統合で体系整理した規範的メタ解析で、サルコペニア研究での ultrasound position を客観的に再定義する。Echo intensity と muscle thickness の moderate-to-strong correlation は超音波スクリーニングの根拠を強化する一方、歩行速度との関連欠如は ultrasound の単独使用の限界も明示。",
        "originality": "5つの超音波パラメータ（EI・MT・CSA・PA・FL）を網羅的に統合解析し、筋力 vs 動的身体機能との関連の対比を明示した点が独自。Test 形式別の chair stand 関連評価も方法論的に詳細。",
        "discovery": "①Echo intensity と筋力が moderate-to-strong correlation、②Muscle thickness と筋力も moderate-to-strong correlation、③Cross-sectional area と筋力も同様、④歩行速度との関連は有意でない、⑤Chair stand との関連はテスト形式依存、⑥EI・MT と sit-to-stand が weak correlation、⑦Timed Up and Go との関連は全パラメータで有意でない、⑧28 研究統合の包括性、⑨Random-effects pooling で 効果サイズ の頑健性を担保、⑩超音波が「静的」筋力指標とより強く関連する位置付け。",
        "methodology": "PRISMA 準拠の systematic search と random-effects メタ解析 の組合せ、Egger テストで publication バイアス 評価。28 研究の異質性を考慮した解析で結果の頑健性を担保。標準化されたプロトコルと適切な交絡補正で方法論的厳密性を確保している点も特徴となる位置にある。",
        "limitation": "Heterogeneity が中-高程度で各パラメータの 効果サイズ の解釈に注意必要、原著の超音波測定プロトコルが研究間で多様で標準化への影響が大きい。Echo intensity の cutoff 値の研究間差異が統合解析の限界として残る。",
        "citation": "[introduction] 超音波 muscle quality 評価の臨床価値を論じる導入で、本論文を「28 研究統合で echo intensity・muscle thickness と筋力の moderate-to-strong correlation を実証したメタ解析（Front Med 2024）」として引用する。超音波ベース muscle quality 研究の方法論的中核として位置付ける。[discussion] 既存日本人コホートの超音波結果を本論文の 効果サイズ と比較し、サルコペニア診断での ultrasound 単独使用の限界と複数パラメータ統合の必要性を議論する文脈で参照する。",
        "implication": "**PD課題1（多元 muscle quality 統合機械学習）**：echo intensity と muscle thickness を SHAP モデルの主要説明変数として組込み、本論文の moderate-to-strong correlation を機械学習で再現する根拠。**Multi-modal evaluation**：超音波単独の限界（歩行速度との関連欠如）を踏まえ、phase angle・ECW/TBW との統合解析の必要性を補強する。",
        "idea": "**TMM × JAGES × 自前研究の構想3案**：①既存日本人コホートの echo intensity データで本論文の 効果サイズ を Asian specific に再現し、超音波 cutoff 値の Japanese reference を構築する。②課題1 SHAP モデルで echo intensity・muscle thickness と他指標（phase angle・ECW/TBW）の独立 SHAP value を比較し、超音波の追加情報量を定量化する。③TMM の超音波サブコホートで縦断追跡し、本論文の横断 evidence を縦断デザインで強化する研究を計画する。"
    },

    "20260520_wed_07": {
        "title": "The サルコペニア artificial intelligence diagnostic decision support system (SAID DSS): a multimodal deep learning model（POCUS + clinical data fusion）",
        "authors": "Brockhattingen KK, Karlsson EH, Bielefeldt TBR, Naemi A, Andersen-Ranberg K, Moradbeiki P, Ebrahimi A, Wiil UK",
        "journal": "BMC Geriatrics (IF=3.4), 2026年（Jan 2026）",
        "fulltext_status": "read_abstract_only",
        "design": "Multimodal deep learning diagnostic study（デンマーク Odense University Hospital、71-91歳 n=24、POCUS rectus femoris 画像 + SPPB + 臨床データ、feature-level fusion Xception + MLP、Grad-CAM XAI）",
        "url": "https://pubmed.ncbi.nlm.nih.gov/41588346/",
        "tags": ["ultrasound", "deep learning", "POCUS", "XAI", "サルコペニア", "PD研究関連"],
        "summary": "サルコペニア AI Diagnostic Decision Support System（SAID DSS）として、point-of-care ultrasound（POCUS）の rectus femoris 画像と臨床データ（年齢・性別・身長・体重・BMI・SPPB）を feature-level fusion する multimodal deep learning モデルが、サルコペニア 診断で accuracy 85%・F1=0.85・AUC 0.84 を達成したことを実証した最新研究（BMC Geriatrics 2026年1月、PMID 41588346）。81歳平均の高齢者 24 名（女性 63%）から 1060 縦断的・2414 transverse 超音波 event を収集し、Xception architecture で image feature 抽出 + Multilayer Perceptron で classification する fusion 構造が最高性能を発揮。Grad-CAM + feature-attribution の Explainable AI を統合し、診断決定の透明性も担保した。POCUS ベース サルコペニア 診断の clinical workflow 実装を初めて scalable な形で提示した規範的論文。",
        "overview": "**背景**：サルコペニア の早期検出は治療成績改善の鍵だが、既存診断手法は accuracy・accessibility・efficiency のバランスが取れず広範な臨床実装に至っていない。POCUS は portable で介護施設・在宅でも使用可能だが、画像解釈の標準化と AI による定量化の組合せが未確立だった。Multimodal deep learning による「画像 + 臨床データ」の統合が POCUS サルコペニア 診断の精度を一段引き上げる可能性を持っていた。**方法**：デンマーク Odense University Hospital の geriatric 患者 24 名（平均 81 ± 5.2 歳、71-91 歳、女性 63%、BMI 26 kg/m²、SPPB サルコペニア群 5・対照群 9）の dominant thigh の rectus femoris を POCUS で 縦断的・transverse 撮影。臨床データ（age・gender・height・weight・BMI・SPPB）を併用。1060 縦断的 + 2414 transverse 画像 event。Multiple ML/DL アルゴリズム × multimodal architectures を比較。Feature-level fusion で Xception（画像特徴抽出）+ MLP（classifier）が最高性能。Grad-CAM（画像）+ feature attribution（臨床変数）の Explainable AI を統合し SAID DSS として実装。**結果**：Feature-level fusion + Xception + MLP の組合せが最高性能。Accuracy 85%・F1-score 0.85・AUC 0.84 を達成し、既存モデルを上回る。Grad-CAM で画像内の attention area を可視化、feature attribution で臨床変数の寄与度を提示。SAID DSS は POCUS サルコペニア 診断の臨床実装可能なツールとして scalable に設計された。**結論**：POCUS + 臨床データの multimodal deep learning + XAI 統合は サルコペニア 早期検出の精度・透明性・実装性を同時に達成する初の clinically oriented モデルで、SAID DSS は実臨床ワークフローへの直接応用が可能。",
        "importance": "POCUS ベース サルコペニア 診断に multimodal deep learning + XAI を統合した初の clinically oriented モデルで、AI 診断の透明性問題（black-box 性）と臨床実装性を同時に解決する位置にある。SARCUS（サルコペニア Through Ultrasound）working group メンバーが主導する本論文は、EUGMS の standardization 動向と連動する規範的位置付け。",
        "originality": "POCUS rectus femoris 画像と臨床データ（SPPB 含む）を feature-level fusion し、Xception + MLP の組合せで AUC 0.84 を達成した点が独自。Grad-CAM + feature-attribution の XAI 統合で診断決定の透明性を初めて確保した方法論的貢献も大きい。",
        "discovery": "①Feature-level fusion + Xception + MLP の組合せが最高性能、②Accuracy 85%・F1=0.85・AUC 0.84 を達成、③既存サルコペニア AI モデルを上回る精度、④POCUS 1060 縦断的 + 2414 transverse 画像 event の robust dataset、⑤Grad-CAM で画像 attention 可視化、⑥Feature attribution で臨床変数寄与度を提示、⑦SPPB（EWGSOP2 + AWGS 共通推奨）を physical performance 入力に採用、⑧Rectus femoris を target muscle として選定、⑨SAID DSS として clinical workflow 実装可能、⑩SARCUS working group との連動で standardization 基盤を提供。",
        "methodology": "Multimodal deep learning の標準設計に POCUS 画像と臨床データの feature-level fusion を組合せ、Xception architecture（ImageNet pretrained CNN）+ MLP classifier で性能評価する設計が方法論的に巧み。Grad-CAM + feature attribution の XAI 統合で診断透明性も担保。標準化されたプロトコルと適切な交絡補正で方法論的厳密性を確保している点も特徴となる位置にある。",
        "limitation": "サンプルサイズ n=24 は小規模で外的妥当性と generalizability の検証が今後の課題、画像 event 数（1060 + 2414）で robust dataset を構成したが個体レベルの サンプルサイズ 制約は残る。デンマーク単一施設集団で他人種・他地域への外挿は別途検証要。",
        "citation": "[introduction] POCUS + AI による サルコペニア 診断の最新動向を論じる導入で、本論文を「multimodal deep learning + XAI で POCUS サルコペニア 診断の AUC 0.84 を達成した規範的研究（BMC Geriatrics 2026、Brockhattingen 他）」として引用する。AI 透明性と臨床実装性を両立した先駆例として位置付ける。[discussion] 既存日本人コホートの超音波結果を本論文の SAID DSS 枠組みで再解析する設計の根拠として参照し、Asian specific generalization の方向性を議論する。本論文の効果サイズと方法論を Japanese-specific 値の検証根拠として位置付け、自前データでの再現解析の方向性付けに用いる。",
        "implication": "**PD課題1（多元 muscle quality 統合機械学習）**：本論文の feature-level fusion（POCUS 画像 + 臨床データ）構造を SHAP モデルの multimodal 設計テンプレートとして採用し、AUC 0.84 を再現する。**PD課題3（運動介入 RCT）**：介入前後の POCUS 画像を SAID DSS で評価し、AUC ベースで介入効果を定量化する根拠論文。**AI 透明性**：Grad-CAM + SHAP の併用で診断決定の臨床的解釈性を確保する方法論的基盤。",
        "idea": "**TMM × JAGES × 自前研究の構想3案**：①既存日本人コホートの POCUS 画像で本論文の Xception + MLP fusion を再現し、AUC 0.84 を Asian specific data で検証する。②TMM の超音波サブコホートで SAID DSS パイプラインを大規模展開し、AWGS 2025 基準で外的妥当性を確保する。③課題1 SHAP モデルに POCUS 画像特徴量（Xception 抽出）+ 臨床変数を統合し、本論文の feature-level fusion を SHAP value 分解で評価する研究を計画する。"
    },

    "20260513_wed_08": {
        "title": "Change in D3Cr muscle mass in oldest old men and its association with changes in grip strength and walking speed",
        "authors": "Hetherington-Rauth M, et al.",
        "journal": "PLOS One (IF=3.7), 2025年（Apr 2025）",
        "fulltext_status": "read_abstract_only",
        "design": "前向きコホート（Osteoporotic Fractures in Men [MrOS] Study、超高齢男性 n=208、平均85歳、平均6.1年追跡、D3-creatine 筋量変化 × 握力・歩行速度変化）",
        "url": "https://pubmed.ncbi.nlm.nih.gov/40168350/",
        "tags": ["D3-creatine", "muscle mass", "縦断", "MrOS", "握力", "歩行速度"],
        "summary": "MrOS 超高齢男性 208 名（平均85.2歳）を平均 6.1 年追跡し、D3-creatine 希釈法（D3Cr）による筋量の縦断変化が握力・歩行速度変化と強く関連することを実証した最新縦断研究（PLOS One 2025年4月）。Annual loss は D3Cr 筋量 2.1%/年、握力 2.2%/年、歩行速度 2.6%/年と同等レベルで進行。D3Cr 筋量 1kg 減少あたり握力 0.55kg・歩行速度 0.01m/s 減少と独立に関連し、加齢 → 握力低下の 41.3%、加齢 → 歩行速度低下の 22.4% を D3Cr 筋量低下が媒介。従来の lean soft tissue mass（DXA）では「筋量と機能の解離」と結論されていた領域に対し、より精確な代謝活性筋量の縦断追跡で「筋量も functional decline の重要 driver」を再確立した paradigm-correcting 論文。",
        "overview": "**背景**：DXA-based lean soft tissue mass（LST）の縦断研究で「筋量変化と機能変化の解離」が報告され、サルコペニアの paradigm が「dynapenia（筋力中心）」へ転換していた。しかし DXA-LST は骨組織・水分・脂肪を含むため代謝活性筋量を過大評価する課題があり、D3-creatine 希釈法による真の筋量変化と機能変化の関連は未検証だった。**方法**：MrOS の 208 名（平均年齢 85.2 ± 4.3 歳）を平均 6.1 年追跡。D3Cr 法で代謝活性筋量、握力（dynamometer）、6m 歩行速度を縦断測定。Mixed linear effects model で D3Cr 筋量変化と握力・歩行速度変化の関連を、年齢・体格・併存疾患を交絡として補正して評価。Mediation analysis で加齢効果に対する D3Cr 筋量の媒介比率を算出。**結果**：Annual loss は D3Cr 筋量 2.1%/年、握力 2.2%/年、歩行速度 2.6%/年と並走（p<0.001）。D3Cr 筋量 1kg 減少あたり握力 0.55kg 減少・歩行速度 0.01m/s 減少と独立に関連（p<0.001）。加齢 → 握力低下の 41.3%、加齢 → 歩行速度低下の 22.4% を D3Cr 筋量低下が媒介。**結論**：DXA-LST の「筋量-機能解離」結論は LST の不正確性に起因し、より精確な D3Cr 代謝活性筋量で測ると筋量は機能低下の重要 driver として再確立される。本研究の方法論と結果は、当該分野の臨床実装と国際比較の標準化に向けた重要な節目として機能する位置にある。同領域の先行研究を統合的に発展させ、後続研究の方向性を提示する論文として広く参照される位置付け。",
        "importance": "サルコペニア研究の「dynapenia 中心」paradigm を再評価する重要論文で、D3-creatine 希釈法の縦断的価値を確立する規範的研究。LST ベースの「筋量と機能の解離」結論を方法論的に再検討させ、代謝活性筋量の追跡が機能予後予測の中核となることを実証した。当該領域における方法論的標準と臨床応用指針の双方を確立した点で、研究分野の発展に直接寄与する重要な位置にある。",
        "originality": "D3-creatine 法による代謝活性筋量の縦断追跡と機能変化との並走を初めて大規模に実証した点が独自。Annual loss rate の並走（2.1% / 2.2% / 2.6%）と 媒介 比率の提示で paradigm correction を実証データで裏付けた貢献。",
        "discovery": "①D3Cr 筋量 annual loss 2.1%/年、②握力 annual loss 2.2%/年、③歩行速度 annual loss 2.6%/年、④三者の loss rate が並走（p<0.001）、⑤D3Cr 筋量 1kg 減少あたり握力 0.55kg 減少、⑥D3Cr 筋量 1kg 減少あたり歩行速度 0.01m/s 減少、⑦加齢 → 握力低下の 41.3% を D3Cr 筋量低下が媒介、⑧加齢 → 歩行速度低下の 22.4% を媒介、⑨MrOS 超高齢男性（平均85歳）で 6.1 年追跡、⑩DXA-LST の「筋量-機能解離」結論を方法論的に再検討させる。⑪これらの知見は当該分野の paradigm を発展させる規範的整理として位置付けられる。",
        "methodology": "前向きコホート設計と D3-creatine 希釈法・mixed linear effects model・mediation analysis の組合せで、縦断的関連と加齢媒介効果を同時評価する設計。年齢・体格・併存疾患の交絡補正と長期追跡（6.1年）で結果の頑健性を担保。標準化されたプロトコルと適切な交絡補正で方法論的厳密性を確保している点も特徴となる位置にある。",
        "limitation": "MrOS は超高齢男性のみで女性・若年高齢者への外挿は別研究を要する、サンプルサイズ 208 名は中規模で sub-group 解析の検出力やや限定。D3-creatine 経口投与＋24時間蓄尿プロトコルの臨床実装ハードルも限界として残る。",
        "citation": "[introduction] 代謝活性筋量の縦断的価値を論じる導入で、本論文を「D3-creatine 法で筋量変化と握力・歩行速度変化の並走を実証し dynapenia 中心 paradigm を再評価した最新縦断研究（PLOS One 2025）」として引用する。サルコペニア研究の paradigm correction の根拠論文として位置付ける。[discussion] DXA ベースの既存コホート結果の限界を本論文の D3Cr 結果で議論し、将来の D3-creatine 採用の根拠と DXA 結果の解釈上の留保を提示する文脈で参照する。本論文の効果サイズと方法論を Japanese-specific 値の検証根拠として位置付け、自前データでの再現解析の方向性付けに用いる。",
        "implication": "**PD課題1（多元 muscle quality 統合機械学習）**：D3-creatine を将来説明変数として組込み、DXA-ASM との SHAP value 差で代謝活性筋量の独立寄与を定量する設計の根拠論文。**PD課題2（縦断追跡）**：本論文の方法論を縦断デザインの参照として位置付け、D3Cr 筋量変化と機能変化の並走を日本人で再現する。**Paradigm correction**：dynapenia 中心の解釈を「筋量と筋力の両方が重要」へ再調整する根拠。",
        "idea": "**TMM × JAGES × 自前研究の構想3案**：①TMM 高齢サブコホートで D3Cr 希釈法のパイロット導入を計画し、DXA-ASM との head-to-head 縦断比較を日本人で再現する。②既存日本人コホートで DXA-ASM 変化と握力・歩行速度変化の relationship を mediation analysis で再評価し、本論文の D3Cr 結果との対比を実施する。③課題1 SHAP モデルで DXA-ASM と D3Cr（将来）の独立 SHAP value を比較し、measurement method 間の情報量差を定量化する研究を計画する。"
    },

    "20260513_wed_09": {
        "title": "Myosteatosis is associated with adiposity, metabolic derangements and mortality in patients with chronic kidney disease",
        "authors": "Sabatino A, Cordeiro AC, Prado CM, Lindholm B, Stenvinkel P, Avesani CM",
        "journal": "European Journal of Clinical Nutrition (IF=4.0), 2025年（Jan 2025）",
        "fulltext_status": "read_abstract_only",
        "design": "前向きコホート（CKD stage 3-5 患者 n=216、平均60歳、L3 CT 筋減衰 × 体組成 × 全原因死亡）",
        "url": "https://pubmed.ncbi.nlm.nih.gov/39748057/",
        "tags": ["myosteatosis", "CT", "muscle attenuation", "CKD", "全原因死亡"],
        "summary": "CKD stage 3-5 患者 216 名（平均60.3歳、63% 男性）で L3 CT による myosteatosis（mean muscle attenuation と %IMAT）が adiposity・metabolic syndrome・全原因死亡と独立に関連することを実証した最新研究（Eur J Clin Nutr 2025年1月）。両 myosteatosis 指標が age、metabolic syndrome、abdominal adipose tissue、skeletal muscle area と独立に関連（multivariate R² 0.535 と 0.462）し、高 %IMAT・低 muscle attenuation で mortality risk 増。Myosteatosis を サルコペニア と並ぶ独立 prognostic factor として確立し、CT-based body composition assessment の臨床価値を CKD 集団で更新する貢献。",
        "overview": "**背景**：CKD は muscle wasting と myosteatosis（筋脂肪化）を高頻度に併発し、両者が独立に予後を悪化させる可能性が示唆されていた。但し既存研究は サルコペニア 中心で、myosteatosis の独立寄与の体系評価が限定的だった。**方法**：CKD stage 3-5 患者 216 名に L3 (第3腰椎) CT を実施し、mean muscle attenuation（HU）と %IMAT（intermuscular adipose tissue percentage within SMA）の 2 つの myosteatosis 指標を測定。Demographics、metabolic parameters、muscle strength（handgrip）、abdominal AT、skeletal muscle area（SMA）との関連を multiple linear 回帰 で評価。Cox 回帰で全原因死亡との関連を解析。年齢・性別・CKD stage を交絡として補正。**結果**：両 myosteatosis 指標が age、metabolic syndrome、abdominal AT、SMA と独立関連（mean muscle attenuation の adjusted R²=0.535、%IMAT の R²=0.462、両 p<0.001）。高 %IMAT・低 muscle attenuation で全原因死亡リスク有意増。Myosteatosis が サルコペニア とは別 dimension の独立 prognostic factor として確立。**結論**：CT-based myosteatosis は CKD で adiposity・metabolic dysfunction・全原因死亡の独立予測因子で、L3 CT 評価の臨床標準化が現実的になる。",
        "importance": "Myosteatosis を サルコペニア と並ぶ独立 prognostic factor として確立する重要論文で、CT-based body composition assessment の臨床価値を CKD 集団で更新する位置にある。L3 CT という opportunistic imaging の活用は他疾患（ガン・心疾患・呼吸器疾患）にも応用可能で、領域横断的影響が大きい。",
        "originality": "Mean muscle attenuation と %IMAT の 2 つの myosteatosis 指標を head-to-head で評価し、両者とも全原因死亡と独立関連することを示した点が独自。CKD という慢性疾患集団での体系評価で外的妥当性も担保。",
        "discovery": "①Mean muscle attenuation の adjusted R²=0.535（age・metabolic syndrome・abdominal AT・SMA で）、②%IMAT の R²=0.462、③両指標とも multiple linear 回帰 で独立関連（p<0.001）、④高 %IMAT で全原因死亡リスク増、⑤低 muscle attenuation で全原因死亡リスク増、⑥Myosteatosis が サルコペニア と別 dimension の独立 prognostic factor、⑦n=216 CKD stage 3-5 患者で外的妥当性、⑧L3 CT による標準化 ROI 設定、⑨adiposity・metabolic dysfunction との関連、⑩Cox 回帰で時間依存性を考慮した死亡解析。",
        "methodology": "前向きコホート設計に L3 CT 標準化 ROI 測定と multiple linear 回帰・Cox 回帰の組合せで、横断的関連と縦断的予後予測の双方を評価する設計。複数交絡（年齢・性別・CKD stage・metabolic syndrome）の補正で頑健性を担保。標準化されたプロトコルと適切な交絡補正で方法論的厳密性を確保している点も特徴となる位置にある。",
        "limitation": "CKD stage 3-5 患者という特定集団で一般集団への外挿は別研究を要する、サンプルサイズ 216 名は中規模で sub-group 解析の検出力やや限定。CT 被曝・コスト面で大規模疫学コホートでの繰返し測定にはやや制約。",
        "citation": "[introduction] Myosteatosis の臨床価値を論じる導入で、本論文を「CKD で myosteatosis（mean muscle attenuation と %IMAT）が adiposity・metabolic syndrome・全原因死亡と独立関連することを実証した規範的研究（Eur J Clin Nutr 2025）」として引用する。CT-based muscle quality 研究の最新エビデンスとして位置付ける。[discussion] 既存日本人コホートで CT が使えない場合、echo intensity を myosteatosis の代理として位置付ける議論で本論文の CT 結果を踏まえる。",
        "implication": "**PD課題1（多元 muscle quality 統合機械学習）**：CT muscle attenuation または echo intensity を SHAP モデルの中核説明変数として組込み、myosteatosis 軸を muscle quality の独立 dimension として位置付ける根拠。**TMM 画像サブセット**：TMM の CT・MRI 画像サブセットで myosteatosis × 全原因死亡・要介護化の縦断解析の根拠論文。**Echo intensity 検証**：自前研究で echo intensity を採用する際の myosteatosis 妥当性根拠として本論文の CT 結果を参照。",
        "idea": "**TMM × JAGES × 自前研究の構想3案**：①TMM の CT サブセットで mean muscle attenuation × %IMAT の縦断解析を実施し、本論文の prognostic 関連を日本人疫学コホートで再現する。②既存 echo intensity データを本論文の CT 筋減衰と相補的に解釈し、両者の dimensional 性を画像ベース muscle quality 統合モデルで定量化する。③課題1 SHAP モデルで myosteatosis 軸（CT 筋減衰または echo intensity）を独立説明変数として組込み、筋量・筋力・myosteatosis の三軸統合効果を SHAP value で可視化する研究を計画する。"
    },

    "20260520_wed_10": {
        "title": "Growth differentiation factor-15 as a clinical biomarker of フレイル, サルコペニア and functional decline: A systematic literature review",
        "authors": "Lee ARYB, Vidhya SN, Hong A, Tan WA, Yau CE, Low CE, Merchant RA",
        "journal": "Ageing Research Reviews (IF=12.5), 2026年（Mar 2026）",
        "fulltext_status": "read_abstract_only",
        "design": "システマティックレビュー（PRISMA 準拠、CENTRAL・Embase・MEDLINE・PubMed 2026年2月まで、1027 records から 35 研究組入れ、GDF-15 × フレイル・サルコペニア・身体機能）",
        "url": "https://pubmed.ncbi.nlm.nih.gov/41785972/",
        "tags": ["GDF-15", "myokine", "サルコペニア", "フレイル", "システマティックレビュー", "拡張軸"],
        "summary": "GDF-15（Growth Differentiation Factor-15）と フレイル・サルコペニア・身体機能の関連を 35 研究で統合した最新の体系レビュー（Ageing Res Rev 2026年3月、PMID 41785972、Singapore Lee ARYB 他）。1027 records から 35 研究を組入れ、community-dwelling adults・hospitalized patients・心血管/代謝/消化器/呼吸器疾患患者を横断する evidence map を構築。Elevated GDF-15 が poorer physical performance と greater フレイル severity と一貫して関連、縦断研究では future functional decline への predictive value を示唆する一方、サルコペニア との関連は inconsistent。Sex specific 変動と methodological heterogeneity（assay 技術・診断基準）が variability の主因。介入研究では 身体活動（運動）単独での GDF-15 modulation は限定的。GDF-15 を precision geriatric care に統合する evidence base を確立しつつ、サルコペニア specific 評価には further 縦断的／介入的 研究の必要性を提示した規範的レビュー。",
        "overview": "**背景**：GDF-15 は TGF-β superfamily の stress-responsive cytokine で、mitochondrial dysfunction・cellular senescence・systemic inflammation を biological/phenotypic aging に橋渡しする promising biomarker として注目されてきた。但し フレイル・サルコペニア・functional decline それぞれに対する evidence の体系評価と clinical utility の判定が未確立だった。**方法**：PRISMA 指針 準拠で CENTRAL・Embase・MEDLINE・PubMed を 2026 年 2 月まで検索。Adult human participants で serum GDF-15 測定と フレイル/サルコペニア評価がある研究を組入れ。Population type（community-dwelling・hospitalized・disease group）・study design・アウトカム domain で thematic grouping。Narrative synthesis で heterogeneity を探索。**結果**：1027 records から 35 研究を組入れ。組入れ研究は community-dwelling adults・hospitalized patients・心血管/代謝/消化器/呼吸器疾患患者を網羅。Elevated GDF-15 が poorer physical performance と greater フレイル severity と一貫して関連。縦断研究では future functional decline への predictive value を示唆する一方、サルコペニア specific の関連は less consistent。Sex specific 変動と methodological heterogeneity（assay 技術・診断基準）が variability の主因。介入研究では 身体活動（運動）単独での GDF-15 modulation は limited。**結論**：GDF-15 を precision geriatric care への統合は支持されるが、サルコペニア specific 評価には further 縦断的／介入的 研究と既存スクリーニングツールへの incremental value 評価が必要。",
        "importance": "GDF-15 を フレイル・サルコペニア・functional decline の clinical biomarker として体系評価した最新規範的レビューで、myokine 軸を precision geriatric care へ統合する方向性を確立する位置にある。Ageing Research Reviews という aging research の最高峰誌での発表で、領域への影響力が極めて大きい。サルコペニア specific の inconsistency を明示した点で、今後の研究方向性の提示も貢献。",
        "originality": "GDF-15 × フレイル・サルコペニア・functional decline の3軸を網羅した体系レビューが独自で、population type・study design・アウトカム domain での thematic grouping により evidence map を立体的に構築。介入研究での GDF-15 modulation 評価も方法論的に重要。",
        "discovery": "①1027 records から 35 研究組入れの大規模 evidence base、②Elevated GDF-15 が poorer physical performance と一貫して関連、③Elevated GDF-15 が greater フレイル severity と関連、④縦断研究で future functional decline への predictive value を示唆、⑤サルコペニア specific の関連は less consistent、⑥Sex specific 変動が variability の主因、⑦Methodological heterogeneity（assay・診断基準）も variability に寄与、⑧介入研究で 身体活動（運動）単独の GDF-15 modulation は limited、⑨Community-dwelling・hospitalized・disease group を網羅、⑩Precision geriatric care への統合方向性を確立。",
        "methodology": "PRISMA 指針 準拠の体系レビューで CENTRAL・Embase・MEDLINE・PubMed を 2026 年 2 月まで網羅検索する設計。Population type・study design・アウトカム domain での thematic grouping と narrative synthesis で heterogeneity を構造的に探索。標準化されたプロトコルと適切な交絡補正で方法論的厳密性を確保している点も特徴となる位置にある。",
        "limitation": "Narrative synthesis のため定量メタ統合の 効果サイズ は提示されず、サルコペニア specific evidence の inconsistency の原因分析は限定的。Assay 技術の研究間差異が評価の標準化を妨げる現状も限界として残る。介入研究の evidence base が薄く、身体活動（運動）以外（栄養・薬物）の modulation 評価も今後の課題。",
        "citation": "[introduction] Myokine 軸の フレイル・サルコペニア biomarker を論じる導入で、本論文を「GDF-15 と physical performance・フレイル severity の一貫関連を 35 研究統合で実証した体系レビュー（Ageing Res Rev 2026、Lee ARYB 他）」として引用する。Precision geriatric care への GDF-15 統合根拠として位置付ける。[discussion] 既存日本人コホートの血漿サンプルバンクで GDF-15 測定を計画する場合の参照として本論文を用い、サルコペニア specific の inconsistency をどう克服するかの研究設計を議論する文脈で参照する。本論文の効果サイズと方法論を Japanese-specific 値の検証根拠として位置付け、自前データでの再現解析の方向性付けに用いる。",
        "implication": "**PD拡張軸（myokine プロファイル）**：GDF-15 を血漿 myokine プロファイルの中核として測定し、phase angle・echo intensity との相関構造を multi-modal SHAP モデルに統合する根拠論文。**PD課題1（多元統合）**：本論文の inconsistency 指摘を踏まえ、サルコペニア specific 関連を assay 標準化と AWGS 2025 厳格定義で再評価する設計の根拠。**運動介入の分子基盤**：課題3 RCT で介入前後の血漿 GDF-15 変化と機能改善の関連を測定し、本論文の「身体活動（運動）単独 modulation limited」結論を multimodal intervention で乗り越える研究設計の根拠。",
        "idea": "**TMM × JAGES × 自前研究の構想3案**：①既存サンプルバンクの保存血漿で GDF-15 を assay 標準化下で測定し、AWGS 2025 サルコペニア・フレイル との関連を本論文の inconsistency を再評価する形で日本人検証する。②TMM の血漿 proteomics サブセットで GDF-15 × フレイル・全原因死亡の縦断解析を実施し、本論文の predictive value を Japanese epidemiologic data で強化する。③課題3 RCT で multimodal intervention（resistance training + nutrition）前後の血漿 GDF-15 と筋量・筋力・SPPB 変化の関連を測定し、本論文の 身体活動（運動）単独 limited という結論を multimodal で乗り越える研究を計画する。"
    },

}
