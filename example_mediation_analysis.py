# -*- coding: utf-8 -*-
"""
Created on Thu Apr 22 17:08:12 2021

Example mediation analysis for the host and microbiome features.
Mediation is modelled accordint to the statsmodels.stats.mediation package:
Basic mediation analysis with regression model accordint to [1].

The outcome model 
outcome_model: "FeatureValue_1 ~ Drug + FeatureValue_2"

is tested against mediator model

mediator_model: "FeatureValue_2 ~ Drug", 

where FeatureValue1 and FeatureValue2 are associated with the Drug treatment.                                                  

Mediation analysis is performed in both directions 
(FeatureValue1 is tested as mediator and FeatureValue2 is tested as mediator).

The script crreates mediation results dataframe and saves it to file. 

[1] Imai, Keele, Tingley (2010). A general approach to causal mediation analysis. 
Psychological Methods 15:4, 309-334. 
http://imai.princeton.edu/research/files/BaronKenny.pdf
@author: mazimmer
"""

# load necessary libraries
import pandas as pd
import numpy as np
from scipy import stats
import statsmodels.api as sm
from statsmodels.stats.mediation import Mediation

##########################################################
fileFolder = './input_data/'

# prepare file names to download: phenotype, drug and feature information
hubfilePhenotype = 'hub.pheno.v8.data.frame.r'
hubfileDrug = 'cmd_drugs_20201210.r'
featureFile = 'example_feature_table.csv'
# supplementary table 8 to filter features affected by drug combinations
fileName = 'Supplementary_Table_8_2019-09-13434.xlsx'


# read file names with features
features_df = pd.read_csv(fileFolder + featureFile, sep=',', index_col=0)

# read phenotype and drug files
featuresPheno = pd.read_csv(fileFolder + hubfilePhenotype, sep='\t')
featuresDrug = pd.read_csv(fileFolder + hubfileDrug, sep='\t')

# create dataframe with sample - group
featuresGroup = featuresPheno[['SampleID', 'Group']]
featuresGroup = featuresGroup.drop_duplicates()
featuresGroup = featuresGroup.set_index('SampleID', drop=True)

##################################################################

# read drug combination features files

sheetName = 'Data'
drugCombinationEffect = pd.read_excel(fileFolder + fileName,
                           sheet_name = sheetName)

#######################################
# select drug combinations and condition for which to perform analysis
drug_pairs = [['STATINE_C', 'METFORMIN_C'],
              ['STATINE_C', 'ASA_C'],
              ['STATINE_C', 'CA2_CBL_C']]

drug_pairs_names = [['Statin', 'Metformin'],
                    ['Statin', 'Aspirin'],
                    ['Statin', 'Calcium antagonist']]

cursampleset = '3' #T2D

# perform mediation analysis for each drug pair
feat_names1 = []
feat_names2 = []
featcorr_DrugFeat = []
featcorrP_DrugFeat = []
featcorr_1_2 = []
featcorrP_1_2 = []
feat_medres = [] 
feat_drugcombo = []

