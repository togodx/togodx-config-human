English | [日本語](about_ja.md)

# What is TogoDX?

TogoDX (Togo Data eXplorer) is a framework for the integrated exploration of various databases that have been turned into knowledge graphs. It integrates many datasets derived from different databases, based on the compatibility of IDs that refer to the same entity and on ID relations that organize the connections between different kinds of data. TogoDX aims to provide a new mechanism for flexibly extracting data useful for data science, by narrowing down data with the diverse attributes that the datasets have.

## Background

### Problems

In the life sciences there are many databases dealing with different subjects. Processing them in an integrated manner and using them for data science involved the following problems.

#### Interfaces differ from database to database

Each database has its own interface. Because the way to access the website, the way to specify search conditions, and the terminology all differ, users have to learn how to use each database individually. The more databases are involved, the higher the cost of learning how to use them.

#### Lack of link information connecting databases

To combine data stored in multiple databases, meaningful correspondences (link information) have to be prepared. Even databases that do not list the IDs of external links may be connected by way of other databases. This requires users to build the link information themselves, and the more databases are involved, the higher the cost of building the links.

#### Output formats differ from database to database

The output formats used by databases vary. The work of converting data in different formats, derived from multiple databases, into a format that can be used in an integrated manner also becomes more costly as the number of databases increases.

### Data integration with knowledge graphs and the development of TogoDX

To solve these problems, which had so far been left to database users, NBDC/DBCLS has been integrating life science databases with knowledge graphs. Using RDF (Resource Description Framework) as the technical foundation of the knowledge graphs brings the following advantages.

- Multiple datasets are linked by common URIs
- The meaning of each piece of data and of its connections can be expressed; in other words, knowledge can be expressed

Data expressed in RDF can be searched and processed by writing queries in SPARQL, its query language. Integrating databases with RDF has made it possible to search and retrieve information across different datasets.

On the other hand, the integrated data has become very large and complex, and searching it requires a certain degree of expertise. TogoDX was therefore developed to process the integrated data at high speed and to make it explorable through operations in a web browser.

Note that TogoDX is a general-purpose framework: as long as the data is integrated with a knowledge graph, it can handle information from any domain, not only biology.

# About TogoDX/Human

## What is TogoDX/Human?

