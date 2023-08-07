# TogoDX とは

TogoDX (Togo Data eXplorer)は、知識グラフ(Knowledge graph)化された様々なデータベースを統合的に探索するためのフレームワークです。異なるデータベースに由来する多数のデータセットを、同じものを示すIDの互換性や、異なるデータ間のつながりを整理したID関係に基づいて統合しています。TogoDXでは、データセットが持つ多様な属性(attribute)によって絞り込みを行い、データサイエンスに有用なデータを柔軟に抽出する新しい仕組みの提供を目指しています。

## 開発の経緯

### 問題点

生命科学分野には異なる対象を取り扱う様々なデータベースがあります。これらを統合的に処理し、データサイエンスに用いるためには、以下のような問題がありました。

#### データベースごとに異なるインターフェース

データベースはそれぞれインターフェースが異なります。ウェブサイトへのアクセス方法、検索条件の指定方法、使われている用語などが異なるため、それぞれのデータベースの使い方を個別に調べる必要があります。扱うデータベースの数が増えるほど利用方法の調査にかかるコストは高くなります。

#### データベース間を繋ぐリンク情報の欠如

複数のデータベースに収載されたデータを組み合わせるためには、意味のある対応関係（リンク情報）を整備する必要があります。外部リンクのIDが記載されていないデータベースであっても、他のデータベースを経由することで繋がる可能性があります。このためには自らリンク情報を作成する必要があり、扱うデータベースの数が増えるほどリンク構築のコストは高くなります。

#### データベースごとに異なる出力形式

データベースごとに用いられている出力形式は様々です。複数のデータベースに由来する異なる形式のデータを、統合的に利用できる形式に変換する作業も、取り扱うデータベースの数が増えるほどコストが高くなります。

### 知識グラフによるデータ統合とTogoDXの開発

NBDC/DBCLSでは、これまでデータベース利用者に委ねられていた、これらの問題を解決するために、知識グラフによる生命科学分野のデータベース統合を進めてきました。知識グラフの技術基盤としてRDF (Resource Description Framework)を用いることで、以下のような利点を得ることができます。

- 複数のデータセットが共通のURIで連結される
- 各データとそのつながりの意味が表現できる、すなわち、知識が表現できる

RDFによって表現されたデータは、問い合わせ言語であるSPARQLでクエリを記述することで検索・加工することができます。RDFを用いてデータベースを統合したことにより、異なるデータセットをまたいだ情報の検索や取得が可能になりました。

一方で、統合されたデータ量は非常に大きく複雑なものとなり、検索にはある程度専門的な知識が必要です。そこで、統合されたデータを高速に処理し、ウェブブラウザ上の操作で探索することができるTogoDXが開発されました。

なお、TogoDXは知識グラフを用いて統合されたデータであれば、生物学に限らずあらゆるドメインの情報を扱うことの出来る汎用的なフレームワークとなっています。

# TogoDX/Humanについて

## TogoDX/Humanとは

