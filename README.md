# metaDrug_figures

This repository contains notebooks to plot the figures associated with the manuscript

*"Combinatorial, additive and dose-dependent drug-microbiome associations"*

Authors: Sofia K. Forslund*, Rima Chakaroun*, Maria Zimmermann-Kogadeeva*, Lajos Markó*, Judith Aron-Wisnewsky*, Trine Nielsen*, <...> The MetaCardis Consortium, <...> Jens Nielsen, Fredrik Bäckhed, S. Dusko Ehrlich, Marc-Emmanuel Dumas, Jeroen Raes, Oluf Pedersen, Karine Clément, Michael Stumvoll, Peer Bork.

Code contributions by: Sofia K. Forslund, Lucas Moitinho-Silva, Thomas S. B. Schmidt, Till Birkner, Maria Zimmermann-Kogadeeva

## Contents:

*All notebook files provided with a source code (.Rmd/.ipynb) in the *source_code* folder and in a .html version with the results available for viewing without running the notebooks.*

- *plot_Figure1ab.Rmd/html*

Figure 1ab: Confounder analysis in drug-host-microbiome associations

- *plot_Figure1c_feature_clustergrams.ipynb/html*

Figure 1c: Hierarchical clustering of drug-feature associations

- *plot_Figure1d.Rmd/html*

Figure 1d: Aspirin-host-microbiome associations

- *plot_Figure1e.Rmd/html*

Figure 1e: SNV analysis results for oral and gut strains in patients taking PPI

- *plot_Figure2a.Rmd/html*

Figure 2a: Drug combinations statistics as barplot

- *plot_Figure2b.Rmd/html*

Figure 2b: Drug combinations graph

- *plot_Figure2cd_drug_combination_features.ipynb.html*

Figure 2cd: Drug combination associations with host and microbiome

- *plot_Figure2E_mediation_graph.ipynb/html*

Figure 2e: Drug combination associations with host and microbiome - example of mediation analysis results

- example_mediation_analysis.py
Python script to perform mediation analysis for the three drug combinations in Figure 2e.

- *plot_Figure3d_dosage.ipynb/html*

Figure 3abs: Associations between long-term antibiotic exposure and microbiome

- *plot_Figure3abc_abxcourses.ipynb/html*

Figure 3d: Heatmap of drug dosage-associated features

- *plot_Figure3ef_enterotypes.ipynb/html*

Figure 3ef: Dosage-associated enterotype features

######################################################
# To run the notebooks, the following input data folder is required: 
Folder *input_data* located in the directory *source_code* containing the files:

- Supplementary_Table_10_2019-09-13434.xlsx
- Supplementary_Table_13_2019-09-13434.xlsx
- Supplementary_Table_14_2019-09-13434.xlsx 
- Supplementary_Table_5_2019-09-13434.xlsx
- Supplementary_Table_6_2019-09-13434.xlsx
- Supplementary_Table_8_2019-09-13434.xlsx
- Supplementary_Tables_1_to_4_2019-09-13434.xlsx
- cmd_dosages_20201210.r
- cmd_drugs_20201210.r
- data_drugs_dict.txt
- drug.indication.tsv
- group_T2D_associations.txt
- hub.enterotype.v1.data.frame.r
- hub.pheno.v8.data.frame.r
- hub.microbiome.summary.down.10000000.r
- hub.motus.SpeciesCluster.down.10000000.r
- snps_ppi_input.txt

All filed are available for download at doi:...