for drug_i in range(len(drug_pairs)):
    drug_name1 = drug_pairs[drug_i][0]
    drug_name2 = drug_pairs[drug_i][1]
    
    # extract dataframe for current drug 
    drug_df = featuresDrug[[item for item in featuresDrug.columns 
                              if (drug_name1 in item) |
                                 (drug_name2 in item)]].copy()
    drug_df.index = featuresDrug['SampleID']
    # column Drug contains combination
    drug_df['Drug'] = drug_df.iloc[:,0] * drug_df.iloc[:,1]
    # overlap with phenotype 
    drug_df = drug_df.loc[featuresGroup.index]
    drug_df['Group'] = featuresGroup.loc[drug_df.index,'Group']
    
    #############################
    # get feature names that are changing in this combination
    associated_features = drugCombinationEffect[(drugCombinationEffect['Effector'].str.find(drug_pairs_names[drug_i][0])>=0) &
                                                (drugCombinationEffect['Effector'].str.find(drug_pairs_names[drug_i][1])>=0) &
                                                (drugCombinationEffect['Sample set'].str.find(cursampleset)>=0)].copy()
    selected_features = list(set(associated_features['Feature display name']).intersection(features_df.columns))
    #############################
    
    print('Running mediation analysis for combination ', drug_name1, ' and ', drug_name2, ' in ', cursampleset)
    
    
    for i in range(len(selected_features)):
        feat1name = selected_features[i]
        for j in range(i+1, len(selected_features)):
            
            feat2name = selected_features[j]
            print('Performing mediation analysis for ', feat1name, ' and ', feat2name)
            # add features to drug df
            drugmediation_df = pd.concat([drug_df, features_df.loc[:,[feat1name,feat2name]]], axis=1)
            # select only patients from one group
            testdata = drugmediation_df[drugmediation_df['Group']==cursampleset].copy()
            # reaplce nans with 0
            testdata = testdata.fillna(0)
            # doublecheck that feature values are numeric
            testdata[feat1name] = pd.to_numeric(testdata[feat1name])
            testdata[feat2name] = pd.to_numeric(testdata[feat2name])
            
            #rename columns to generic for easier formula definition for mediation analysis
            testdata.columns = [item.replace(feat1name, 'FeatureValue_1') for item in testdata.columns]
            testdata.columns = [item.replace(feat2name, 'FeatureValue_2') for item in testdata.columns]
            
            # change drug from boolean to 0 and 1
            testdata['Drug'] = [1 if testdata['Drug'].iloc[i]==True else 0 for i in range(len(testdata))]
            # model feature 1 as mediator
            outcome_model = sm.OLS.from_formula("FeatureValue_1 ~ Drug + FeatureValue_2",
                                                data = testdata)
            mediator_model = sm.OLS.from_formula("FeatureValue_2 ~ Drug",
                                                  data = testdata)
    
            med = Mediation(outcome_model, mediator_model, "Drug", "FeatureValue_2")
    
            med_result = med.fit(n_rep = 100)
            res = med_result.summary()
            # save results
            feat_names1.append(feat1name)
            feat_names2.append(feat2name)
            feat_medres.append(res) 
            #model feature 2 as mediator
            outcome_model = sm.OLS.from_formula("FeatureValue_2 ~ Drug + FeatureValue_1",
                                        data = testdata)
            mediator_model = sm.OLS.from_formula("FeatureValue_1 ~ Drug",
                                                  data = testdata)
    
            med = Mediation(outcome_model, mediator_model, "Drug", "FeatureValue_1")
    
            med_result = med.fit(n_rep = 100)
            res = med_result.summary()
            # save results
            feat_names1.append(feat2name)
            feat_names2.append(feat1name)
            feat_medres.append(res) 
    
            # calculate correlations
            res = stats.spearmanr(testdata['Drug'], testdata['FeatureValue_1'])
            featcorr_DrugFeat.append(res[0])
            featcorrP_DrugFeat.append(res[1])
    
            res = stats.spearmanr(testdata['Drug'], testdata['FeatureValue_2'])
            featcorr_DrugFeat.append(res[0])
            featcorrP_DrugFeat.append(res[1])
    
            res = stats.spearmanr(testdata['FeatureValue_1'], testdata['FeatureValue_2'])
            featcorr_1_2.append(res[0])
            featcorrP_1_2.append(res[1])
    
            res = stats.spearmanr(testdata['FeatureValue_2'], testdata['FeatureValue_1'])
            featcorr_1_2.append(res[0])
            featcorrP_1_2.append(res[1])
            
            feat_drugcombo.append('Combination: ' + drug_name1 + ', ' + drug_name2)
            feat_drugcombo.append('Combination: ' + drug_name1 + ', ' + drug_name2)

# compile dataframe with mediation results
medres_df = []
for i in range(len(feat_medres)):
    df = feat_medres[i].copy()
    df = pd.melt(df.assign(index=df.index), id_vars=['index'])
    df = pd.DataFrame(np.reshape(df['value'].values,(1,np.shape(df)[0])),
                  columns=df['index']+'_'+df['variable'])
    if i==0:
        medres_df = df
    else:
        medres_df = pd.concat([medres_df, df])

medres_df['Feature1'] = feat_names1
medres_df['Feature2_med'] = feat_names2
        
medres_df['FeatureDrugCorr'] = featcorr_DrugFeat
medres_df['FeatureDrugCorrP'] = featcorrP_DrugFeat
medres_df['FeatureFeatureCorr'] = featcorr_1_2
medres_df['FeatureFeatureCorrP'] = featcorrP_1_2
medres_df['Effector'] = feat_drugcombo
medres_df['Sample set'] = cursampleset
    
###############################
# select a subset of columns to print to file
medres_df = medres_df[['Effector',                  # drug combination pair
                       'Sample set',                # patient group
                       'Feature1', 'Feature2_med',  # Feature (1) and mediator (2)
                       'ACME (average)_Estimate',   # Average estimate of mediated effect
                       'ADE (average)_Estimate',    # Average estimate of direct drug effect
                       'Total effect_Estimate',     # Estimate of total effect
                       'ACME (average)_P-value',    # P-value of mediated effect
                       'ADE (average)_P-value',     # P-value of direct drug effect
                       'Total effect_P-value',      # P-value of total effect
                       'FeatureDrugCorr', 'FeatureDrugCorrP',   # Pearson corr and p-value between drug and Feature 1
                       'FeatureFeatureCorr', 'FeatureFeatureCorrP']] #Pearson corr and p-value between Feature 1 and Feature 2
medres_df.to_csv(fileFolder  + 'mediation_results_drug_combination.csv', index=0)
    
