
"TogoDX UI調査まとめ" のスプレッドシートから、attributes.json を自動生成するスクリプトを置きました。  
- Usage
  1. [TogoDX UI調査まとめ](https://docs.google.com/spreadsheets/d/1e-hTRirfNlpS_3giVxV291r_H8tSJP2xDRMI0EEsE10/edit?pli=1#gid=679243932)のシートをTSV形式でダウンロードする。
  2. script ディレクトリで  `$ ./generate-attributes-json.sh [tsv exported from spreadsheet]`
  3. `attributes.json` という名前のファイルが出力されます。
