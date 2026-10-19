#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# fetch_api_json.sh で取得したデータについて、データソースの Ver. 番号と更新日を
# 取得元から調べ、このスクリプトが置いてあるリポジトリ (togodx-config-human) の
# 以下のファイルを書き換える。
#   - config/attributes.dx-server.json
#       attributes.<ID>.source[].version / updated
#   - docs/about.md (英語) / about_ja.md (日本語)
#       「## Update history」「## 更新履歴」の先頭に更新情報を追記
#
# Ver. 番号と更新日の取得元:
#   - 通常: RDF portal の設定リポジトリ
#       https://github.com/rdfportal/website/tree/main/assets/datasets
#       の <dataset>/metadata.yaml にある version / issued
#   - variant (TogoVar) のみ: https://grch38.togovar.org/doc/datasets の
#       ClinVar / GWAS Catalog の行 (日付のみ)。
#       このページは Cloudflare のボット判定で取得できないので、ページの生成元である
#       GitHub 上のソース (togovar/togovar の datasets_grch38.pug) を読む。
#
# 取得した更新日が現在の値より古い場合は、取得元の管理ミスと考えられるので
# 書き換えず、報告だけする (手動で対応する)。
# 取得元に設定が無いデータセット (Mondo, HPO) も報告だけする。
#
# 対象は fetch_api_json.sh と同じ行 (6カラム目が "OK" かつ 5カラム目が URL) で、
# かつ <output_dir> に JSON が実際に存在するもの。attribute の ID は
# fetch_api_json.sh の保存ファイル名と同じく URL の最後のスラッシュ以降とする。
#
# attribute とデータセットの対応は ID の末尾 (_ensembl, _uniprot など) で決める。
# 対応表は下の SUFFIX_TO_DATASET / ATTRIBUTE_TO_DATASET / DATASETS を編集する。
#
# Usage: update_attribute_versions.py [options] <input.tsv> <output_dir>
#   -n, --dry-run        ファイルを書き換えず、変更内容の表示のみ
#   --date YYYY-MM-DD    about に書く更新日 (既定: 今日)
#
# 例:
#   python3 togodx-config-human/script/update_attribute_versions.py \
#       dev2610/togodx_human_2026_attributes.tsv dev2610/attributes
#
# Python 3.6 以上、標準ライブラリのみで動く。

import argparse
import datetime
import json
import os
import re
import sys
import urllib.request
from collections import OrderedDict

# このスクリプトは <リポジトリ>/script/ に置く
REPO_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONFIG_PATH = os.path.join(REPO_DIR, "config", "attributes.dx-server.json")
ABOUT_PATH = os.path.join(REPO_DIR, "docs", "about.md")
ABOUT_JA_PATH = os.path.join(REPO_DIR, "docs", "about_ja.md")

RDFPORTAL_METADATA_URL = ("https://raw.githubusercontent.com/rdfportal/website/main"
                          "/assets/datasets/{}/metadata.yaml")
TOGOVAR_DATASETS_URL = ("https://raw.githubusercontent.com/togovar/togovar/master"
                        "/app/frontend/views/doc/ja/datasets_grch38.pug")

# about の更新履歴の見出し: (節の見出し, 項目名)
ABOUT_EN = ("## Update history", "Data update")
ABOUT_JA = ("## 更新履歴", "データ更新")