TogoDX/Human uses the TogoDX framework to provide an interface for the integrated exploration of data related to humans. It collects and integrates information on genes, proteins, compounds, diseases and more from databases in Japan and abroad. This site is developed and provided by [NBDC](https://biosciencedbc.jp/)/[DBCLS](https://dbcls.rois.ac.jp/).

## Features of TogoDX/Human

TogoDX/Human lets you explore, in one place, information on humans that has so far been scattered across a wide variety of databases. Currently, 50 attributes (attributes extracted from each dataset) derived from 21 datasets are available.

## How to use

TogoDX can be used in two ways: exploring data while getting an overview of all the data, and mapping your own data as IDs. It aims to be a framework whose results lead to further analysis.

- By selecting part of the hierarchical classification or of the distribution of continuous values of each attribute according to your purpose and interests, you can obtain the results that satisfy those conditions (such as a list of matching proteins), which can be applied to narrowing down research targets.
- By entering your own ID list (such as a list of genes obtained from an experiment), you can get an overview of its distribution in each attribute, and unexpected connections or biases in other attributes can help you interpret and discuss your experimental results.
- For the narrowed-down results, you can easily check the information related to each ID, and download the attribute information to use it in further integrated analysis.

Search conditions in TogoDX can be saved as a URL and shared with other users.

- [Details on how to use TogoDX/Human](https://togodx.github.io/togodx-config-human/usage.html)
- [Concrete use cases](https://togodx.github.io/togodx-config-human/examples.html)
- [ID link relations between datasets](https://togodx.github.io/togodx-path/path-highlight-2022-11.html)

## Update history
- 2026.10.16 Data update
  - Data update
    - Ensembl (human release 115)
    - HomoloGene (release_20230517)
    - NCBI Gene (release_20230525)
    - TogoID (2026-08-20)
    - UniProt (release 2026_01)
    - PDB (Release_20260902)
    - Reactome (V97)
    - ChEMBL (CHEMBL36)
    - ChEBI (Release 244)
    - PubChem (2026-05-06 updated)
    - GlyCosmos (2026-03-17 updated)
    - Mondo Disease Ontology (2026-08-04 updated)
    - MeSH (2025)
    - NANDO (2026-05-29 updated)
    - HPO (2026-06-23 updated)
    - GWAS Catalog All associations (2025-11-12 updated)
    - ClinVar (2026-07-02 updated)
  - Because neXtProt has been discontinued, the attributes "Isoform specific GO existence" and "Isoform specific interaction existence" (Protein) were discontinued, and the data source of "Evidence of existence" was switched from neXtProt to UniProt.
- 2024.04.03 Data update
  - Data update
    - Ensembl (human release 111)
    - UniProt (release 2024_01)
    - PDB (2023-10-20 updated)
    - neXtProt (Release 2023-09-11)
    - ChEMBL (CHEMBL33)
    - PubChem (Ver:2024-02-20)
    - ChEBI (Release 231)
    - GlyCosmos (v3.4.0)
    - Mondo Disease Ontology (v2024-03-04)
    - MeSH (2023-12-19 updated)
    - HPO (2024-02-08 updated)
    - GWAS Catalog All associations (2023-05-09 updated)
    - ClinVar (2024-02-07 updated)
- 2023.09.01 [TogoDX/Human v1\.2 released]()
  - UI updates and additions (v1.2)
    - Added the ability to choose which attributes to display, and introduced presets
    - Ontology browser that can search for terms deep in the hierarchy
    - Preview of the results of an exploration that combines filters
    - Saving and sharing of exploration conditions as JSON files
  - Attribute added (v2023-09)
      - Disease
        - Mode of inheritance
  - Data update (v2023-09)
    - ATC (2022AB) 
    - ChEBI (Release 219)
    - ChEMBL (CHEMBL32)
    - ClinVar (2023-03-06 updated)
    - Ensembl (human release 109)
    - GWAS Catalog (2023-03-29  updated)
    - HPO (2023-01-27)
    - MEDGEN (2023-03-14)
    - MeSH (2023-03-07 updated)
    - Mondo Disease Ontology (v2023-03-01)
    - NANDO (1.0.0)
    - PubChem (1.8.0 beta)
    - Rhea (release 126)
    - UBERON (2023-03-15)
    - UniProt (release 2023_01)
    - PDB (2023-03-15 updated) 
- 2023.01.11 [Data update](https://dbcls.rois.ac.jp/ja/2023/01/11/post1.html) (v2023-01)
  - Data update
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
- 2022.11.11 [New attributes and data update](https://dbcls.rois.ac.jp/ja/2022/11/11/post1.html) (v2022-11)
    - Added 14 attributes
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
    - Added "Ensembl transcript" as an ID from which to start an exploration (target dataset)
    - Data update
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
- 2022.06.20 [TogoDX/Human v1\.1 released](http://dbcls.rois.ac.jp/ja/2022/06/20/post1.html)
    - Made various technical adjustments to improve the usability of the application, making it about 1,000 times faster than v1.0
    - Published the ID correspondences between the datasets used in TogoDX/Human
    - Changed the original data of "# of alpha-helices" and "# of beta-sheets" from PDB to UniProt, and changed them to "Rate of helical regions" and "Rate of beta strand regions" in the monomer, respectively
- 2021.10.05 [TogoDX/Human (v1.0) released](http://dbcls.rois.ac.jp/ja/2021/10/05/post1.html) 

# Recommended browsers
- Google Chrome (latest version)
- Mozilla Firefox (latest version)
- Microsoft Edge (latest version)
- Apple Safari (latest version)

# Funding

This service was developed as part of the Life Science Database Integration Project of NBDC.

# Site policy

- This site follows the [DBCLS site policy](http://dbcls.rois.ac.jp/policy.html).

