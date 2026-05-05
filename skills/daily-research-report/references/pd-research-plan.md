# Yuji の PD 研究計画（学振PD申請）

**毎日の論文選定で参照すること。10本中2本以上を PD 研究関連にする。**

---

## 研究タイトル

**「脳と筋から紐解く高齢者の身体機能の低下要因」**

---

## 研究の3課題

### 課題1: 疫学＋SHAP（包括測定研究）

**目的**: 日本人高齢者900名コホート（東北メディカル・メガバンク × 国立長寿医療研究センター連携）で、脳・筋・身体機能を包括測定し、身体機能低下・LTCI開始への寄与度を SHAP（説明可能AI）で順位化する。

**測定項目**:
- 脳容量（MRI）
- 脳機能性（fMRI、EEG）
- 脳神経密度（DTI、NODDI）
- 筋量（CT、MRI、BIA）
- 筋質（CT muscle density、ultrasound echo intensity、BIA phase angle、ECW/ICW、Dixon MRI fat infiltration）
- 筋力（握力、膝伸展力）
- 運動単位（surface EMG、運動単位decomposition）
- 手指器用さ（finger tapping、9-Hole Peg、digital phenotyping）
- 歩行（gait analysis、timed-up-and-go）
- バランス（Berg Balance、posturography）

**予備SHAP分析の知見**:
- 重要度ランキング: 手指器用さ ＞ 筋質 ＞ 認知機能 ＞ 筋力
- 数値: 脳機能性 13.1% ＞ 筋質 10.2% ＞ 筋量 7.5%

**統計手法**:
- SHAP（SHapley Additive exPlanations）
- 構造方程式モデル（SEM）
- Causal feature learning
- Mediation analysis
- Multi-state model（要介護移行）

### 課題2: 運動中EEG（脳活動測定）

**目的**: 128ch EEG で歩行・finger tapping・balance 課題中の脳波を測定し、身体機能低下高齢者の脳活動パターンを解明する。

**測定指標**:
- Aperiodic exponent（1/f slope）
- Cortical activity（運動関連電位、movement-related cortical potential）
- Beta band desynchronization
- Cortico-muscular coherence（CMC）
- Motor unit synchronization
- Mobile EEG technology

**研究意義**:
- 脳-筋協調の老化機序を解明
- 神経筋制御障害の早期マーカー候補

### 課題3: 介入RCT（tDCS試験）

**目的**: 高齢者80名のRCT（コントロール vs 機能トレ vs 機能トレ＋tDCS）で、転倒・身体機能・脳波変化を主要転帰として評価。

**介入条件**:
- 対照群: 通常ケア
- 介入群1: 機能トレーニング（balance、gait、resistance）
- 介入群2: 機能トレーニング ＋ tDCS

**tDCS刺激部位**:
- M1（一次運動野）
- Cerebellum（小脳）
- 両者の比較

**主要転帰**:
- 転倒発生率
- 身体機能スコア（SPPB、TUG）
- 脳波変化（aperiodic exponent、cortical activity）

---

## PD関連論文の選定キーワード（毎日2本以上の選定基準）

### A. 脳・筋・身体機能の統合解析
- SEM（構造方程式モデル）
- SHAP analysis、causal feature learning
- Mediation analysis
- Multi-modal integration（brain + muscle + function）
- UK Biobank brain-muscle integration
- Tohoku Medical Megabank multi-organ studies

### B. 筋質指標
- CT muscle density / muscle attenuation
- 超音波 echo intensity / muscle quality
- BIA phase angle
- ECW/ICW ratio
- Dixon MRI fat infiltration
- Myosteatosis
- D3-creatine dilution

### C. 手指器用さ・finger tapping
- 9-Hole Peg test
- Pegboard performance
- Digital phenotyping
- Smartphone tapping
- Fine motor control aging
- Hand dexterity decline

### D. 運動中EEG・脳波
- Aperiodic exponent
- 1/f neural noise
- Mobile EEG / wearable EEG
- Corticospinal control
- Cortico-muscular coherence
- Motor unit decomposition
- High-density surface EMG
- Movement-related cortical potential

### E. tDCS・rTMS（非侵襲的脳刺激）
- tDCS balance training
- tDCS gait training
- Cerebellar tDCS
- M1 tDCS motor function
- rTMS aging
- Non-invasive brain stimulation elderly

### F. サルコペニア・フレイル・健康寿命・LTCI
- Sarcopenia diagnosis (EWGSOP2, AWGS2019)
- Frailty (Fried, Rockwood)
- Disability-free life expectancy (DFLE)
- LTCI (Long-Term Care Insurance)
- Healthy life expectancy
- Multi-state model for disability

### G. 脳構造・脳機能と身体機能の関連
- Brain age / DunedinPACNI
- Sensorimotor cortex aging
- Cerebellum structure and motor function
- Basal ganglia and gait
- White matter and balance
- Hippocampus and dual-task gait

### H. 説明可能AI（SHAP、XAI）の老年医学応用
- SHAP for aging biomarkers
- XAI in geriatric medicine
- Interpretable ML for frailty prediction
- Causal feature learning
- ML mediation analysis

---

## PD関連論文の表示方法

### HTMLでの表示

```html
<div class="paper-card top1" 
     data-paper-id="20260505_01" 
     data-tags="PD関連|大規模コホート|SHAP|身体機能"
     ...>
  <span class="rank-badge">RANK 1</span>
  <span class="task-tag pd">📍 PD研究</span>
  <h2>論文タイトル</h2>
  ...
</div>
```

### CSSスタイル（templates に既に定義済み）

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

### 選定優先度

- **Top 5 以内に PD関連を最低1本は入れる**（重要性が高いため）
- 残り1本は Top 6-10 に配置可
- 木曜日（脳・認知）は PD関連が10本中6-7本になる（PD研究特化版では10本全てがPD関連）

---

## 研究アイデアの書き方（PD関連論文の場合）

PD関連論文の `idea` セクションでは、以下の枠組みで記述する：

1. **本研究の知見をPD研究1（疫学＋SHAP）にどう活かすか**
2. **PD研究2（運動中EEG）への展開可能性**
3. **PD研究3（tDCS RCT）への接続**
4. **日本人900名コホートでの再現・拡張アイデア**

例：
> 本研究のSHAP-基盤の脳-筋統合解析手法は、PD研究1の900名コホートで「脳機能性・筋質・身体機能」の重要度ランキングを精緻化する基盤となる。さらにPD研究2の128ch EEGデータと組み合わせれば、aperiodic exponentを説明変数に加えたmulti-modal SHAP解析が可能。PD研究3のtDCS RCTでは、本研究の同定した重要バイオマーカーを介入応答性の層別化指標として活用できる。

---

## 関連する研究者プロフィール（必ず接続させる）

- 健康寿命（disability-free life expectancy, LTCI）
- 身体機能（mobility, gait, balance, frailty）
- 筋質（CT muscle density, ultrasound echo intensity, BIA phase angle, ECW/ICW）
- 身体活動（leisure-time physical activity, social exercise）
- 認知機能（brain aging, cognition, brain structure）
- 遺伝子・オミクス（GWAS, epigenetic aging, DNA methylation, UK Biobank, Tohoku Medical Megabank）
- 方法論（g-formula, marginal structural models, target trial emulation, multi-state models, Mendelian randomization, machine learning, SHAP）
