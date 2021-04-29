# metaDrug_figures

This repository contains notebooks to plot the figures associated with the manuscript

*"Combinatorial, additive and dose-dependent drug-microbiome associations"*

Authors: Sofia K. Forslund*, Rima Chakaroun*, Maria Zimmermann-Kogadeeva*, Lajos Markó*, Judith Aron-Wisnewsky*, Trine Nielsen*, <...> The MetaCardis Consortium, <...> Jens Nielsen, Fredrik Bäckhed, S. Dusko Ehrlich, Marc-Emmanuel Dumas, Jeroen Raes, Oluf Pedersen, Karine Clément, Michael Stumvoll, Peer Bork.

Code contributions by: Sofia K. Forslund, Lucas Moitinho-Silva, Thomas S. B. Schmidt, Till Birkner, Maria Zimmermann-Kogadeeva

## Contents:

*All notebook files provided with a source code (.Rmd/.ipynb) in the *source_code* folder and as a .html version with the results available for viewing without running the notebooks.*

- *PlotFigures.Rproj*

Rproject file associated with the source_code directory to ease navigation within the R notebooks. *Tip: To run source Rmd notebooks, first open the PlotFigures.Rproj file from RStudio environment, and then navigate to the Rmd files in the home directory*. 

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

- *plot_Figure2e_example_mediation_analysis.ipynb/html*

Python script to perform mediation analysis for the three drug combinations in Figure 2e.

- *plot_Figure3abc_abxcourses.ipynb/html*

Figure 3abs: Associations between long-term antibiotic exposure and microbiome

- *plot_Figure3d_dosage.ipynb/html*

Figure 3d: Heatmap of drug dosage-associated features

- *plot_Figure3ef_enterotypes.ipynb/html*

Figure 3ef: Dosage-associated enterotype features

######################################################
# To run the notebooks, the following files are required to be located in the folder *input_data* located in the subdirectory *source_code*:

- Supplementary_Tables_1_to_4_2019-09-13434.xlsx

Supplementary Tables 1 to 4 include information on the cohort characteristics and drug intake with source metadata. Source metadata for the MetaCardis cohort includes disease group, gender, age, study center, body mass index (BMI, kg/m2), alternative healthy eating index (aHEI), diet diversity score (DDS), and dietary approaches to stop hypertension (DASH), physical activity and manual work levels, and smoking status. Source data includes information on the drug intake, drug combinations, dosage and antibiotic use analyzed in the MetaCardis cohort.

- Supplementary_Table_5_2019-09-13434.xlsx

Supplementary Table 5 Multivariate breakdown of variance. The table includes multivariate breakdown of variance for each feature space by each predictor, a summary of all interaction terms in the models, and the results of the confounder analysis for all patient groups analyzed in the MetaCardis cohort. 

- Supplementary_Table_6_2019-09-13434.xlsx

Supplementary Table 6: Features of microbiome, host and metabolome impacted by different drug groups and drug compounds. Results of drug group (or drug compound according to the ATC classification) assessment for its impact on host and microbiome features for each patient group. Compound comparison with Maier et al., Nature 2018, tab shows microbiome features negatively impacted by the drug treatment (for the ATC-level compounds) in at least one patient group, and bacterial species whose growth was inhibited by the same drug in the in vitro experiment.

- Supplementary_Table_8_2019-09-13434.xlsx

Supplementary Table 8: Features of microbiome, host and metabolome impacted by different drug combinations. Analysis of the effect of drug combinations, assessed for impact on host and microbiome falling within different measurement categories in each patient group. 

- Supplementary_Table_10_2019-09-13434.xlsx

Supplementary Table 10. Mediation analysis of host and microbiome features for drug intake, dosage and combinations. Mediation analysis via a regression model of drug effect on each host feature mediated through a microbiome feature or vice versa. 

- Supplementary_Table_13_2019-09-13434.xlsx

Supplementary Table 13. Features of microbiome, host and metabolome impacted by different drug dosages. Results of drug dosage assessment for its impact on host and microbiome features falling within different measurement categories for each patient group. Both dosage-confirmed (the effect was identified both from drug intake status and relative drug dosage analysis) and dosage-unique (the effect was revealed only by relative dosage analysis) effects are shown.

- Supplementary_Table_14_2019-09-13434.xlsx 

Supplementary Table 14. Significant impacts on enterotype distribution based on disease status and medication variables. The table includes clinical status (patient vs healthy control comparisons), CMD or antibiotic drug status or dosage, or intake of drug combinations, shown for each enterotype versus the other three enterotypes in the four-enterotype classification.

- snps_ppi_input.txt

File containing the information on effect size and statistic of association between the abundance of selected [potentially] oral strains and PPI intake across patient groups.

- data_drugs_dict.txt

File containing the mapping between drug IDs in the metadata table and drug names and variable type.

- drug.indication.tsv

File containing the mapping between drug name and indication.

- example_feature_table.csv

File with source data on host and microbiome feature values per sample.

- group_T2D_associations.txt

File containing all associations between drugs and features in T2D group (both significant and non-significant).

- hub.enterotype.v1.data.frame.r

File with source data on enterotype classification of each sample.

- hub.pheno.v8.data.frame.r

File with source data on phenotype features in each sample.

- hub.microbiome.summary.down.10000000.r

File with source data on summary microbiome features per sample (such as gene richness, abundance of antibiotic resistance genes, etc.)

- hub.cellcount.motu.Species.v2.data.frame.r

File with source data on microbial species abundances estimated with mOTU software.

The *input_data* folder is available for download at:

