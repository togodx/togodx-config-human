# Examples
## Case 1: 類似した発現状況を示す遺伝子・タンパク質を標的とする医薬品の開発状況を調べる
##### 更新履歴
 - 2023-03-15作成
 - 2023-03-24更新 
### 目的
- 肺および腸で組織特異的に高い遺伝子発現が確認され、タンパク質として細胞膜表面に局在し、また何らかのタンパク質と化合物の直接の相互作用を検出する方法のデータが存在し、さらに「感染」に対する薬効がある化合物に関わる、ヒトのタンパク質の一覧を取得する
### 背景
- COVID-19を引き起こすSARS-CoV-2ウイルスが細胞内に侵入する上で重要な役割を果たすタンパク質として、ACE2やTMPRSS2が知られています。そのため、これらのタンパク質を標的とする治療法や予防法の開発が研究されています。
    - [ACE2 (Angiotensin-converting enzyme 2)](https://www.uniprot.org/uniprotkb/Q9BYF1/)： ACE2は、SARS-CoV-2ウイルスがヒト細胞に侵入するのに必要な受容体です。この受容体は、主に肺、小腸、心臓、腎臓などの細胞表面に存在しています。SARS-CoV-2ウイルスは、ACE2に結合することで細胞内に侵入し、感染を引き起こします。
    - [TMPRSS2 (transmembrane serine protease 2)](https://www.uniprot.org/uniprotkb/O15393/)： TMPRSS2は、SARS-CoV-2ウイルスの融合に必要なタンパク質であり、ウイルスが細胞内に侵入するのを助けます。TMPRSS2は、ACE2と同様に、主に肺や小腸などの細胞表面に存在しています。SARS-CoV-2ウイルスは、まずACE2に結合し、次にTMPRSS2によって細胞内に侵入します。
- ACE2およびTMPRSS2が、肺や小腸を構成する細胞の細胞膜表面で高発現することを手がかりに、類似した発現状況を示す遺伝子・タンパク質を標的とする医薬品(候補)がどのぐらい開発されているのかについて網羅的に調べてみます。

### 探索条件とその意図
- [この検索条件を再現するための設定ファイル](https://github.com/togodx/togodx-config-human/blob/develop/docs/togodx-preset_example_case1.json)
#### Select target dataset
- `UniProt`
    - 最終的に出力したいのはタンパク質のIDリストなので、タンパク質DBである`UniProt`を選択 
#### Add filters

- `Gene` / `Tissue-specific high expression (HPA)` / `Lung`
    - [The Human Protein Atlas project(HPA)](https://www.proteinatlas.org/) (ヒトの細胞、組織、臓器に存在するすべてのヒトタンパク質を様々なオミックス技術を統合してマッピングするプロジェクト)で得られた37組織中で、「Lung(肺)」に高発現が認められた遺伝子(236個)
- `Gene` / `Tissue-specific high expression (HPA)` / `Intestine`
    - HPAで得られた37組織中で、「Intestine(腸)」に高発現が認められた遺伝子(758個)
- `Protein` / `cellular component` / `cellular anatomical entity` / `membrane` / `plasma membrane`
    - ヒトの各タンパク質に[UniProtが根拠情報とともに付与したGeneOntology(GO)](https://www.uniprot.org/help/gene_ontology)のCellular component (細胞内局在)カテゴリに由来する機能アノテーション(GO term)の中で、「plasma membrane(細胞膜)」に局在することが知られているタンパク質(7,400個)
- `Interaction` / `ChEMBL assay existence` / `Conf-score 9: Direct single protein target assigned`
    -  UniProtの各エントリーに対して、そのタンパク質と化合物の直接の相互作用を検出する方法（ChEMBL assay）が存在し、さらに、アッセイとターゲットの関係に付与された[信頼度スコア](https://chembl.gitbook.io/chembl-interface-documentation/frequently-asked-questions/chembl-data-questions#what-is-the-confidence-score)の中で、最も高い信頼度(Direct single protein target assigned)が付与されているタンパク質(3,388個)
- `Compound` / `Drug indication` / `Infections`
    - ChEMBLの化合物に対して、MeSH(Medical Subject Headings)シソーラスを用いた薬剤適応疾患の分類の中で、「Infections(感染)」に対する適応が認められている化合物(2,041個)

#### Map attributes
- `Structure` / `Structure data existence` 
    - UniProtの各エントリーに付与されている、PDBにおけるタンパク質立体構造データの有無を区別して検索できます。同じタンパク質でも異なる条件で立体構造を取得されている場合があります。
- `Compound` / `Max drug development phase` 
    - ChEMBLの化合物には、世界のある地域で特定の疾患/診断（適応症）の治療薬として承認されている医薬品および臨床試験プロセスで適応症を調査中の臨床候補医薬品に関する情報が含まれており、すべての適応症における化合物の最高の開発段階（研究段階、第1-3相、上市後）に基づく分類です。


### 結果とその考察・応用
- `97`のタンパク質(UniProt)の一覧が得られました。
    - 肺および腸で組織特異的に高い遺伝子発現が確認され、タンパク質として細胞膜表面に局在し、また何らかのタンパク質と化合物の直接の相互作用を検出する方法のデータが存在し、さらに「感染」に対する薬効がある化合物に関わる、ヒトのタンパク質
- ![Example case-1 view results](https://raw.githubusercontent.com/togodx/togodx-config-human/develop/docs/img/20230804_example_case1_viewresults.png)
#### 得られたリストの解釈例
- このリストの中には、[ACE2](https://www.uniprot.org/uniprot/Q9BYF1)や[TMPRSS2(リスト中ではTMPS2)](https://www.uniprot.org/uniprotkb/O15393/)も含まれています。
    - SARS-CoV-2ウイルスはACE2やTMPRSS2を標的とすることが知られていますが、今回の検索方法の組み合わせで**共起した他のタンパク質との関連性を調べる**ことや、また、将来、異なるウイルスによる呼吸器・消化器系の疾患が流行した場合に、**このタンパク質のリストをそのウイルスの標的候補として検討する**きっかけになります。
    - 実際に、SARS-CoV-2ウイルスと関連する中東呼吸器症候群コロナウイルス（MERS-CoV)が細胞に感染するときの受容体である[DPP4(Dipeptidyl peptidase 4)](https://www.uniprot.org/uniprotkb/P27487/entry)は主に肺の肺細胞、多核上皮細胞、気管支粘膜下腺細胞、腎臓と小腸の上皮細胞、および活性白血球に発現していることが知られており([ref](https://doi.org/10.1038/nature12005))、このリストに含まれています。
- リスト中で関連が示されたタンパク質と医薬品との関係
    - ACE2 と [RIFAMPIN: CHEMBL374478](https://www.ebi.ac.uk/chembl/compound_report_card/CHEMBL374478/)
        - - ![Example case-1 ACE2](https://raw.githubusercontent.com/togodx/togodx-config-human/develop/docs/img/20230804_example_case1_ACE2.png)
        - 1965年に発見されたリファンピシンは、1971年に米国で承認され、世界保健機関（WHO）の必須医薬品リストに掲載されている医薬品です。
        - リファンピシンは、ウイルスによる細胞の形質転換を阻害する抗ウイルス薬であり、他の現代の抗ウイルス薬と比較して非常に安価なジェネリック医薬品として広く利用されています。
        - 最近の*in-silico*解析によって、リファンピシンがコロナウイルス疾患の治療に再利用できる最も有望な既存薬の1つであることが示されています([ref](https://doi.org/10.5501%2Fwjv.v11.i2.90))。
    - TMPRSS2 と [CAMOSTAT: CHEMBL590799](https://www.ebi.ac.uk/chembl/compound_report_card/CHEMBL590799/)
        - - ![Example case-1 TMPRSS2](https://raw.githubusercontent.com/togodx/togodx-config-human/develop/docs/img/20230804_example_case1_TMPRSS2.png)
        - カモスタットは、セリンプロテアーゼ阻害剤に分類されており、TMPRSS2の発現を抑制します。
        - カモスタットは急性膵炎などの治療薬剤として日本で開発され、すでに国内で長年にわたって処方されてきた薬剤です。安全性については十分な臨床データが蓄積されており、速やかに臨床治験を行うことが可能です。
        - カモスタットはSARS-CoV-2の治療薬としてフェーズ3まで進んでいるほか、カテプシンB阻害剤との組合せによりSARS-CoV-2感染効率を低下させることが確認されています([ref](https://www.cell.com/molecular-therapy-family/nucleic-acids/fulltext/S2162-2531(21)00259-6))。

---
## Case 2: 特定の疾患に関連する遺伝子をリストアップし、それらのタンパク質と相互作用する可能性のある化合物を取得する

##### 更新履歴
 - 2023-07-25作成
### 目的
「網膜色素変性症」に関わるヒト遺伝子についてリストアップした後、それらのオーソログ遺伝子がゼブラフィッシュにおいて保存されているものに絞り込み、それらの表現型、タンパク質と相互作用する可能性のある化合物を調べる。

### 背景
網膜色素変性症は指定難病の一つで治療方法も確立していないが、研究アプローチとしてモデル生物（ゼブラフィッシュ）を用いた薬剤候補スクリーニング実験が考えられる([参考文献](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8425951/))。ここでは、網膜色素変性症およびそれに関連する表現型に着目した場合のデータ探索を行う。

### 探索条件とその意図
- この検索条件の再現

#### Select target dataset
- `Ensembl gene`
    - 遺伝子ごとに情報をまとめたリストを作成したいので、遺伝子DBである`Ensembl gene`を選択
#### Filtering
* `Protein` / `Disease-related proteins`
  * Retinitis pigmentosa（網膜色素変性症）
  * Congenital stationary night blindness（先天停止性夜盲）
  * Cone-rod dystrophy（錐体桿体ジストロフィー）
  * Leber congenital amaurosis（レーバー先天黒内障
* `Gene` / `Tissue-specific high expression (HPA)`
  * Retina（網膜）
* `Gene` / `Ortholog existence`
  * Zebrafish (Danio rerio)
      * ゼブラフィッシュを網膜疾患のモデル生物と想定して、オーソログが存在することを条件として指定

#### Projection
* `Compound` / `Max drug development phase`
    * 関連する化合物を抽出する
* `Disease` / `Phenotypic abnormality`
    * 関連する表現型を抽出する

### 結果とその考察
#### 結果
* 指定した疾患に関連するヒト遺伝子で、ゼブラフィッシュにもオーソログが存在する42の遺伝子が得られた。

#### 得られたリストの解釈例
* 結果として得られた遺伝子群が持つ表現型の解釈
    * Resultを押すと結果が一覧されるが、その上部でヒット率のヒスとグラムが表示される。その中でも、”Abnormality of the eye”のヒット率が群を抜いており、抽出された遺伝子群の表現型として、目に何かしらの異常を及ぼす事が示唆される。
![]()

* 結果として得られた遺伝子群と関連するタンパク質と相互作用する可能性のある化合物の解釈
   * 結果として得られる化合物は935あるが、このうち、第IV相試験(製造販売後臨床試験)に達している化合物は46件である。関連する遺伝子が多くまた表現型も多様なため、得られた化合物が疾患に対して有効かはどうかを判定することは難しいが、少なくともCHEMBL91 (Miconazole) については、上記参考文献の実験でも網膜色素変性症に対し神経保護剤として有効であるという結果が出ている。


---
## Case 3: ドラッグリポジショニングの例からその薬剤の適応疾患について類似性等を比較する
##### 更新履歴
 - 2023-07-25作成
### 目的・背景
「Fluoxetine hydrochloride (ChEMBL: CHEMBL1201082)」フルオキセチンは、当初 "Major Depressive Disorder (MDD)"用の薬として利用されていたが、その後　”premenstrual syndrome(PMS), Premenstrual dysphoric disorder (PMDD)"にも適用されるようになった。なお、現在も両方の疾患の治療薬としても用いられている。TogoDXにおいて、フルオキセチンについて網羅的に探索し、どうしてリポジショニングが可能だったのかを考察する。
### 探索条件とその意図
#### Select target dataset
- `ChEMBL compound`
    - Map your IDsに入れるIDのデータベースを選択する

#### Map your IDｓ
- Fluoxetine hydrochloride (ChEMBL: CHEMBL1201082)」フルオキセチンをMapする

#### Filtering
Mapされた結果から、興味のあるカテゴリーを選択してFilteringを行う
- `Disease` / `Phenotypic abnormality`/`Abnormality of the nervous system`
    - フルオキセチンが関連する表現型を選択する
- `Disease` / `Disease in Mondo`/`Human disease`
    - フルオキセチンが関連する疾患名を選択する
- `Gene` / `Gene biotype`/`protein cording`
    - フルオキセチンが関連んする遺伝子を選択する
#### Projection
- `protein`/`Disease-related proteins`
    - 複数Mapされているので、比率を見るためにProjectionを利用する
- [この検索条件の再現]

### 結果とその考察
#### 結果
フルオキセチンをキーとして、関連する疾患(4)、表現型(5)、遺伝子(16）、たんぱく質（16）の情報が得られた。

#### 得られたリストの解釈例
* 結果として得られた関連疾患及び表現型について
    * フルオキセチンに関連する表現型はすべて「Abnormality of the nervous system」でHitする。その結果、フルオキセチンが神経伝達の異常に対して何かしらの作用をもたらすことがわかる。関連疾患としては「抑うつ症状」が見られる疾患を抽出しているため、フルオキセチンが「抑うつ症状」に作用をもたらすと考えられる。

* 結果として得られた関連遺伝子を考察する
    * 遺伝学的研究により、うつ症状と関連する可能性のある遺伝子や遺伝子変異がいくつか特定されており、これらの遺伝子は、脳内の神経伝達物質の調節や神経回路の機能に関与していることが多い。特にセロトニン、ドーパミン、ノルアドレナリンなどの神経伝達物質に関連する遺伝子がうつ症状と関連していることが示唆されている。結果として得られた遺伝子リストの中には、SLC6A4遺伝子（セロトニントランスポーター遺伝子）、HTR1A遺伝子（セロトニン1A 受容体(または5-HT 1A受容体)）等、「抑うつ症状」に深く関わると思われる遺伝子が含まれている。 
    * MDD, PMDDの論文の中で、「選択的セロトニン再取り込み阻害薬（SSRI）」の利用を推奨しており、フルオキセチンはSSRIの一つである。MDD及びPMDDの特徴的な症状の一つとして「抑うつ症状」が含まれており、抑うつ症状の発生にセロトニンが大きく関与するため、SSRIを用いる事で症状の軽減が期待できる。MDDもPMDDも精神障害であり「抑うつ症状」がその特徴の一つとなっている。そのため、フルオキセチンは「抑うつ症状の改善」に対して、効果が見られたものと考察できる。


