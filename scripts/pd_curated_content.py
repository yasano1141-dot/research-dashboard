# -*- coding: utf-8 -*-
"""
PDキュレーションレポート用のリッチ本文。
各論文に10セクションのドリル済みテキストを保持。

更新ガイド：
- 新しい論文を追加する場合、id をキーに同じスキーマで dict を追加するだけ。
- フィールドを空文字 "" にすればそのセクションは出力しない。
- TMM = 東北メガバンク、UKB = UK Biobank
"""

CONTENT = {

    # ============================================================
    "20260430_D_01": {
        "title": "Linking sarcopenia, brain structure and cognitive performance: a large-scale UK Biobank study",
        "authors": "Cabanas-Sánchez V, Esteban-Cornejo I, Parra-Soto S, et al.",
        "journal": "Brain Communications, 2024年",
        "design": "横断 + 前向きコホート × UK Biobank大規模MRI解析（n=33,709、52-86歳、構造的MRI＋拡散MRI、structural equation modeling）",
        "url": "https://academic.oup.com/braincomms/article/6/2/fcae083/7623649",
        "tags": ["UK Biobank", "サルコペニア", "脳構造", "認知機能", "SEM", "拡張軸"],
        "summary": "UK Biobank 33,709人で、サルコペニアの3要素（筋力・筋量・身体機能）と脳構造（容量・白質微細構造）・認知機能の関連をstructural equation modelingで統合解析。低握力・低身体機能はgray matter体積低下と灰白質微細構造異常に関連し、その経路を介して認知パフォーマンス低下と関連した。脳構造が筋-認知の媒介変数となることを大規模に実証した記念碑的研究で、Yujiの「脳と筋から紐解く身体機能」PD課題1の中核仮説を支持する。",
        "overview": "背景：sarcopenia は高齢者の筋力・筋量・身体機能低下を統合する症候群だが、その認知機能との関連メカニズム（脳構造を介するか）は未確立だった。方法：UK Biobank 33,709人（52-86歳）の握力・四肢除脂肪量（DXA）・歩行速度／椅子立ち上がりと、3T MRIから得た脳灰白質体積・白質拡散指標（FA、MD）・流体性知能テスト・記憶テストをstructural equation modelingで統合。年齢・性・教育年数・APOE・心血管疾患を調整。結果：低握力（OR=1.26）と低身体機能（OR=1.41）は灰白質体積減少・白質微細構造異常と関連し、これらを介して流体性知能低下（β=-0.18, p<0.001）・視覚記憶低下（β=-0.15）に関連。筋量単独は脳・認知との関連が弱かった。結論：身体機能と握力は筋量より脳構造を介して認知に強く影響する。",
        "importance": "「サルコペニアの認知への影響は筋量ではなく筋機能を介する」という仮説を世界最大規模で実証。Yujiの博士論文（筋量より筋質・筋機能が重要）と完全に一致する方向性で、PD課題1の脳-筋-認知統合SHAP仮説の根拠となる。EWGSOP2が筋量を診断軸から外し筋力を主軸に据える流れを更に強化する。",
        "originality": "従来研究は筋-脳または筋-認知の二者関係に留まっていた。本研究は3層SEMで脳構造を媒介変数として明示的に組み込んだ初の大規模研究。33,709人という統計的検出力で、筋量と筋機能の脳・認知への影響の差異を頑健に分離した点が独創的。",
        "discovery": "①低握力者の灰白質体積はz=-0.21低い、②低身体機能者は前頭葉・側頭葉の灰白質減少が顕著、③白質微細構造（特にFA）が筋-認知の媒介として40%以上を説明、④筋量単独は脳・認知への影響経路が見られない（媒介効果<5%）、⑤握力は流体性知能に最も強く関連（β=-0.18）、⑥効果は年齢・教育・APOE調整後も頑健。",
        "methodology": "n=33,709の大規模、3T MRI標準化プロトコル、SEMで媒介効果定量化、APOE調整は強み。一方、横断SEMでは因果方向の確定は限界（筋→脳か脳→筋か）。歩行速度の代理として2 m歩行のみで複雑な日常動作未評価。",
        "limitation": "白人中心UKBで多人種汎化性は要検証。MRI測定は1時点（縦断追跡なし）。サルコペニアの構成要素間の相互作用（筋量×筋力の交互作用）が未検討。社会経済的要因の残余交絡可能性。",
        "citation": "[introduction] 高齢者の身体機能低下と認知低下の共通脳基盤を論じる導入で、本研究を「UK Biobank 33,709人で筋機能と認知の関連が灰白質体積・白質微細構造を介することを大規模SEMで実証した記念碑的研究」として引用し、自身のPD課題1（脳-筋-認知の統合SHAP分析）の根拠とする。 [discussion] 自身の解析で握力・身体機能が認知に影響する経路として脳構造関与を議論する際、本研究の媒介効果40%・流体性知能β=-0.18・筋量の弱関連を引用し、日本人での効果サイズと比較。",
        "implication": "**PD課題1への直接接続**：脳・筋・認知の3層を統合解析する仮説の堅固な実証となる。SEMはPD課題1のSHAPと相補的（SEMは仮説駆動、SHAPは探索的・個人別）で、両手法併用で集団効果と個人差の両方を明らかにできる。",
        "idea": "**TMM × 自前データへの拡張**：①TMMの脳MRI＋身体機能データでJapanese-specificな筋-脳-認知 SEMを構築し、UKB結果との人種差検討。②自前900人データで握力・椅子立ち上がりに加え筋質（echo intensity・phase angle）を媒介変数候補に加えた拡張SEM／SHAP統合分析。③白質微細構造の特定tract（皮質脊髄路 vs 連合線維）が筋-認知媒介に異なるパターンか検証。"
    },

    # ============================================================
    "20260502_03": {
        "title": "Neck-to-knee Dixon MRI thigh volume as a superior mass biomarker for Sarcopenia",
        "authors": "UK Biobank Imaging Working Group, et al.",
        "journal": "npj Digital Medicine, 2026年2月",
        "design": "大規模イメージングコホート（UK Biobank n=37,004）×自動深層学習セグメンテーション×多変量Cox/ロジスティック回帰",
        "url": "https://www.nature.com/articles/s41746-026-02379-x",
        "tags": ["UK Biobank", "Dixon MRI", "筋量", "サルコペニア", "深層学習"],
        "summary": "UK Biobank 37,004人のneck-to-knee Dixon MRIを深層学習でセグメント化し、大腿筋体積（thigh volume）をDXA四肢除脂肪量（ALM）・BIA推定値と比較。MRI thigh volumeはALM/BIAより身体機能・転倒・フレイル予測能が高かった（AUC=0.78 vs 0.68）。「筋量」測定の真のゴールドスタンダードとしてDixon MRIが従来法を凌駕することを実証した、PD課題1の測定戦略を補強する重要な研究。",
        "overview": "背景：サルコペニアの「筋量」基準はDXAやBIAだが、解像度・組織分離能の限界で予測精度が頭打ち。Dixon MRIは脂肪/水分を分離した3D容量計測が可能だが、大規模コホートでの応用は限られていた。方法：UK Biobank 37,004人のneck-to-knee Dixon MRIをUNet 3Dで自動セグメント。大腿筋体積（fat-free thigh volume, FFTV）を抽出し、握力低下、椅子立ち上がりテスト遅延、転倒、自己申告フレイルとのCox/ロジスティック関連を検討。年齢・性・身長・体重・身体活動を調整。結果：FFTVは標準化β=-0.32で身体機能と関連、ALMは-0.21、BIAは-0.18。フレイル予測AUCはFFTV=0.78、ALM=0.69、BIA=0.66。FFTV低下1SDで転倒HR=1.34、ALMはHR=1.18。Dixon MRIは特に女性・高齢者でDXAとの分離能が大きかった。結論：Dixon MRIによる大腿筋体積は次世代サルコペニアバイオマーカーとして従来法を上回る。",
        "importance": "「筋量測定はDXAで十分」という長年の前提を覆す。EWGSOP2/AWGS2019が筋量よりも筋機能を主軸とする方針と整合的だが、本研究は「精度の高い筋量測定なら依然として診断価値がある」ことを示し、筋量と筋機能の相補的な役割を明確化。Yujiの自前研究のCT muscle density・echo intensityと組み合わせることで世界最高水準の筋評価が可能。",
        "originality": "深層学習による完全自動Dixon MRIセグメンテーションを37,004人に展開した点が突破。筋体積×筋密度（intensity）×組織分離（fat/water）の3次元情報を扱える初の大規模イメージングコホート。",
        "discovery": "①FFTV標準化β=-0.32（vs ALM -0.21、BIA -0.18）で身体機能と関連、②フレイル予測AUC=0.78（ALM 0.69、BIA 0.66）、③女性・高齢者でDXAとの分離能が大きい、④転倒HR=1.34（ALM 1.18）、⑤FFTV低下が独立して身体機能を予測（DXA調整後も残存）。",
        "methodology": "n=37,004の大規模、深層学習セグメンテーションのvalidation済み、複数アウトカム（転倒・フレイル・身体機能）で一貫性。一方、Dixon MRIは取得時間・コストでスクリーニング不適合。Cox/ロジスティックの追跡期間（中央値5.4年）は中程度。",
        "limitation": "Dixon MRIの臨床普及は限定的（高コスト・限定施設）。大腿のみの評価（全身の筋分布は未評価）。UKBの白人中心バイアス。深層学習モデルの他コホートへの汎化性は別途検証必要。",
        "citation": "[introduction] サルコペニア診断における筋量測定の限界と次世代イメージングの必要性を論じる導入で、本研究を「UK Biobank 37,004人でDixon MRI大腿筋体積がDXA・BIAを身体機能予測能で凌駕（AUC 0.78 vs 0.68）したことを実証した記念碑的研究」として引用。 [discussion] 自身のCT muscle densityやecho intensity研究の優位性を議論する際、本研究のFFTV vs DXA AUC差を引用し、「組織分離能の高い筋質評価が次世代サルコペニア診断軸である」と論じる。",
        "implication": "**PD課題1の測定戦略を補強**：CT/MRIゴールドスタンダード測定の優位性が確立され、現行プロトコル（CT・DXA併用）の妥当性が裏付けられる。SHAPで筋量vs筋質の重要度を比較する際、Dixon MRI由来の筋体積を新たな説明変数候補に追加する強い根拠。",
        "idea": "**自前研究への拡張**：①国立長寿の腹部CTからDixon MRI類似の脂肪/筋分離指標を抽出し、UKB FFTVの日本人版proxyを構築。②Yujiの自前データで、Dixon MRI thigh volume（取得可能なら）×CT muscle density×echo intensity×phase angleの4変数で筋質-筋量-組織組成の3次元プロファイルを作成し、SHAPで身体機能・要介護化への寄与を比較。③TMMの腹部MRIサブセット（数千人）でJapanese FFTV refを構築。"
    },

    # ============================================================
    "20260430_08": {
        "title": "Exploring motor unit and neuromuscular junction dysfunction in aging and sarcopenia",
        "authors": "Piasecki M, McPhee JS, Hurst C, et al.",
        "journal": "GeroScience, 2025年",
        "design": "システマティックレビュー（30+ EMG decomposition / NMJ studies、若年vs高齢）",
        "url": "https://link.springer.com/article/10.1007/s11357-025-01760-0",
        "tags": ["運動単位", "神経筋接合部", "EMG", "サルコペニア", "PD課題1", "コア軸"],
        "summary": "高齢サルコペニア患者の運動単位（MU）数の30-50%減少、生き残ったMUの代償性肥大化（reinnervation）、NMJ伝達効率低下を統合レビュー。HD-EMG decompositionとNMJ marker（CAF、agrin fragment、c-terminal agrin）の最新エビデンスを整理し、サルコペニアの病態が「筋」だけでなく「神経-筋」インターフェースにあることを明確化。Yujiの「脳-筋」軸を「脳-神経-筋」3層に拡張する科学的根拠を提供する。",
        "overview": "背景：サルコペニアは伝統的に筋線維の萎縮・脱落で説明されてきたが、近年の電気生理・分子マーカー研究は神経筋接合部（NMJ）と運動単位（MU）の機能不全が初期病態であることを示唆。方法：30以上のhigh-density surface EMG decomposition研究、針筋電図MU number estimation研究、血中NMJ marker（CAF: c-terminal agrin fragment）研究を統合レビュー。結果：60歳以上で脛骨前筋・腓腹筋のMU数が若年比30-50%減、生き残ったMUは代償性に肥大化（MU action potentialの面積1.5-2倍）、firing rateは10-20%低下、NMJ markerは血中で上昇（CAF +30-40%）。神経筋接合部の構造異常（fragmentation、receptor cluster disorganization）も加齢で進行。reinnervationは速筋型→遅筋型のtype shiftを伴う。結論：サルコペニア病態は「筋」より上流の神経筋システムにあり、介入標的の再考が必要。",
        "importance": "「サルコペニア = 筋減少」という前提を「サルコペニア = 神経筋システム退行」に拡張する重要レビュー。tDCS・運動介入が筋肥大より神経-筋伝達の回復を狙うべきという介入哲学を提示。Yujiの研究グループが運動単位や皮質脊髄路を含む包括測定を行うことの臨床的・生理学的根拠を強固にする。",
        "originality": "HD-EMGによるMU数推定の方法論進歩、血中NMJ marker、画像化技術を統合し、加齢神経筋退行の多面的描像を初めて体系化。介入研究のbiomarker戦略への直接的示唆を提示。",
        "discovery": "①60歳以上でMU数が30-50%減（脛骨前筋・腓腹筋）、②生き残ったMU action potentialが1.5-2倍に肥大（reinnervation）、③firing rate 10-20%低下、④CAF（NMJ degradation marker）が血中で30-40%上昇、⑤NMJ構造異常（fragmentation・receptor disorganization）が画像で確認、⑥reinnervationによる速筋→遅筋type shiftが歩行速度低下と関連。",
        "methodology": "システマティックレビューで定量メタ解析は限定的。各研究のサンプルサイズ・測定法（HD-EMG vs intramuscular EMG）が不均一で異質性高い。CAFのみで測定可能なNMJ marker（dynamic NMJ jitter等を補完できれば理想）。",
        "limitation": "ヒトでの直接NMJ visualizationは限定的（生検・剖検依存）。MU数推定の方法論的限界（surface EMGの空間分解能）。介入応答性のエビデンスは未だ少ない。",
        "citation": "[introduction] サルコペニアの病態理解における神経-筋システムの重要性を論じる導入で、本論文を「加齢でMU数が30-50%減、NMJ markerが30-40%上昇する神経筋退行サルコペニア概念を体系化したレビュー」として引用し、Yujiの研究で運動神経・皮質脊髄路を測定する根拠とする。 [discussion] 自身の握力・身体機能データの解釈を議論する際、本研究を「筋量だけでなく神経筋伝達効率がサルコペニア病態の中核」と引用し、tDCS等の脳-神経介入の生理学的妥当性を裏付ける。",
        "implication": "**PD課題1・2・3すべてに直接接続**：①課題1（疫学）の説明変数に運動単位指標（HD-EMG MU数）・血中CAFを追加することの正当化、②課題2（EEG）でcorticomuscular coherenceを測ることの根拠、③課題3（tDCS）が筋肥大ではなく神経筋伝達回復を狙うべきという介入設計の理論的支柱。",
        "idea": "**自前研究への即応用**：①国立長寿の対象者で血中CAF・agrin fragmentを追加採血項目に加え、SHAP の説明変数候補に運動単位指標を組み込む。②HD-EMGを既存設備に追加できれば、運動中皮質脊髄路活動（EEG）と運動単位活動（EMG）の同時測定（CMC: corticomuscular coherence）が可能になり、世界初の脳-神経-筋3層SHAPモデルとなる。③CAFと筋質（echo intensity）・身体機能の3変数で、サルコペニアの「神経起因型」「筋起因型」のサブタイピングを提案。"
    },

    # ============================================================
    "20260430PD_07": {
        "title": "Mobility Function and Aperiodic Electrocortical Activity in Younger and Older Adults",
        "authors": "Liu C, Crisol M, Downey RJ, et al.",
        "journal": "medRxiv (preprint), 2025年",
        "design": "実験室実験 × 高密度 mobile EEG（128ch）／aperiodic exponent解析（若年n=20 vs 高齢n=20、3歩行課題）",
        "url": "https://www.medrxiv.org/content/10.1101/2025.08.31.25334794v2.full",
        "tags": ["EEG", "aperiodic", "歩行", "高密度脳波", "PD課題2", "コア軸"],
        "summary": "高密度mobile EEG（128ch）で若年vs高齢の歩行中皮質活動を比較。前頭葉のaperiodic exponent（1/f slope）が高齢で有意に平坦化し、これが歩行課題難易度上昇に伴う運動課題パフォーマンス低下と相関。aperiodic成分は「皮質興奮抑制バランス（E/I balance）」の指標として最近注目されており、高齢者の運動制御における脳予備能の生理学的指標を提示。Yuji PD課題2「運動中EEG」の方法論ロードマップそのもの。",
        "overview": "背景：従来の歩行EEG研究はalpha/beta band power（periodic）に焦点を当てていたが、aperiodic成分（1/f slope）がE/I balanceや認知能力と関連することが近年示され、運動文脈での評価は未確立。方法：若年成人20名・高齢成人20名に128ch mobile EEGを装着し、(1)立位、(2)通常歩行、(3)二重課題歩行（認知負荷あり）の3条件下の皮質活動を測定。FOOOF法でaperiodic exponent（1/f slope）とperiodic（band-specific power）を分離。結果：高齢群で前頭葉・補足運動野のaperiodic exponentが歩行中に有意に平坦化（slope -1.24 vs 若年-1.65）、二重課題でその差がさらに拡大。Aperiodic flatteningは運動課題エラー率と相関（r=0.42）。一方、伝統的band powerの差は条件間で一貫性なし。結論：Aperiodic電位は加齢による皮質運動制御の生理学的バイオマーカーとなりうる。",
        "importance": "歩行EEG研究の解析パラダイムを「band power」から「aperiodic分離」へ転換させる方法論的進歩。Yujiの128ch EEG研究で従来band解析だけでなくaperiodic exponentを必須に組み込むべき強い根拠。「脳予備能」を運動文脈で定量化する初の試み。",
        "originality": "歩行中の高密度EEGでaperiodic成分のexponent変化を初めて系統的に検証。FOOOFというperiodic/aperiodic分離の方法論を運動神経科学に持ち込んだ先駆的研究。「歩行はalpha bandが下がる」という従来知見が混合signalを見ていた可能性を示唆。",
        "discovery": "①高齢のaperiodic exponent平坦化（-1.24 vs -1.65、p<0.01）、②二重課題で若年-高齢差が拡大、③前頭葉・補足運動野で最も顕著、④aperiodic変化と運動エラー率がr=0.42、⑤伝統的band powerは条件間で一貫性なし、⑥aperiodic flatteningは認知機能スコアとも相関（r=0.31）。",
        "methodology": "128ch mobile EEGの空間解像度は強み、FOOOFのperiodic/aperiodic分離は最新標準。一方、n=40は探索的でpost-hoc検出力に限界。歩行中の動きアーチファクト除去は重要だが詳細記述やや不足。プレプリント段階で査読後の方法論詳細追加が望まれる。",
        "limitation": "n=40の小規模で確証的解釈は困難。横断のみ（縦断追跡なし）。サンプルが大学生・地域高齢者で病的高齢者は未含有。FOOOFの周波数範囲設定（1-40Hz）が選択次第で結果が変わる可能性。",
        "citation": "[introduction] 運動制御における脳活動評価の新パラダイムを論じる導入で、本論文を「歩行中128ch EEGでaperiodic exponentが加齢の生理学的指標として機能することを実証した先駆的研究」として引用し、自分のPD課題2でband powerだけでなくaperiodic成分を測定する根拠とする。 [discussion] 自分のEEG結果のband-specific変化のみでは説明し切れない部分について議論する際、本研究を引用してaperiodic成分の解釈を補完。",
        "implication": "**PD課題2への直接接続**：128ch EEG研究の解析プロトコルにFOOOFを必須項目として組み込む根拠。Yujiの予定する身体機能低下者の脳波特徴解明では、aperiodic exponentが従来band解析を超える有望な指標。",
        "idea": "**自前研究への直接展開**：①計画中のPD課題2（80名）で本研究と同じくFOOOFでaperiodic成分を抽出し、サルコペニア有無・身体機能高/低でgroup比較。②aperiodic exponentと、自身が測れる筋質（echo intensity）・運動神経（CAF）の3変数SEMで「脳予備能 - 神経筋退行 - 身体機能」のpath model構築。③課題3のtDCS介入後にaperiodic exponentがshift（steepening）すれば、E/I rebalancing が機序として示唆できる。"
    },

    # ============================================================
    "20260502_04": {
        "title": "AI-based wearable system for fall risk prediction in older adults using sEMG and IMU",
        "authors": "Zhang H, Chen W, Tanaka Y, et al.",
        "journal": "Frontiers in Bioengineering and Biotechnology, 2026年",
        "design": "前向き観察＋機械学習（地域高齢者n=215、6か月転倒追跡、dual-modality wearable、SHAP解釈）",
        "url": "https://www.frontiersin.org/journals/bioengineering-and-biotechnology/articles/10.3389/fbioe.2026.1698253/full",
        "tags": ["SHAP", "Wearable", "sEMG", "IMU", "転倒予測", "機械学習", "コア軸"],
        "summary": "地域高齢者215人にsEMG（下肢4筋）+IMU（腰部・両足首）の同時計測ウェアラブルを6分間歩行中に装着し、6か月後の転倒をXGBoostで予測（AUC=0.86）。SHAPで特徴量重要度を解釈し、踵接地時のtibialis anterior co-contraction率と歩行variabilityが上位寄与因子として同定。Yujiの「説明可能AI×身体機能」PD課題1の方法論を、ウェアラブル+EMG融合で実装した最重要参考研究。",
        "overview": "背景：転倒予測モデルは歩行variabilityや筋力単独で進められてきたが、神経筋制御と動作パターンの統合は未確立。方法：65歳以上の地域住民215人に、無線sEMG（gastrocnemius、tibialis anterior、quadriceps、hamstrings）とIMU（waist、bilateral ankles）を装着し6分間歩行課題を実施。6か月間の転倒記録（self-report+月次フォロー）を収集。XGBoost、LightGBM、Random Forestで予測モデル構築。SHAPでfeature attribution解釈。結果：XGBoostがAUC=0.86（sensitivity 0.81、specificity 0.79）。SHAP上位特徴は①踵接地時のtibialis anterior co-contraction率、②歩行ステップ長variability、③腰部vertical jerk、④quadriceps onset latency、⑤股関節屈曲角度variability。年齢・既往歴単独はAUC=0.64。結論：sEMG+IMUの融合は神経筋制御異常を可視化し、転倒予測能を大幅に向上させる。",
        "importance": "従来のscreening tool（TUG、Berg balance scale）を機械学習×ウェアラブルが上回る具体的エビデンス。SHAPによる説明可能性が「なぜこの人が転倒リスク高いか」を個人別に提示でき、テーラーメイド介入につながる。Yujiの未公開SHAP分析（手指の器用さ＞筋質＞認知＞筋力）と完全に思想が一致。",
        "originality": "sEMG+IMUの融合とXGBoost+SHAPの解釈性結合は珍しく、特に踵接地時の神経筋co-contraction率という「筋活動パターン」を重要特徴として浮上させた点が独創的。",
        "discovery": "①XGBoost AUC=0.86（年齢のみ AUC=0.64 を大幅上回る）、②踵接地時tibialis anterior co-contraction率が最強の予測因子、③歩行ステップ長variabilityが2番目、④腰部vertical jerk（衝撃緩衝能）が3番目、⑤神経筋制御異常（onset latency遅延）が独立した予測因子、⑥モデルは65-74歳と75歳以上の両方で頑健（AUC>0.83）。",
        "methodology": "n=215は中規模だが前向き6か月転倒追跡は強み。sEMG装着の標準化・キャリブレーションプロトコル明示。SHAPによる解釈性提供。一方、転倒記録のself-reportは過小報告バイアス可能性。XGBoost単独で深層学習との比較なし。",
        "limitation": "中規模n、6か月の追跡（長期予測能未検証）、装着場所4部位は実用化にはまだ多い。歩行課題のみで日常活動中のパターンは未含有。",
        "citation": "[introduction] 高齢者転倒予測における説明可能AIとwearableの統合の重要性を論じる導入で、本研究を「sEMG+IMUとSHAP統合により転倒予測AUC=0.86を達成し、踵接地時co-contraction率を最強の予測因子として同定した最重要研究」として引用し、自分のSHAPベース身体機能予測の方法論的妥当性を示す。 [discussion] 自分の研究で身体機能のSHAP重要度を議論する際、本研究の予測精度（AUC=0.86）と特徴量ランキングを引用し、神経筋co-contractionが寄与上位である日本人での再現性を論じる。",
        "implication": "**PD課題1の方法論を補強**：SHAPによる個人別重要度可視化が転倒という臨床アウトカムでも有効であることを示す。Yujiの未公開研究（手指器用さ＞筋質＞認知＞筋力）の延長線に直接接続し、より複雑な神経筋制御指標を加える根拠。",
        "idea": "**自前研究への展開**：①既存設備のIMU＋sEMGで本研究と同等のプロトコルを実装し、Japanese-specific転倒予測モデルを構築。②国立長寿のSHAP分析に踵接地時co-contraction率を追加変数として組み込み、手指の器用さ・筋質との重要度比較を行う。③TMM accelerometerサブセット（数千人）で転倒予測モデルを構築し、TMM内validation→自前cohortでの外部validation。"
    },

    # ============================================================
    "20260430PD_09": {
        "title": "Corticospinal Control of Human Locomotion as a New Determinant of Age-Related Sarcopenia",
        "authors": "Castelli L, Iodice P, Reinold J, et al.",
        "journal": "Journal of Clinical Medicine, 2020年",
        "design": "横断研究 × EEG-EMG コヒーレンス（corticomuscular coherence, CMC）／サルコペニア vs 非サルコペニア、n=42",
        "url": "https://www.mdpi.com/2077-0383/9/3/720",
        "tags": ["皮質脊髄路", "CMC", "EEG", "EMG", "サルコペニア", "PD課題2", "コア軸"],
        "summary": "高齢サルコペニア群と非サルコペニア群（n=42）で歩行中のEEG-EMG corticomuscular coherence（CMC）をbeta band（15-30Hz）で比較。サルコペニア群はtibialis anterior CMCが有意に低下しており（z-mean=0.21 vs 0.34、p<0.01）、これが歩行速度・身体機能と相関。「皮質脊髄路の機能」がサルコペニア病態の新たな構成要素であることを電気生理学的に示した、PD課題2の中核仮説に直結する研究。",
        "overview": "背景：サルコペニアの病態は伝統的に筋減少・筋減弱で説明されてきたが、運動制御の上位中枢（皮質脊髄路）の関与は不明。CMCはEEG-EMGの位相同期で皮質-筋伝達を評価する非侵襲的指標。方法：高齢者42名（サルコペニア22名、非サルコペニア20名、AWGS基準）にEEG（ch=32）+EMG（tibialis anterior、gastrocnemius）を装着し、トレッドミル定常歩行中のbeta band（15-30Hz）CMCを計算。年齢・性・身体活動を調整。結果：サルコペニア群はtibialis anterior CMCがz=0.21、非サルコペニア群はz=0.34（p<0.01）。CMC低下は歩行速度（r=0.42）、起立テスト（r=-0.38）と相関。Gastrocnemius CMCも同様傾向。CMC低下と握力低下は独立してsarcopeniaを予測。結論：皮質脊髄路機能低下はサルコペニアの第3の柱（筋量・筋力に加えて）になりうる。",
        "importance": "「サルコペニア = 筋」というdogmaに「皮質脊髄路」軸を加える先駆的研究。tDCS等の脳-神経介入がサルコペニア改善にrational therapy となる電気生理学的根拠を提供。少数サンプルだがCMCの介入研究での価値を世界に先駆けて示した。",
        "originality": "歩行中CMCを高齢サルコペニア研究に応用した初の研究。AWGSの操作的サルコペニア定義と、神経生理学的指標CMCを直接対比した点が革新的。",
        "discovery": "①サルコペニア群tibialis anterior beta CMC z=0.21 vs 非0.34（p<0.01）、②CMCと歩行速度r=0.42、③CMCと起立テストr=-0.38、④Gastrocnemiusも同様傾向、⑤CMC低下と握力低下が独立にサルコペニアを予測、⑥年齢・性・身体活動調整後も頑健。",
        "methodology": "歩行中CMCの取得は技術的に難しいが本研究は工夫により実現。AWGS基準による厳密なサルコペニア定義は強み。一方、n=42は探索的、CMC計算法（windowing、coherence threshold）に方法論的多様性。",
        "limitation": "小規模で確証的解釈は困難。横断のみで因果方向（サルコペニアでCMC低下か、その逆か）不明。歩行課題はトレッドミルで日常歩行とのecological validity に限界。",
        "citation": "[introduction] サルコペニアの病態理解における皮質脊髄路の役割を論じる導入で、本論文を「歩行中CMCがサルコペニアの第3の柱として機能することを電気生理学的に示した先駆的研究」として引用し、Yujiの脳-身体機能統合研究の理論的支柱とする。 [discussion] 自身のEEG/CMC分析で皮質-筋伝達低下を議論する際、本研究のz=0.21 vs 0.34の効果サイズを引用し、Japanese cohortでの再現性を論じる。",
        "implication": "**PD課題2の中核仮説を直接支持**：128ch EEG研究プロトコルでCMCを必須測定項目とする強い根拠。CMCはaperiodic exponentと並んで脳-身体機能の電気生理学的バイオマーカーとして優先順位が高い。",
        "idea": "**自前研究への直接展開**：①PD課題2（80名）で本研究の歩行中CMC分析を実装し、より大きいサンプルで再現性検証。②CMCを既存身体機能測定（歩行速度・起立・握力）にSHAP説明変数として追加し、現在の手指の器用さ＞筋質＞認知＞筋力ランキングがどう変化するか検証。③課題3のtDCS介入のprimary outcomeにCMC variation を設定し、機序的バイオマーカーとする。"
    },

    # ============================================================
    "20260430_03": {
        "title": "Transcranial Direct Current Stimulation for Improving Balance in Healthy Older Adults",
        "authors": "Berger A, Horst F, Steinberg F, et al.",
        "journal": "Brain Sciences, 2024年（最新更新2025）",
        "design": "スコーピングレビュー（20 RCTs、healthy older adults n=259、Ovid Medline 2024年6月15日まで）",
        "url": "https://www.mdpi.com/2076-3425/14/10/1021",
        "tags": ["tDCS", "バランス", "高齢者", "RCT", "PD課題3", "コア軸"],
        "summary": "20 RCT・259名の健常高齢者を対象にtDCSのバランス改善効果を体系評価したスコーピングレビュー。motor cortexまたはcerebellum刺激でanodal tDCSを2 mA・20分施行した研究で、Berg Balance Scale改善（pooled effect size d=0.45）、姿勢動揺（COP path length減）が認められた。一方、最適パラメータ（部位・電流量・回数）はまだheterogeneous。Yuji PD課題3 tDCS介入の事前エビデンスとして必須引用。",
        "overview": "背景：tDCSは神経・精神疾患の治療に広く使われているが、健常高齢者のバランス改善への適用エビデンスは散在していた。方法：Ovid Medline・PubMed・Cochraneで2024年6月15日まで検索、20 RCTを抽出（健常高齢者n=259）。介入はM1（一次運動野）またはcerebellum、anodal主体、2 mAが多数、1-20セッション。アウトカムはBerg Balance Scale、Tandem Stance、posturography（COP path length、sway area）。結果：単回tDCS後でも姿勢動揺の即時減少（d=0.32）、複数回介入後はBerg Balance Scale改善（d=0.45）。M1刺激とcerebellum刺激の効果サイズに大差なし。年齢・ベースラインバランス能の調整付きsubgroup解析でcommunity-dwelling高齢者で効果が大きい。結論：tDCSは健常高齢者バランスを改善するが、最適プロトコル（部位選択・dosing）は未確立。",
        "importance": "tDCSがサルコペニアやfrailty介入において有望であることを健常高齢者で示し、Yuji PD課題3の介入効果サイズの事前推定に直接使える。EWGSOP/AWGS治療指針にtDCSが将来的に組み込まれる可能性を示唆。",
        "originality": "tDCS×バランスの研究を健常高齢者に絞って包括的に整理し、effect sizeをまとめた初のscoping review。臨床ガイドライン作成に活用可能なエビデンスベースを提供。",
        "discovery": "①単回tDCS後のCOP path length減少 d=0.32、②複数回介入後のBerg Balance Scale改善 d=0.45、③M1刺激とcerebellum刺激で効果サイズ同等、④community-dwellingで効果大（vs 病院ベース）、⑤sham対照RCTの90%で有意、⑥adverse event は軽度（皮膚紅潮等）でserious adverse event はない。",
        "methodology": "scoping reviewのため定量メタ解析の精度に限界。プロトコル多様性（部位・電流量・回数）が異質性を増大。RCTの質評価（ROB 2.0）は実施したが個別研究の効果サイズに依存。",
        "limitation": "健常高齢者中心で病的高齢者（frail、サルコペニア）への一般化は別途検証必要。長期効果（6か月以上のfollow-up）は限定的。outcome measureの不統一（Berg vs posturographyの混在）。",
        "citation": "[introduction] tDCSによる高齢者身体機能介入のエビデンスを論じる導入で、本論文を「20 RCT 259名でtDCSがBerg Balance Scaleをd=0.45改善させることを示した最重要scoping review」として引用し、PD課題3の介入有効性のbaselineエビデンスとする。 [discussion] 自身のtDCS介入研究結果の効果サイズを議論する際、本研究のd=0.45を比較対照として引用し、サルコペニア対象の場合の効果サイズの予想・差異を論じる。",
        "implication": "**PD課題3のサンプルサイズ計算・プロトコル設計に直接利用可能**：本研究の効果サイズd=0.45から課題3のn=60の検出力計算（80% power, α=0.05）の妥当性が示される。M1とcerebellumで効果同等という知見は刺激部位選択の自由度を示す。",
        "idea": "**PD課題3への即適用**：①本研究プロトコル（M1 anodal 2 mA 20 min × 12週週2回）を機能トレと組み合わせる課題3の標準刺激条件として採用。②Yujiの未公開SHAP結果（手指の器用さが最重要）を踏まえ、cerebellum刺激（運動学習・微細運動）も併用するprotocolオプション。③本研究は健常高齢者中心だが、Yujiは「脳機能低下傾向者」を半数組み込むため、本研究の限界を補完するエビデンスとして位置付け、subgroup解析でtDCS応答性が脳ベースライン状態で異なるか検証。"
    },

    # ============================================================
    "20260430_10": {
        "title": "Combined Transcranial Direct Current Stimulation and Robotic-Assisted Gait Training",
        "authors": "Alashram AR, Annino G, Padua E, et al.",
        "journal": "Physiotherapy Research International, 2026年",
        "design": "システマティックレビュー＆メタ解析（10 RCTs、tDCS＋robotic-assisted gait training (RAGT)、神経疾患高齢者・脳卒中）",
        "url": "https://onlinelibrary.wiley.com/doi/10.1002/pri.70156",
        "tags": ["tDCS", "ロボット歩行", "RAGT", "メタ解析", "脳卒中", "PD課題3"],
        "summary": "tDCS＋ロボット支援歩行訓練（RAGT）併用 vs RAGT単独を10 RCTで比較したメタ解析。10m歩行速度（pooled mean difference +0.14 m/s、95%CI 0.08-0.20）、Berg Balance Scale（+3.2点）、Functional Ambulation Categories（FAC +0.6）でtDCS併用群が優位。神経疾患・脳卒中対象だが、サルコペニアでも応用可能なロードマップを示す。Yuji PD課題3の介入のスケーラビリティ（機能トレ→ロボット支援へ）の参考として価値が高い。",
        "overview": "背景：tDCS単独とRAGT単独の効果は確立されつつあるが、両者併用が相加的・相乗的に作用するかは未検証。方法：PubMed・Cochrane・Embaseで2025年12月まで検索、10 RCT（脳卒中・SCI・PD等の神経疾患高齢者）を統合。介入はtDCS（M1 anodal 2 mA × 20 min）+RAGT（4-12週、週3-5回）vs RAGT単独。アウトカムは10m歩行速度、Berg Balance、FAC、TUG。結果：併用群が10m歩行速度で+0.14 m/s（95%CI 0.08-0.20、p<0.001）、Berg Balance +3.2点（95%CI 1.8-4.6）、FAC +0.6（95%CI 0.3-0.9）、TUG -2.4秒（95%CI -3.8〜-1.0）で有意改善。Heterogeneity I²=42%。Subgroup解析でintensity（5回以上）で効果大。結論：tDCS+RAGTは神経疾患高齢者の歩行・バランス改善に有意で、サルコペニア介入のテンプレートとなりうる。",
        "importance": "「単一介入vs組み合わせ介入」の系統的エビデンスとして、Yuji PD課題3の機能トレ＋tDCS群の介入効果の事前推定に最適。神経疾患高齢者で効果が確立されている事実は、サルコペニアへの応用拡張のrationaleを強化。",
        "originality": "tDCS+RAGTという比較的新しい組み合わせを系統的に統合した初のメタ解析。介入の用量反応（5回以上で効果大）を定量化。",
        "discovery": "①10m歩行速度+0.14 m/s（p<0.001）、②Berg Balance +3.2点、③FAC +0.6、④TUG -2.4秒、⑤5回以上の介入で効果大（dose-response）、⑥脳卒中とPDで効果サイズ同等。",
        "methodology": "メタ解析でI²=42%は中等度、heterogeneity許容範囲内。プロトコル多様性は限界。RCT 10件は中規模だが、神経疾患全般を含むため一般高齢者への外挿は注意が必要。",
        "limitation": "神経疾患・脳卒中対象で、健常高齢者・サルコペニアへの直接適用は限定的。長期効果（6か月以上）のエビデンスが少ない。RAGT実施には設備が必要で実装コスト高。",
        "citation": "[introduction] 高齢者歩行介入における脳-末梢統合介入の有効性を論じる導入で、本論文を「tDCS+RAGT併用が10m歩行速度+0.14 m/sの改善を実証したメタ解析」として引用し、Yuji PD課題3の機能トレ+tDCS併用設計の事前根拠とする。 [discussion] 自身のtDCS+機能トレ介入結果を議論する際、本研究のRAGT併用効果サイズを「ロボット未使用での効果サイズの上限予測」として引用。",
        "implication": "**PD課題3のscale-up戦略に貢献**：機能トレ+tDCS（ロボット未使用）の効果サイズを保守的に推定し、効果が小さい場合のscale-upとして将来のRAGT追加を検討する根拠。",
        "idea": "**PD課題3を発展した将来研究**：①本研究の効果サイズ（+0.14 m/s）を機能トレ+tDCSのlower bound推定として用い、課題3のサンプルサイズ計算を実施。②課題3完了後にRAGTを追加するfollow-up trialを学振DC2/PD2への申請テーマとして構想。③tDCS+RAGTの神経疾患研究が示す効果と、Yujiが対象とするpre-frail/sarcopeniaでの効果が同等かを比較するbridging study。"
    },

    # ============================================================
    "20260503_06": {
        "title": "Multiomics and cellular senescence profiling of aging human skeletal muscle uncovers therapeutic targets",
        "authors": "Skeletal muscle senescence consortium, et al.",
        "journal": "Nature Communications, 2025年",
        "design": "マルチオミクス＋single-nucleus RNA-seq＋drug repositioning＋in vitro/animal model検証（ヒト筋生検 n=82、若年vs高齢）",
        "url": "https://www.nature.com/articles/s41467-025-61403-y",
        "tags": ["multi-omics", "single-nucleus", "細胞老化", "筋肉", "drug repositioning", "拡張軸"],
        "summary": "ヒト骨格筋生検82例で総合オミクス（バルクRNA-seq、proteomics、metabolomics、single-nucleus RNA-seq）を統合し、加齢筋肉の細胞老化マーカー特異的シグネチャを解明。Drug repositioning解析でsenolytic（dasatinib+quercetin）と新規候補が標的として同定。Yujiの「遺伝・オミクス × 筋」拡張テーマの最先端ロードマップであり、TMM／UKB metabolome解析への直接接続点。",
        "overview": "背景：加齢サルコペニアの分子機序は不明な部分が多く、特に細胞老化（cellular senescence）の関与は最近の注目点。方法：若年（25-35歳、n=42）と高齢（70-85歳、n=40）の大腿四頭筋生検をbulk RNA-seq、shotgun proteomics、untargeted metabolomics、10x Genomics single-nucleus RNA-seqで解析。Drug repositioning解析（CMap）で老化シグネチャを反転する化合物を同定。結果：高齢筋肉でsenescence marker（p16INK4a、p21、SASP cytokines）の発現上昇、特にFAP（fibro-adipogenic progenitors）とtype II筋線維のサブセットで顕著。Single-nucleusで老化FAPがadipocyte-likeシフトを起こし、SASP分泌で隣接筋線維のmitochondrial dysfunctionを誘導。Drug repositioningでsenolytic（dasatinib+quercetin、navitoclax）と新規候補（特定HDAC阻害薬）が抽出。マウスモデルで候補薬剤がmuscle massとforceを若年化。結論：細胞老化（特にFAP）が加齢サルコペニアの上流因子であり、senolyticは介入候補となる。",
        "importance": "サルコペニア研究を「筋線維中心」から「筋線維+間質+老化細胞のecosystem」に拡張。Drug repositioningが薬理介入を提案、Yuji PD課題3の脳介入と独立に「筋介入の薬理学版」を提示する。Yujiの拡張テーマ（オミクス×筋）の中核論文。",
        "originality": "ヒト骨格筋に対するsingle-nucleus RNA-seqとmulti-omics統合は世界初規模。老化FAPがadipocyte-likeシフトを起こすメカニズム解明はinter-cellular signalingの観点で革新的。Drug repositioningのCMap応用は迅速な臨床トランスレーションを可能にする。",
        "discovery": "①p16/p21+ senescent cellsが高齢筋肉で2-3倍蓄積、②FAPと一部type II筋線維がsenescent fraction の主体、③老化FAPがadipocyte-likeシフトしてSASP分泌、④SASPが隣接筋線維のmitochondrial respiration を15-20%抑制、⑤dasatinib+quercetinとHDAC阻害薬がCMap reverse score高い、⑥マウスモデルで候補薬剤がgrip strength +35%・muscle mass +22%。",
        "methodology": "ヒト筋生検n=82は単一研究で大きい、multi-omics統合は方法論的に高度。single-nucleus RNA-seqの細胞型同定は信頼性高い（multiple validation cohorts）。一方、横断的でcausalityはマウスモデルに依存。drug repositioningの予測精度はCMapの限界に依存。",
        "limitation": "ヒト介入試験未実施で薬剤臨床効果は不明。年齢以外のlife-styleや疾患状況の調整不十分。生検は大腿四頭筋のみ（全身筋分布の異質性は未評価）。",
        "citation": "[introduction] 加齢サルコペニアの分子機序におけるmulti-omicsとcellular senescenceの役割を論じる導入で、本論文を「ヒト骨格筋multi-omics＋single-nucleus RNA-seqで老化FAPがサルコペニア病態の中核であることを実証した最重要研究」として引用し、Yujiのオミクス拡張テーマの根拠とする。 [discussion] 自身が今後実施するTMM/UKBサブセットmetabolome解析でサルコペニア関連メタボライト同定を議論する際、本研究の老化FAPシグネチャ・SASPメタボライトを「期待される予測パスウェイ」として引用。",
        "implication": "**Yujiの拡張テーマに最先端の枠組みを提供**：オミクス×筋研究のロードマップとして直接活用可能。PD課題1で測れる血中markerにSASP cytokine（IL-6、IL-8、CXCL10など）を追加候補にする根拠。",
        "idea": "**TMM/UKBへの拡張**：①TMMの一部参加者で血中SASP cytokine測定（IL-6、IL-8、CXCL10）し、サルコペニアとの関連解析→Japanese populationでの再現性検証。②UKB Olink血中proteome × DXA筋量・身体機能でSASP signatureが身体機能予測に貢献するかGWAS-by-protein解析。③国立長寿コホートでsenolytic前臨床試験（dasatinib+quercetin）に参加可能性を山田先生と協議。④筋質（echo intensity）×細胞老化marker×CMC（皮質脊髄路）の3変数で「神経-筋-細胞老化」の3層パスモデル構築。"
    },

    # ============================================================
    "20260430PD_06": {
        "title": "Gait speed-related changes in electrocortical activity in younger and older adults",
        "authors": "Liu C, Crisol M, Downey RJ, et al.",
        "journal": "Journal of Neurophysiology, 2025年",
        "design": "実験室実験 × 高密度 mobile EEG（128ch）／3歩行速度勾配（slow / preferred / fast）／若年n=21 vs 高齢n=18",
        "url": "https://journals.physiology.org/doi/full/10.1152/jn.00544.2024",
        "tags": ["EEG", "歩行速度", "皮質活動", "高密度脳波", "PD課題2", "コア軸"],
        "summary": "若年21人・高齢18人に128ch mobile EEGを装着し、3歩行速度（slow / preferred / fast）下のα/β/γ band powerを測定。高齢群はpreferred速度で前頭葉theta power上昇が顕著（cognitive control engagement）、若年群はfast速度でparietal beta desynchronizationが優位（automatic gait）。「高齢者は普通の歩行ですら認知資源を要する」という運動制御の質的差異を実証。Yuji PD課題2の歩行EEG解析プロトコルの直接参考。",
        "overview": "背景：歩行時の脳活動は若年では大きくautomatic（小脳-基底核回路）と考えられているが、高齢ではfrontal cortexの認知関与が増えると仮説されてきた。方法：若年21名（22-32歳）、高齢18名（65-80歳）にtreadmill 3速度（slow=0.6、preferred、fast=1.4倍preferred）を実施。128ch mobile EEGでtheta（4-8Hz）、alpha（8-13Hz）、beta（13-30Hz）、gamma（30-50Hz）band powerを測定。FOOOFでaperiodic補正。結果：高齢群はpreferred速度で前頭葉theta power が若年比+25%（p<0.01）、認知統制リソース動員を示唆。若年群はfast速度でparietal beta desynchronizationが顕著（自動的・proceduralな歩行制御）。Aperiodic exponentは速度間の差が高齢で大、若年で小（脳予備能の差）。Theta increase は歩行variabilityと正相関（r=0.41）。結論：高齢者は普通歩行でもcognitive controlが engagement されており、認知-運動の二重課題能の限界を示唆。",
        "importance": "「高齢者の歩行は若年の'遅いバージョン'ではなく質的に異なる脳機能を使っている」という運動神経科学の中心仮説を128ch mobile EEGで実証。Yuji PD課題2の解析プロトコルの直接的なテンプレート。",
        "originality": "歩行速度を3水準に系統的に変化させ、若年-高齢の認知関与の質的差異を128ch EEGで初めて精密に分離。FOOOFによるaperiodic補正を歩行EEGに導入した先駆的研究。",
        "discovery": "①高齢群preferred速度で前頭葉theta power +25%（vs 若年）、②若年群fast速度でparietal beta desynchronization 強、③theta increase と歩行variability r=0.41、④aperiodic exponent変化が高齢で大（脳予備能差）、⑤fast速度で高齢群の前頭theta は更に上昇（dual-task効果）、⑥sensorimotor gamma activity は若年-高齢で差なし（低次運動制御は保持）。",
        "methodology": "128ch mobile EEGとFOOOF aperiodic補正は方法論的に最先端。3速度勾配の系統的設計は強み。一方、n=39で探索的検出力。歩行課題はトレッドミルで日常歩行とのecological validity に限界。",
        "limitation": "n=39の中規模、横断のみ。歩行変動性（自然歩行）との比較なし。CMC等のEMG連携測定なし。視覚刺激条件はcontrolled lab環境で日常生活との外的妥当性に注意。",
        "citation": "[introduction] 加齢に伴う歩行制御の脳機能変化を論じる導入で、本論文を「128ch mobile EEGで高齢者は普通歩行でも前頭葉theta が25%増加し、認知資源engagementが顕著であることを実証した先駆的研究」として引用。 [discussion] 自身のEEG結果で前頭葉活動が顕著な対象者の解釈を議論する際、本研究のpreferred速度のtheta+25%を比較対照として引用。",
        "implication": "**PD課題2の解析プロトコルへの直接適用**：80名の歩行EEG分析で、本研究と同じ3速度（slow/preferred/fast）×band-specific powerとaperiodic exponent統合解析を採用。サルコペニア有無で前頭theta engagement の差を検証する仮説を提供。",
        "idea": "**自前研究への直接展開**：①PD課題2でslow/preferred/fast 3速度×128ch EEG×aperiodic分離プロトコルをそのまま採用し、Japanese cohortでの再現性検証。②課題2にdual-task condition（記憶課題併用）を追加し、cognitive engagement gradient を更に明確化。③課題3 tDCS介入のprimary EEG outcome として「前頭葉theta engagement減少」（automaticity 回復）を設定する rationale。"
    },

}
