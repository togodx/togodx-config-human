#!/bin/bash
set -euo pipefail

function usage {
    cat <<EOF
Usage:
    $(basename ${0}) [input]

    The input is a tsv file exported from "TogoDX UI調査まとめ".
    "datasets" can not be generated from the input tsv. "datasets" value is just copied from existing attributes.dx-server.json.
    The result is output as a file named "attributes.json".

Requirement:
    jq
EOF
}

if [ $# -ne 1 ]; then
  usage
  exit 1
fi

TSV=$1

sed '1d;s/\r//g' $TSV | jq -s -R 'split("\n")|map(split("\t"))|map({(.[1]): {"label": .[2], "description": .[3], "api": ("https://togodx.dbcls.jp/human/breakdown/" + .[1]), "order": .[18], "dataset": .[16], "datamodel": .[17], "source": [{"label": .[6], "url": .[7], "version": .[8], "updated": .[9]}]}})|.[]' | jq -s add | jq '{"attributes": .}' | awk '$0!~/"order": "",$/' > attributes.attributes.json

sed '1d;s/\r//g' $TSV | awk -F "\t" 'a[$1]{a[$1]=a[$1] "\t" $2}!a[$1]{a[$1]=$2;c[n++]=$1}END{for(i=0;i<n;i++)print tolower(c[i]) "\t" c[i] "\t" a[c[i]]}' | jq -s -R 'split("\n")[:-1]|map(split("\t"))|map({"id": .[0], "label": .[1], "attributes": .[2:]})|{"categories": .}' > attributes.categories.json

jq -s add attributes.categories.json attributes.attributes.json <(jq '{datasets}' ../config/attributes.dx-server.json) > attributes.json

rm attributes.attributes.json attributes.categories.json