# データセットの定義。
#   name    about.md の更新履歴に書く名前
#   source  "rdfportal" (id = assets/datasets 以下のディレクトリ名)
#           "togovar"   (id = datasets ページの表の1カラム目の名前)
#           None        取得元に設定が無いので書き換えない (報告のみ)
#   version (任意) 取得した version を config の表記に整える関数
DATASETS = {
    "ensembl":    {"name": "Ensembl", "source": "rdfportal", "id": "ensembl",
                   "version": lambda v: "human release " + v},
    "homologene": {"name": "HomoloGene", "source": "rdfportal", "id": "homologene"},
    "ncbigene":   {"name": "NCBI Gene", "source": "rdfportal", "id": "ncbigene"},
    "refex":      {"name": "RefEx", "source": "rdfportal", "id": "refex"},
    "uniprot":    {"name": "UniProt", "source": "rdfportal", "id": "uniprot",
                   "version": lambda v: "release " + v},
    "pdb":        {"name": "PDB", "source": "rdfportal", "id": "pdb"},
    "reactome":   {"name": "Reactome", "source": "rdfportal", "id": "reactome",
                   "version": lambda v: "V" + v},
    "chembl":     {"name": "ChEMBL", "source": "rdfportal", "id": "chembl",
                   "version": lambda v: "CHEMBL" + re.sub(r"\.0$", "", v)},
    "chebi":      {"name": "ChEBI", "source": "rdfportal", "id": "chebi"},
    "pubchem":    {"name": "PubChem", "source": "rdfportal", "id": "pubchem"},
    "glycosmos":  {"name": "GlyCosmos", "source": "rdfportal", "id": "glycosmos"},
    "mesh":       {"name": "MeSH", "source": "rdfportal", "id": "mesh"},
    "nando":      {"name": "NANDO", "source": "rdfportal", "id": "nando"},
    "togoid":     {"name": "TogoID", "source": "rdfportal", "id": "togoid"},
    "tismed":     {"name": "TiSMeD", "source": "rdfportal", "id": "tismed"},
    # RDF portal の bioportal グラフを使っているが、assets/datasets に設定が無い
    "mondo":      {"name": "Mondo Disease Ontology", "source": None},
    "hpo":        {"name": "HPO", "source": None},
    "togovar_clinvar": {"name": "ClinVar", "source": "togovar", "id": "ClinVar"},
    "togovar_gwas":    {"name": "GWAS Catalog All associations", "source": "togovar",
                        "id": "GWAS Catalog"},
}

# attribute ID の末尾 -> DATASETS のキー
SUFFIX_TO_DATASET = {
    "ensembl": "ensembl", "homologene": "homologene", "ncbigene": "ncbigene",
    "refex": "refex", "uniprot": "uniprot", "pdb": "pdb", "reactome": "reactome",
    "chembl": "chembl", "chebi": "chebi", "pubchem": "pubchem",
    "glycosmos": "glycosmos", "mesh": "mesh", "nando": "nando",
    "mondo": "mondo", "hpo": "hpo",
}

# 末尾では決まらない attribute -> DATASETS のキー
ATTRIBUTE_TO_DATASET = {
    # config の source は ChEMBL-RDF
    "interaction_chembl_assay_existence_uniprot": "chembl",
    # GO のデータは NCBI Gene から TogoID に切り替えた (config の source は TogoID)
    "gene_biological_process_ncbigene": "togoid",
    "gene_cellular_component_ncbigene": "togoid",
    "gene_molecular_function_ncbigene": "togoid",
    "variant_clinical_significance_togovar": "togovar_clinvar",
    "variant_gwas_togovar": "togovar_gwas",
}

DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")


def fetch(url):
    req = urllib.request.Request(url, headers={"User-Agent": "togodx-update-versions"})
    with urllib.request.urlopen(req, timeout=60) as res:
        return res.read().decode("utf-8")


def read_tsv(path, output_dir):
    """fetch_api_json.sh と同じ条件で対象行を選び、(取得済みID, 未取得ID) を返す"""
    fetched, missing = [], []
    with open(path, encoding="utf-8", newline="") as f:
        for line in f:
            cols = line.rstrip("\r\n").split("\t")
            if len(cols) < 6:
                continue
            url, status = cols[4].strip(), cols[5].strip()
            if status != "OK" or not re.match(r"https?://", url):
                continue
            attr = url.rsplit("/", 1)[1]
            if attr in fetched or attr in missing:
                continue
            if os.path.isfile(os.path.join(output_dir, attr + ".json")):
                fetched.append(attr)
            else:
                missing.append(attr)
    return fetched, missing


def yaml_top_level(text, key):
    """metadata.yaml のトップレベルにある単純な 'key: value' の値を返す"""
    m = re.search(r"^%s:[ \t]*(.*)$" % re.escape(key), text, re.M)
    if not m:
        return ""
    value = re.sub(r"\s+#.*$", "", m.group(1)).strip()
    if len(value) >= 2 and value[0] == value[-1] and value[0] in "'\"":
        value = value[1:-1]
    return value