TogoDX/HumanはTogoDXのフレームワークを用いて、ヒトに関するデータを統合的に探索するためのインターフェースを提供します。遺伝子、タンパク質、化合物、疾患などの情報を国内外のデータベースから収集・統合しています。本サイトは、[NBDC](https://biosciencedbc.jp/)/[DBCLS](https://dbcls.rois.ac.jp/)が開発・提供しています。

## TogoDX/Humanの特長

TogoDX/Humanでは、これまで多種多様なデータベースに散在して収録されてきたヒトに関する情報をワンストップで探索することができます。現在、21個のデータセットに由来する50個の属性(各データセットから抽出されたattribute)が利用可能です。

## 使い方

TogoDXは、全データを俯瞰しながらデータを探索する使い方と、自分のデータをIDとしてマッピングする使い方があり、その結果がさらなる解析につながるようなフレームワークを目指しています。

- 利用者の目的や興味に応じて、各属性の階層分類または連続値分布の一部を選択することにより、それらの条件を満たす結果（該当するタンパク質のリストなど）を取得できるため、研究対象の絞り込みに応用できます。
- また、利用者の持つIDリスト（実験から得られた遺伝子のリストなど）を入力することで、各属性における分布を俯瞰的に把握したり、他の属性における想定外の繋がりや偏りから、実験結果の解釈や考察の一助となります。
- さらに、絞り込んだ結果については、そのIDに関連する情報が容易に確認できるほか、属性情報をダウンロードしてさらなる統合解析に利用することができます。

TogoDXの検索条件はURLとして保存可能で、他のユーザーと共有することができます。

- [使い方の詳細についてはこちら](https://togodx.github.io/togodx-config-human/usage.html)
- [具体的な利用事例はこちら](https://togodx.github.io/togodx-config-human/examples.html)
- [データセット間のIDリンク関係](https://togodx.github.io/togodx-path/path-highlight-2022-11.html)

## 更新履歴
- 2023.01.11 [データ更新](https://dbcls.rois.ac.jp/ja/2023/01/11/post1.html) (v2023-01)
  - データ更新
    - Ensembl (human release 108)
    - UniProt (release 2022_05)
    - PDB (2022-12-14 updated)
    - neXtProt (Release 2022-08-18)
    - PubChem (Ver:2022-12-15)
    - ChEBI (Release 220)
    - Mondo Disease Ontology (v2022-12-01)
    - MeSH (2022-12-16 updated)
    - HPO (2022-12-15 updated)
    - GWAS Catalog All associations (2022-12-16 updated)
    - ClinVar (2022-12-01 updated)
- 2022.11.11 [新規Attribute追加およびデータ更新](https://dbcls.rois.ac.jp/ja/2022/11/11/post1.html) (v2022-11)
    - 14種類の属性(Attribute)を追加
        - Gene
            - Ortholog existence
            - Biological process
            - Cellular component
            - Molecular function
            - Transcript biotype
            - Transcript length
        - Protein
            - UniProtKB sections
            - Isoform specific GO existence
            - Catalytic activity
            - Isoform specific interaction existence
            - Pathway annotation
        - Structure
            - \# of turn structures
            - \# of disulfide bonds
            - Rate of disorder regions 
    - 探索の起点となるID(target dataset)として “Ensembl transcript” を追加
    - データ更新
        - Ensembl (human release 107)
        - UniProt (release 2022_03)
        - PDB (2022-09-28 updated)
        - Reactome (76)
        - ChEMBL (CHEMBL31)
        - ChEBI (Release 213)
        - Mondo Disease Ontology (v2022-08-01)
        - MeSH (2022-09-20 updated)
        - GWAS Catalog All associations (2022-09-20 updated)
        - ClinVar (2022-09-01 updated)     
- 2022.06.20 [TogoDX/human v1\.1を公開](http://dbcls.rois.ac.jp/ja/2022/06/20/post1.html)
    - アプリケーションの操作性向上を目的として様々な技術的な調整を行い、v1.0と比較して約1000倍の高速化を実現
    - TogoDX/humanで使用されているデータセット間のIDの対応関係を掲載
    - ”# of alpha-helices”、”# of beta-sheets” のオリジナルデータをPDBからUniProtに変更し、単量体における”Rate of helical regions”、”Rate of beta strand regions”にそれぞれ変更
- 2021.10.05 [TogoDX/Human (v1.0)を公開](http://dbcls.rois.ac.jp/ja/2021/10/05/post1.html) 

# 推奨ブラウザ
- Google Chrome (最新版)
- Mozilla Firefox　(最新版)
- Microsoft Edge　(最新版)
- Apple Safari　(最新版)

# ファンディング

このサービスは、NBDCのライフサイエンスデータベース統合推進事業の一環として開発されました。

# サイトポリシー

- [DBCLSのサイトポリシー](http://dbcls.rois.ac.jp/policy.html)に準ずる。

