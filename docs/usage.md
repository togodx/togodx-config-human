# TogoDX/Humanの使い方

## 目次

- [画面構成](#画面構成)
  - [Explorer画面](#explorer画面)
    - [属性詳細](#属性詳細)
  - [Results画面](#results画面)
- [操作方法](#操作方法)
  - [Add filtersを用いた探索方法](#add-filtersを用いた探索方法)
  - [Map Attributesを用いた探索方法](#map-attributesを用いた探索方法)
  - [Map your IDsを用いた探索方法](#map-your-idsを用いた探索方法)
- [その他](#その他)
  - [ページヘッダ](#ページヘッダ)
  - [初期化](#初期化)
  - [IDのリンク関係](#idのリンク関係)

---
## 動画マニュアル
[TogoDX/human を使ってヒトのデータベースを統合的に探索、俯瞰、抽出する](https://doi.org/10.7875/togotv.2021.079)

## 画面構成

### Explorer画面

![Explorer](https://raw.githubusercontent.com/togodx/togodx-config-human/develop/docs/img/20211004_togodx_help_attributekeys.png)

Explorer画面(トップページ)では、遺伝子・タンパク質・化合物・疾患など各カテゴリごとに、様々な属性の内訳を俯瞰的に表示したり、絞り込み条件を指定することができます。また、ユーザが持つIDのリストを指定することで、各属性における分布を簡易的なエンリッチメント解析のように表示させることができます。

- `Attribute keys` 各データセットの属性
  - 各属性の`>`ボタンで、詳細データおよび階層分類や連続値分布を、展開したり閉じたりできます。
  - 最上段の`>`ボタンで、全ての属性の詳細を、まとめて展開したり閉じたりできます。
  - 詳細データについては後述の[属性詳細](#属性詳細)を参照。
- `Attribute values` 属性ごとの内訳、階層分類および連続値分布
  - 閉じた状態では、属性ごとに俯瞰的な内訳を表示しています。
  - 展開した状態では、階層分類の場合はカラムブラウザが、連続値分布の場合はヒストグラムが表示されます。
- `Log scale`
  - 各`Attribute values`の内訳を対数表示に切り替え、該当数の少ない内訳を選択しやすくできます。
- `Condition builder` 検索条件の指定
  - `Clear`ボタンを押すと、`Add filters`、`Map attributes`の選択が初期化されます。
- `Select target dataset` データセットの選択
  - 最終的な結果をどのデータセットのIDに対応させて表示するかを指定します。
- `Map your IDs` IDリストのマッピング
  - 利用者の持つIDリストを`Attribute keys`の各属性にマッピングします。
  - データセットを`Select target dataset`で変更すると、入力可能なIDの例がグレーで表示されます。
  - カンマ、スペース、改行区切りのIDリストが入力可能です。
- `Add filters` 絞り込み条件の指定
  - 各属性の`Attribute values`から、内訳や階層分類および連続値の範囲を絞り込み条件として指定します。
    - [Add filtersを用いた探索方法](#add-filtersを用いた探索方法)を参照。
  - 1つの属性内で複数の条件を追加した場合は、いずれかを満たすOR検索となります。
  - 複数の属性から条件を組み合わせて指定した場合、すべてを満たすAND検索となります。
- `Map attributes` 検索結果の各属性における分布
  - `Add filters`で絞り込まれた結果に対し、ここで指定した属性における分布を表示させることができます。
    - [Map attributesを用いた探索方法](#map-attributesを用いた探索方法)を参照。
- `View results` 結果表示
  - `Add filters`で指定した絞り込み条件を満たす[Results画面](#results画面)を表示します。

#### 属性詳細

![Explore](https://raw.githubusercontent.com/togodx/togodx-config-human/develop/docs/img/20211005_togodx_help_attribute.png)

各属性の`>`ボタンで、詳細データを展開表示することができます。

- `Description` 概要説明
  - `Attribute keys`で表示される属性情報の値や分類の内訳に関する説明。
- `API` データ取得方法
  - `Attribute keys`で表示される属性情報を取得するために使用しているAPIのURL。
- `Original data` 元データ
  - `TogoDX/Human`に収載されている属性情報の元データの提供元や出典情報。
- `Version` バージョン
  - `TogoDX/Human`に収載されている属性情報の元データのバージョン情報。
- `Last updated` 更新日
  - `TogoDX/Human`に収載されている属性情報の元データの更新年月日。

階層分類を持つ属性では細分類ごとの内訳が表示されます。

- `Values` 属性の細分類名
- `Total` 属性の総内訳数
- `Mapped` `Map your IDs`で指定したIDの該当数
- `p-value` `Mapped`の該当数と総数を元にしたp値

### Results画面

![result](https://raw.githubusercontent.com/togodx/togodx-config-human/develop/docs/img/20211004_togodx_help_results.png)

絞り込み条件に合致する`Select target dataset`で指定したIDの一覧、または、`Map your IDs`で指定したIDに対応する結果の一覧と、`Add filters`の値および`Map attributes`の内訳が取得できます。画面上部には検索結果の`分布の内訳グラフ`が表示されます。検索結果に含まれる各IDからは、より詳細な情報をポップアップ表示することができます。検索結果は`Saved conditions`からダウンロードすることができます。

- `Saved conditions` 保存された検索条件
  - `Saved Conditions`のプログレスバーでは、データ取得の状況が表示されます。
  - データ取得が全て完了すると`Completed`と表示され、検索条件が`Saved conditions`に保存されます。
  - 検索結果はTSV形式などでダウンロードすることができます。
  - 過去の検索条件をクリックすることで、結果画面を切替えて表示することができます。
  - ブラウザを閉じたり、再読み込みをすると、保存された検索条件はすべて消去されます。
- `分布の内訳グラフ`
  - `Hits/All` デフォルトでは各内訳の総数における、絞り込み条件を満たすIDの数が表示されます。
  - `Hits/All(%)` 上記の割合をパーセント表示します。(`Stretch`)
  - `Hits only` 絞り込み条件を満たすIDの実数だけを表示します。(`Only hit count`)
- `関連情報の表示`
  - 検索結果の表に表示されている各種IDをクリックすると、IDに紐づく関連情報が表示されます。
  - 関連情報の中にリンクがある場合は、外部のデータベースと紐づいており、更に詳細な情報を参照できます。
- `Return`
  - クリックすることで[Explorer画面](#explorer画面)に戻ることができます。
  - ブラウザの戻るボタンでは[Explorer画面](#explorer画面)に戻れないので注意が必要です。
  - [Explorer画面](#explorer画面)からは`Saved conditions`を選択することで[Results画面](#results画面)に戻ってくることができます。

![result_stanza](https://raw.githubusercontent.com/togodx/togodx-config-human/develop/docs/img/20211004_togodx_help_resultsstanza.png)

## 操作方法

### Add filtersを用いた探索方法

`Add filters`では、様々な属性における絞り込み条件を満たすIDセットを取得します。

- `Select target dataset`から検索結果の集計に用いるIDのデータセットを選択します。
- `Condition builder`の`Add filters`をクリックして有効化します（初期状態では選択済みです）。
  - 各属性の`Attribute values`の値をクリックすることで俯瞰的な内訳を条件に追加します。
  - 属性が階層分類を持つ場合は、詳細を展開しチェックボックスをクリックすることで、細分類を条件に追加することができます。
    - カラムブラウザで分類項目の右端に`▶`が表示されている場合は、その項目が子階層を持つことを示します。
  - 属性が連続値分布を持つ場合は、詳細を展開しヒストグラムの範囲を指定することで、選択範囲を条件に追加することができます。
	- 上段のヒストグラムで指定した範囲が下段に拡大表示され、その範囲が`Add filters`に追加されます。
- 絞り込み条件の選択が終わったら、`View results`をクリックします。結果は[Results画面](#results画面)のページで表示されます。

### Map Attributesを用いた探索方法

`Map attributes`では`Add filters`や`Map your IDs`で絞り込まれたIDセットに対し、他の属性での分布を見ることで新たな発見を促します。

- `Select target dataset`から検索結果の集計に用いるIDのデータセットを選択します。
- `Condition builder`の`Map attributes`をクリックして有効化します（初期状態では`Add filters`が選択されているため切替えます）。
  - `Attribute keys`の欄の右端に現れるチェックボックスを選択します。
  - 属性が階層分類を持つ場合は、詳細を展開し`Map following attributes`のチェックボックスを選択することで、細分類における分布表示を指定できます。
- 選択が終わったら、`View results`をクリックします。結果は[Results画面](#results画面)のページで表示されます。

### Map your IDsを用いた探索方法

`Map your IDs`では、手持ちのIDリストに対する各属性での偏りやp値の計算、`Add filters`による絞り込みや、`Map attributes`による他の属性での分布を確認することができます。

- `Select target dataset`で入力するIDに対応するデータセットを選択します。
- `Map your IDs`では、表示されるサンプルIDの表記方法に従ってIDを入力します。
  - 複数のIDは、カンマ、スペース、または改行区切りで入力します。
  - 手持ちのIDが`Select target dataset`に含まれていない場合は、[TogoID](https://togoid.dbcls.jp/)で変換したものを用いることができます。
- `Submit`ボタンを押すと、`In progress`の表記とともに進捗状況を示すバーが表示されます。

![Map your IDs](https://raw.githubusercontent.com/togodx/togodx-config-human/develop/docs/img/20211005_togodx_help_mapyourids_in_progress.png)

- 各属性の内訳ごとに該当するIDの数とp値が計算されます。
  - 各属性で、対応するIDを含む内訳には左肩にピンが表示され、該当するIDがない部分はグレーアウトされます。
  - ピンにマウスオーバーすることで該当数とp値が表示されます。

![Map your IDs](https://raw.githubusercontent.com/togodx/togodx-config-human/develop/docs/img/20211005_togodx_help_mapyourids.png)

## その他

### ページヘッダ

- `About`
  - TogoDX/Humanについての概要へのリンク
- `Help`
  - TogoDX/Humanの用語説明や機能説明へのリンク
- `Example`
  - TogoDX/Humanの具体的な事例解説へのリンク
- `Contact`
  - TogoDX/Humanに関するお問い合わせ

### 初期化

- 起動時あるいは再読み込み時には、画面が全て初期設定に戻ります。
- 上部にある`TogoDX`のロゴをクリックすることでも、初期設定に戻ります。
- `Condition builder`の`Clear`ボタンをクリックすると検索条件が初期化されます。

### IDのリンク関係
- [TogoDX/Humanで使用されているデータセット間のIDリンク関係の図](https://togodx.github.io/togodx-path/path-highlight-2022-11.html)
- [IDリンク関係の表](https://github.com/togodx/togodx-path/blob/main/tsv/dataset-links-2022-11.tsv)


