English | [日本語](examples_ja.md)

# Examples
## Case 1: Investigate the development status of drugs targeting genes/proteins that show a similar expression pattern

##### Update history
 - Created 2023-03-15
 - Updated 2023-03-24

### Purpose
- Obtain the list of human proteins for which tissue-specific high gene expression has been observed in the lung and intestine, which are localized on the plasma membrane as proteins, for which data exist from a method that detects a direct interaction between the protein and some compound, and which are related to compounds that are effective against "infections"

### Background
- ACE2 and TMPRSS2 are known as proteins that play an important role when the SARS-CoV-2 virus, which causes COVID-19, enters cells. Therapies and preventive measures targeting these proteins are therefore being studied.
    - [ACE2 (Angiotensin-converting enzyme 2)](https://www.uniprot.org/uniprotkb/Q9BYF1/): ACE2 is the receptor that the SARS-CoV-2 virus needs in order to enter human cells. This receptor is present mainly on the surface of cells of the lung, small intestine, heart, kidney and so on. The SARS-CoV-2 virus enters cells by binding to ACE2 and causes infection.
    - [TMPRSS2 (transmembrane serine protease 2)](https://www.uniprot.org/uniprotkb/O15393/): TMPRSS2 is a protein required for the fusion of the SARS-CoV-2 virus and helps the virus enter cells. Like ACE2, TMPRSS2 is present mainly on the surface of cells of the lung, small intestine and so on. The SARS-CoV-2 virus first binds to ACE2 and then enters the cell with the help of TMPRSS2.
- Taking as a clue the fact that ACE2 and TMPRSS2 are highly expressed on the plasma membrane of the cells that make up the lung and small intestine, we comprehensively examine how many drugs (or drug candidates) have been developed that target genes/proteins showing a similar expression pattern.

### Exploration conditions and their intent
- [Configuration file for reproducing these search conditions](https://raw.githubusercontent.com/togodx/togodx-config-human/develop/docs/togodx-preset_example_case1.json)

#### Select target dataset
- `UniProt`
    - Since what we finally want to output is a list of protein IDs, select `UniProt`, a protein database
  
#### Filtering

- `Gene` / `Tissue-specific high expression (HPA)` / `Lung`
    - Genes found to be highly expressed in "Lung" among the 37 tissues studied in [The Human Protein Atlas project (HPA)](https://www.proteinatlas.org/), a project that maps all the human proteins in human cells, tissues and organs by integrating various omics technologies (236 genes)
- `Gene` / `Tissue-specific high expression (HPA)` / `Intestine`
    - Genes found to be highly expressed in "Intestine" among the 37 tissues studied in HPA (758 genes)
- `Protein` / `cellular component` / `cellular anatomical entity` / `membrane` / `plasma membrane`
    - Proteins known to be localized to the "plasma membrane", among the functional annotations (GO terms) in the Cellular component category of the [Gene Ontology (GO) annotations that UniProt assigns to each human protein together with their evidence](https://www.uniprot.org/help/gene_ontology) (7,400 proteins)
- `Interaction` / `ChEMBL assay existence` / `Conf-score 9: Direct single protein target assigned`
    -  Proteins for which, for the UniProt entry, a method that detects a direct interaction between the protein and a compound (a ChEMBL assay) exists, and for which the highest confidence (Direct single protein target assigned) among the [confidence scores](https://chembl.gitbook.io/chembl-interface-documentation/frequently-asked-questions/chembl-data-questions#what-is-the-confidence-score) given to the relationship between assay and target has been assigned (3,388 proteins)
- `Compound` / `Drug indication` / `Infections`
    - ChEMBL compounds with an indication for "Infections" in the classification of drug indications based on the MeSH (Medical Subject Headings) thesaurus (2,041 compounds)

#### Projection
- `Structure` / `Structure data existence` 
    - Lets you distinguish, for each UniProt entry, whether protein 3D structure data exist in PDB. Structures of the same protein may have been determined under different conditions.
- `Compound` / `Max drug development phase` 
    - ChEMBL compounds include information on drugs approved for the treatment of a specific disease/diagnosis (indication) in some region of the world, and on clinical candidate drugs whose indications are being investigated in the clinical trial process. This is a classification based on the maximum development phase of the compound across all indications (research stage, Phase 1–3, post-marketing).

### Results, discussion and applications
- A list of `97` proteins (UniProt) was obtained.
    - Human proteins for which tissue-specific high gene expression has been observed in the lung and intestine, which are localized on the plasma membrane as proteins, for which data exist from a method that detects a direct interaction between the protein and some compound, and which are related to compounds that are effective against "infections"
- ![Example case-1 view results](https://raw.githubusercontent.com/togodx/togodx-config-human/develop/docs/img/20230804_example_case1_viewresults.png)

#### Example interpretation of the obtained list
- This list includes [ACE2](https://www.uniprot.org/uniprot/Q9BYF1) and [TMPRSS2 (TMPS2 in the list)](https://www.uniprot.org/uniprotkb/O15393/).
    - The SARS-CoV-2 virus is known to target ACE2 and TMPRSS2, but this list can prompt you to **examine their relation to the other proteins that co-occurred** under this combination of search conditions, or, if a respiratory or digestive disease caused by a different virus spreads in the future, to **consider this list of proteins as candidate targets of that virus**.
    - In fact, [DPP4 (Dipeptidyl peptidase 4)](https://www.uniprot.org/uniprotkb/P27487/entry), the receptor used when the Middle East respiratory syndrome coronavirus (MERS-CoV), which is related to the SARS-CoV-2 virus, infects cells, is known to be expressed mainly in pneumocytes of the lung, multinucleated epithelial cells, bronchial submucosal gland cells, epithelial cells of the kidney and small intestine, and activated leukocytes ([ref](https://doi.org/10.1038/nature12005)), and it is included in this list.
- Relations between proteins and drugs shown in the list
    - ACE2 and [RIFAMPIN: CHEMBL374478](https://www.ebi.ac.uk/chembl/compound_report_card/CHEMBL374478/)
        - - ![Example case-1 ACE2](https://raw.githubusercontent.com/togodx/togodx-config-human/develop/docs/img/20230804_example_case1_ACE2.png)
        - Rifampicin, discovered in 1965, was approved in the United States in 1971 and is on the World Health Organization (WHO) Model List of Essential Medicines.
        - Rifampicin is an antiviral drug that inhibits the transformation of cells by viruses, and is widely used as a generic drug that is very inexpensive compared with other modern antiviral drugs.
        - A recent *in-silico* analysis has shown that rifampicin is one of the most promising existing drugs that could be repurposed for the treatment of coronavirus disease ([ref](https://doi.org/10.5501%2Fwjv.v11.i2.90)).
    - TMPRSS2 and [CAMOSTAT: CHEMBL590799](https://www.ebi.ac.uk/chembl/compound_report_card/CHEMBL590799/)
        - - ![Example case-1 TMPRSS2](https://raw.githubusercontent.com/togodx/togodx-config-human/develop/docs/img/20230804_example_case1_TMPRSS2.png)
        - Camostat is classified as a serine protease inhibitor and suppresses the expression of TMPRSS2.
        - Camostat was developed in Japan as a treatment for conditions such as acute pancreatitis and has already been prescribed in Japan for many years. Sufficient clinical data on its safety have been accumulated, so clinical trials can be carried out promptly.
        - Camostat has progressed to Phase 3 as a treatment for SARS-CoV-2, and it has also been confirmed that combining it with a cathepsin B inhibitor reduces the efficiency of SARS-CoV-2 infection ([ref](https://www.cell.com/molecular-therapy-family/nucleic-acids/fulltext/S2162-2531(21)00259-6)).

---

## Case 2: List the genes related to a specific disease and obtain the compounds that may interact with their proteins

##### Update history
 - Created 2023-07-25

### Purpose
After listing the human genes involved in "retinitis pigmentosa", we narrow them down to those whose orthologous genes are conserved in zebrafish, and examine their phenotypes and the compounds that may interact with their proteins.

### Background
Retinitis pigmentosa is one of the designated intractable diseases in Japan and no treatment has been established, but one possible research approach is a screening experiment for drug candidates using a model organism (zebrafish) ([reference](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8425951/)). Here we explore data focusing on retinitis pigmentosa and its related phenotypes.

### Exploration conditions and their intent
- [Configuration file for reproducing these search conditions](https://raw.githubusercontent.com/togodx/togodx-config-human/develop/docs/togodx-preset_example_case2.json)

#### Select target dataset
- `Ensembl gene`
  - Since we want to create a list that summarizes the information per gene, select `Ensembl gene`, a gene database

#### Filtering
- `Protein` / `Disease-related proteins`
  - Retinitis pigmentosa
  - Congenital stationary night blindness
  - Cone-rod dystrophy
  - Leber congenital amaurosis
- `Gene` / `Tissue-specific high expression (HPA)`
  - Retina
- `Gene` / `Ortholog existence`
  - Zebrafish (Danio rerio)
    - Assuming zebrafish as a model organism for retinal diseases, the existence of an ortholog is specified as a condition

#### Projection
- `Compound` / `Max drug development phase`
  - Extracts the related compounds
- `Disease` / `Phenotypic abnormality`
  - Extracts the related phenotypes

### Results and discussion

#### Results
- 42 human genes related to the specified diseases that also have an ortholog in zebrafish were obtained.

#### Example interpretation of the obtained list
- Interpretation of the phenotypes of the obtained group of genes
  - Pressing Result lists the results, with histograms of the hit rates displayed above them. Among them, the hit rate of "Abnormality of the eye" stands out, suggesting that, as a phenotype, the extracted group of genes causes some abnormality of the eye.
![]()
- Interpretation of the compounds that may interact with the proteins related to the obtained group of genes
  - 935 compounds were obtained, of which 46 have reached Phase IV trials (post-marketing clinical trials). Because there are many related genes and the phenotypes are diverse, it is difficult to judge from these exploration results whether the obtained compounds are effective against the disease, but at least for CHEMBL91 (Miconazole), the experiments in the reference above also showed that it is effective as a neuroprotective agent against retinitis pigmentosa.


---

## Case 3: Starting from an example of drug repositioning, compare the indications of the drug in terms of similarity and so on

##### Update history
 - Created 2023-07-25
  
### Purpose and background
Fluoxetine ("Fluoxetine hydrochloride (ChEMBL: CHEMBL1201082)") was initially used as a drug for "Major Depressive Disorder (MDD)", but later came to be applied also to "premenstrual syndrome (PMS), Premenstrual dysphoric disorder (PMDD)". It is still used today as a treatment for both diseases. In this example, we use TogoDX/Human to explore fluoxetine comprehensively and consider why the repositioning was possible.

### Exploration conditions and their intent
- [Configuration file for reproducing these search conditions](https://raw.githubusercontent.com/togodx/togodx-config-human/develop/docs/togodx-preset_example_case3.json)

#### Select target dataset
- `ChEMBL compound`
  - Select the database of the IDs to enter in Map your IDs

#### Map your IDs
- Map fluoxetine, "Fluoxetine hydrochloride (ChEMBL: CHEMBL1201082)"

#### Filtering
From the mapped results, select the categories of interest and perform Filtering
- `Disease` / `Phenotypic abnormality`/`Abnormality of the nervous system`
  - Select the phenotypes related to fluoxetine
- `Disease` / `Disease in Mondo`/`human disease`
  - Select the disease names related to fluoxetine
- `Gene` / `Gene biotype`/`protein coding`
  - Select the genes related to fluoxetine

#### Projection
- `protein`/`Disease-related proteins`
  - Since multiple items are mapped, use Projection to see the ratios

### Results and discussion

#### Results
With fluoxetine as the key, information was obtained on the related diseases (4), phenotypes (5), genes (16) and proteins (16).

#### Example interpretation of the obtained list
- On the related diseases and phenotypes obtained
  - All the phenotypes related to fluoxetine were hits under "Abnormality of the nervous system". This suggests that fluoxetine has some effect on abnormalities of neurotransmission. Since diseases in which "depressive symptoms" are seen were extracted as related diseases, it can be inferred that fluoxetine acts on "depressive symptoms".
- On the related genes obtained
  - Genetic studies have identified several genes and genetic variants that may be associated with depressive symptoms, and these genes are often involved in the regulation of neurotransmitters in the brain and in the function of neural circuits. In particular, genes related to neurotransmitters such as serotonin, dopamine and noradrenaline have been suggested to be associated with depressive symptoms. The obtained gene list included genes that appear to be deeply involved in "depressive symptoms", such as the SLC6A4 gene (serotonin transporter gene) and the HTR1A gene (serotonin 1A receptor, or 5-HT 1A receptor).
  - Papers on MDD and PMDD recommend the use of "selective serotonin reuptake inhibitors (SSRIs)", and fluoxetine is one of the SSRIs. "Depressive symptoms" are among the characteristic symptoms of both MDD and PMDD, and since serotonin is heavily involved in the occurrence of depressive symptoms, the use of SSRIs can be expected to relieve the symptoms. Both MDD and PMDD are mental disorders, and "depressive symptoms" are one of their features. It can therefore be considered that fluoxetine was effective in "improving depressive symptoms".

