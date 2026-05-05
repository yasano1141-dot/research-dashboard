# 研究者プロフィール（浅野優次郎）

毎回のレポート生成時、選定論文の「研究への示唆」「研究アイデア」セクションは必ずこのプロフィールと結びつけること。

## 所属・身分
- 筑波大学大学院 人間総合科学学術院 体育科学学位プログラム 博士後期課程
- 大藏研究室 D2（2025年度時点）
- 国立健康・栄養研究所（NIBIOHN）研修生
- 東北大学医工学研究科スポーツ健康科学分野 協力研究員（山田陽介研の関連）

## 主要な研究テーマ

### 1. 健康寿命（Healthspan / Disability-free life expectancy）
- 介護保険（LTCI: Long-Term Care Insurance）データの解析
- 要介護認定の発生・遷移を多状態モデル（multi-state model）で解析
- 健康寿命 vs 平均寿命のギャップ要因
- 自治体ごとの健康寿命格差

### 2. 身体機能（Physical function）
- mobility（移動能力）
- gait（歩行）— gait speed, gait variability, cadence
- balance（バランス）
- frailty（フレイル）— J-CHS基準、Frailty Index、Clinical Frailty Scale
- 10m歩行速度、Timed Up and Go (TUG)、Short Physical Performance Battery (SPPB)

### 3. 筋質（Muscle quality） — 主要関心領域
- **CT muscle density（CT筋密度）** — 大腿/腹部の筋実質密度
- **超音波 echo intensity（エコー輝度）** — 筋の脂肪浸潤評価
- **BIA phase angle（位相角）** — Bioelectrical Impedance Analysis
- **ECW/ICW ratio** — 細胞外水/細胞内水比、筋細胞健全性指標
- **D3-creatine dilution** — 筋量の絶対測定（次世代法）
- 既発表: BISによる筋質評価と身体活動の関連（CoDA解析、EJAP投稿予定）

### 4. 身体活動（Physical activity）
- leisure-time physical activity（余暇身体活動）
- social exercise（社会的運動）— 仲間と行う運動の介護予防効果
- 加速度計測定（Axivity AX3、ActiGraph）
- compositional data analysis (CoDA) — 24時間活動の組成分析

### 5. 認知機能・脳構造（Cognition & Brain）
- brain aging（脳老化）
- cognitive function — MoCA, MMSE
- brain structure — MRI volumetry, cortical thickness, white matter integrity
- DunedinPACNI、brain age clock

### 6. 遺伝子・オミクス（Genetics & Omics）
- GWAS（Genome-wide association study）
- epigenetic aging — DNA methylation, GrimAge, DunedinPACE
- UK Biobank データ
- Tohoku Medical Megabank データ
- polygenic risk score (PRS)

### 7. 方法論（Methodology） — 強い関心
- **g-formula** — 仮想介入効果の推定
- **marginal structural models (MSM)** — 時間依存的曝露・交絡
- **target trial emulation** — 観察データから仮想RCT構築
- **multi-state models** — 状態遷移（健常→要支援→要介護→死亡）
- **Mendelian randomization** — 遺伝子を操作変数とした因果推論
- **machine learning** — ランダムフォレスト、勾配ブースティング
- **SHAP (SHapley Additive exPlanations)** — 機械学習の解釈
- **CoDA (Compositional Data Analysis)** — 組成データ解析

## 共同研究者・関係者
- 筑波大学・大藏研究室（指導教官）
- 国立健康・栄養研究所（NIBIOHN）— 山田陽介、南里妃名子、村上晴香
- 早稲田大学 — 宮地元彦
- 東北大学医工学研究科スポーツ健康科学分野 — 山田陽介

## 研究アイデアの組み立て方（テンプレート）

論文の「研究アイデア」セクションでは、以下のパターンで日本コホートとの接続を示す：

### パターン1：日本コホートでの再現
> 「{研究内容}を{日本コホート名（JAGES、東北メディカル・メガバンク、JPHC-NEXT、JSTAR等）}で再現解析。日本特有の{特徴}を考慮した感度解析を追加する。」

### パターン2：方法論の応用
> 「{使用された方法（target trial emulation、g-formula等）}を要介護発生エンドポイントに応用し、『もし全員が{介入}したら要介護発生をX%予防可能』という仮想介入効果を推定。」

### パターン3：自分の研究領域との統合
> 「{論文のテーマ}と{自分の関心領域（筋質・身体機能・認知機能等）}の関連を{方法論}で解析。{特定の指標（CT muscle density、BIA PhA、gait speed等）}との縦断関連を評価。」

### パターン4：因果性検証
> 「Mendelian randomizationで{曝露}↔{アウトカム}の因果方向を検証。SHAP値による解釈可能AIで{機械学習モデル}の特徴重要度を可視化。」