def rdfportal_info(dataset_id):
    text = fetch(RDFPORTAL_METADATA_URL.format(dataset_id))
    return yaml_top_level(text, "version"), yaml_top_level(text, "issued")


def togovar_table():
    """datasets ページのソース (pug) の表を {1カラム目の名前: 2カラム目} にする"""
    table = {}
    cells = None
    for line in fetch(TOGOVAR_DATASETS_URL).splitlines() + ["tr"]:
        s = line.strip()
        if s == "tr":
            if cells and len(cells) >= 2:
                table.setdefault(cells[0], cells[1])
            cells = []
        elif cells is None:
            continue
        elif s == "td" or s.startswith("td ") or s.startswith("td("):
            cells.append(s[2:].strip() if s.startswith("td ") else "")
        elif s.startswith("|") and cells:
            cells[-1] = (cells[-1] + " " + s[1:].strip()).strip()
    if not table:
        raise RuntimeError("表が見つかりません: " + TOGOVAR_DATASETS_URL)
    return table


def about_line(name, version, updated):
    # 既存の表記に合わせ、Ver. 番号が日付のものは "(日付 updated)"
    if DATE_RE.match(version):
        return "    - %s (%s updated)" % (name, version)
    return "    - %s (%s)" % (name, version)


def update_about(text, date, lines, section, title):
    """更新履歴の節 (section) の先頭に追記した about の内容を返す"""
    out = text.split("\n")
    try:
        start = next(i for i, l in enumerate(out) if l.strip() == section) + 1
    except StopIteration:
        raise RuntimeError("「%s」がありません" % section)
    heading = "- %s %s" % (date.strftime("%Y.%m.%d"), title)
    sub = "  - " + title

    if start < len(out) and out[start] == heading:
        # 同じ日に再実行した場合は、その日の項目に足す (同じ名前の行は置き換え)
        end = start + 1
        while end < len(out) and out[end].startswith("    - "):
            end += 1
        if end < len(out) and out[end] == sub:
            end += 1
            while end < len(out) and out[end].startswith("    - "):
                end += 1
        block = out[start + 2:end] if out[start + 1:start + 2] == [sub] else []
        for line in lines:
            name = line.rsplit(" (", 1)[0]
            same = [i for i, l in enumerate(block) if l.rsplit(" (", 1)[0] == name]
            if same:
                block[same[0]] = line
            else:
                block.append(line)
        out[start:end] = [heading, sub] + block
    else:
        out[start:start] = [heading, sub] + lines
    return "\n".join(out)


