# Examples
## Case 1: 肺でタンパク質として発現が確認され、細胞膜表面に局在し、タンパク質立体構造が明らかになっており、対応する医薬品が開発されているヒトのタンパク質の一覧を取得する
### 検索方法の組み合わせ
- Select target dataset
    - `UniProt`
- Add filters
    - `Protein` / `Tissues w/expression reported` / `Lung`
    - `Protein` / `Cellular component` / `Membrane` / `plasma membrane`
    - `Structure` / `Structure data existence` / `Proteins with structure data`
    - `Interaction` / `ChEMBL assay existence` / `Conf-score 9: Direct single protein target assigned` 
- [検索結果を再現する](http://ep.dbcls.jp/togodx-server/build/?togoKey=uniprot&keys=%5B%5D&values=%5B%7B%22propertyId%22%3A%22protein_isolation_source_uniprot%22%2C%22ids%22%3A%5B%7B%22categoryId%22%3A%22568%22%7D%5D%7D%2C%7B%22propertyId%22%3A%22protein_cellular_component_uniprot%22%2C%22ids%22%3A%5B%7B%22categoryId%22%3A%22GO_0005886%22%2C%22ancestors%22%3A%5B%22GO_0110165%22%2C%22GO_0016020%22%5D%7D%5D%7D%2C%7B%22propertyId%22%3A%22structure_data_existence_uniprot%22%2C%22ids%22%3A%5B%7B%22categoryId%22%3A%221%22%7D%5D%7D%2C%7B%22propertyId%22%3A%22interaction_chembl_assay_existence_uniprot%22%2C%22ids%22%3A%5B%7B%22categoryId%22%3A%221%22%7D%5D%7D%5D)
    - [TODO]ep6のままなので、後で　togodx.dbcls.jp/human/ に直す。

### 検索のコツ
- `Tissues w/expression reported` では、タンパク質配列が解析されたクローンが単離された組織を検索できる。
- `Protein` / `Cellular component` では、ヒトの各タンパク質に[UniProtが根拠情報とともに付与したGeneOntology(GO)](https://www.uniprot.org/help/gene_ontology)のCellular component (細胞内局在)カテゴリに由来する機能アノテーション(GO term)を検索できる。
- `Structure` / `Structure data existence` では、UniProtの各エントリーに付与されている、PDBにおけるタンパク質立体構造データの有無を区別して検索できる。同じタンパク質でも異なる条件で立体構造を取得されている場合がある。
- `Interaction` / `ChEMBL assay existence` では、UniProtの各エントリーに付与されている、タンパク質と化合物の直接の相互作用を検出する方法（ChEMBL assay）の有無、種類を区別して検索できる。

### 結果とその考察・その後考えられる展開
- `131`のタンパク質(UniProt)の一覧が得られた。
    - 肺でタンパク質として発現が確認され、細胞膜表面に局在し、タンパク質立体構造が明らかになっており、対応する医薬品が開発されているヒトのタンパク質
- ![Add filter結果](https://github.com/togodx/togodx-config-human/raw/develop/docs/img/20211001_togodx_example1_01.png)
    - このリスト中には、[ACE2\(Angiotensin\-converting enzyme 2\)](https://www.uniprot.org/uniprot/Q9BYF1)も含まれている。
      - ACE2は、COVID-19の発病原因となるSARS-CoV-2ウイルスのウイルス受容体であり、SARS-CoV-2ウイルスのACE2への結合親和性が大きいため、COVID-19の高い感染力の土台となっている可能性がある。
      - SARS-CoV-2ウイルスはACE2を標的とすることが知られているが、今回の検索方法の組み合わせで共起した他のタンパク質との関連性を調べるきっかけになる。
      - また、将来、異なるウイルスによる呼吸器系の疾患が流行した場合に、ACE2以外のタンパク質がそのウイルスの標的候補として検討できる可能性がある。
- 検索結果のリストをさらに評価するために、`Map attributes`機能を使って他の属性での分布を見ることができる。
    - 例1:　ヒト遺伝子が保存されている最も遠縁の生物別に分類することができる`Gene` / `Evolutionary divergence` を利用する。
    - 例2: [GTEx(V6)](https://gtexportal.org/home/releaseInfoPage)で測定された49組織中で、組織特異的に高発現する遺伝子を組織別に分類することができる`Gene` / `Expressed in tissues` を利用する。
    - 例3:　UniProtの各エントリーに付与されているタンパク質と関連する疾患別の分類 `Protein` / `Disease-related proteins` を利用する。
    - [検索結果を再現する](http://ep.dbcls.jp/togodx-server/build/?togoKey=uniprot&keys=%5B%7B%22propertyId%22%3A%22gene_evolutionary_conservation_homologene%22%7D%2C%7B%22propertyId%22%3A%22gene_high_level_expression_gtex6%22%7D%2C%7B%22propertyId%22%3A%22protein_disease_related_proteins_uniprot%22%7D%5D&values=%5B%7B%22propertyId%22%3A%22protein_isolation_source_uniprot%22%2C%22ids%22%3A%5B%7B%22categoryId%22%3A%22568%22%7D%5D%7D%2C%7B%22propertyId%22%3A%22protein_cellular_component_uniprot%22%2C%22ids%22%3A%5B%7B%22categoryId%22%3A%22GO_0005886%22%2C%22ancestors%22%3A%5B%22GO_0110165%22%2C%22GO_0016020%22%5D%7D%5D%7D%2C%7B%22propertyId%22%3A%22structure_data_existence_uniprot%22%2C%22ids%22%3A%5B%7B%22categoryId%22%3A%221%22%7D%5D%7D%2C%7B%22propertyId%22%3A%22interaction_chembl_assay_existence_uniprot%22%2C%22ids%22%3A%5B%7B%22categoryId%22%3A%221%22%7D%5D%7D%5D)
    - [TODO]ep6のままなので、後で　togodx.dbcls.jp/human/ に直す。
    - ![Add filter+Map attributes](https://github.com/togodx/togodx-config-human/raw/develop/docs/img/20211001_togodx_example1_02.png)

## Case2: 作成中