def main():
    ap = argparse.ArgumentParser(
        description="取得したデータの Ver. 番号と更新日で attributes の JSON と about.md を更新する")
    ap.add_argument("input_tsv")
    ap.add_argument("output_dir", help="fetch_api_json.sh の出力先ディレクトリ")
    ap.add_argument("-n", "--dry-run", action="store_true")
    ap.add_argument("--date", help="about に書く更新日 YYYY-MM-DD (既定: 今日)")
    args = ap.parse_args()

    config_path = CONFIG_PATH
    about_paths = [(ABOUT_PATH, ABOUT_EN), (ABOUT_JA_PATH, ABOUT_JA)]
    for path in [config_path] + [p for p, _ in about_paths]:
        if not os.path.isfile(path):
            ap.error("書き換えるファイルがありません: %s" % path)

    date = (datetime.datetime.strptime(args.date, "%Y-%m-%d").date()
            if args.date else datetime.date.today())

    fetched, not_fetched = read_tsv(args.input_tsv, args.output_dir)
    if not fetched:
        print("対象となる取得済みの attribute がありません: %s" % args.input_tsv)
        return 0

    with open(config_path, encoding="utf-8") as f:
        config_text = f.read()
    config = json.loads(config_text, object_pairs_hook=OrderedDict)
    attributes = config["attributes"]

    # attribute -> データセット
    by_dataset = OrderedDict()
    not_in_config, unknown = [], []
    for attr in fetched:
        if attr not in attributes:
            not_in_config.append(attr)
            continue
        key = ATTRIBUTE_TO_DATASET.get(attr) or SUFFIX_TO_DATASET.get(attr.rsplit("_", 1)[-1])
        if key is None:
            unknown.append(attr)
            continue
        by_dataset.setdefault(key, []).append(attr)

    # データセットごとに Ver. 番号と更新日を取得
    info = {}           # key -> (version or None, updated)
    no_source, failed = [], []
    togovar = None
    for key in by_dataset:
        ds = DATASETS[key]
        try:
            if ds["source"] is None:
                no_source.append(key)
                continue
            if ds["source"] == "togovar":
                if togovar is None:
                    togovar = togovar_table()
                # 表にあるのは日付だけ
                version, updated = None, togovar.get(ds["id"], "").replace("/", "-")
                if not DATE_RE.match(updated):
                    raise RuntimeError("datasets の表に %s の日付がありません: %r"
                                       % (ds["id"], togovar.get(ds["id"])))
            else:
                version, updated = rdfportal_info(ds["id"])
                if not updated:
                    raise RuntimeError("metadata.yaml に issued がありません")
                if version and "version" in ds:
                    version = ds["version"](version)
            info[key] = (version or None, updated)
        except Exception as e:
            failed.append((key, str(e)))

    # config を書き換え
    changes, warnings, older, about_lines = [], [], [], []
    for key, attrs in by_dataset.items():
        if key not in info:
            continue
        version, updated = info[key]
        changed = None
        for attr in attrs:
            for src in attributes[attr].get("source", []):
                old_version, old_updated = src.get("version", ""), src.get("updated", "")
                # Ver. 番号が取れないデータセットは日付を入れる
                new_version = version or updated
                if (old_version, old_updated) == (new_version, updated):
                    continue
                if updated < old_updated:
                    older.append("%s: 現在 %s (%s) / 取得元 %s (%s)"
                                 % (attr, old_version, old_updated, new_version, updated))
                    continue
                src["version"], src["updated"] = new_version, updated
                changes.append((attr, old_version, old_updated, new_version, updated))
                changed = (new_version, updated)
        if not DATE_RE.match(updated):
            warnings.append("%s: 更新日が YYYY-MM-DD 形式ではありません: %s"
                            % (DATASETS[key]["name"], updated))
        if changed:
            about_lines.append(about_line(DATASETS[key]["name"], *changed))

    # 報告
    print("対象: %d attribute / 変更: %d attribute" % (len(fetched), len(changes)))
    for attr, ov, ou, nv, nu in changes:
        print("  %s: %s (%s) -> %s (%s)" % (attr, ov, ou, nv, nu))

    def report(title, items):
        if items:
            print("\n" + title)
            for item in items:
                print("  - " + item)

    report("注意:", sorted(set(warnings)))
    report("取得元の更新日が現在の値より古いため書き換えなかった attribute (要確認):", older)
    report("取得元に設定が無いため書き換えなかったデータセット:",
           ["%s: %s" % (DATASETS[k]["name"], " ".join(by_dataset[k])) for k in no_source])
    report("Ver. 番号と更新日を取得できなかったデータセット:",
           ["%s (%s): %s" % (DATASETS[k]["name"], " ".join(by_dataset[k]), e)
            for k, e in failed])
    report("%s に無い attribute:" % os.path.basename(config_path), not_in_config)
    report("データセットとの対応が分からない attribute (対応表に追加してください):", unknown)
    report("%s に JSON が無いため対象外とした attribute:" % args.output_dir, not_fetched)

    if not changes:
        print("\n変更はありません。")
        return 1 if failed else 0

    new_config = json.dumps(config, indent=2, ensure_ascii=False) + "\n"
    new_abouts = []
    if about_paths:
        for path, (section, title) in about_paths:
            with open(path, encoding="utf-8") as f:
                try:
                    new_abouts.append((path, update_about(f.read(), date, about_lines,
                                                          section, title)))
                except RuntimeError as e:
                    print("Error: %s: %s" % (path, e), file=sys.stderr)
                    return 1
        print("\n更新履歴に追記する内容:")
        print("\n".join(about_lines))

    if args.dry_run:
        print("\n(dry-run のためファイルは書き換えていません)")
    else:
        with open(config_path, "w", encoding="utf-8") as f:
            f.write(new_config)
        print("\n書き換えました: %s" % config_path)
        for path, text in new_abouts:
            with open(path, "w", encoding="utf-8") as f:
                f.write(text)
            print("書き換えました: %s" % path)
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
