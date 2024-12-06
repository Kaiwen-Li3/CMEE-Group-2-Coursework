**CMEE Coursework Week 3**

This repository contains the coursework for **Week 3** of the Computational Methods in Ecology and Evolution (CMEE) module. Our team consists of the following members:

1.Pearce, Saskia   saskia.pearce21@imperial.ac.uk
2.Li, Kaiwen   kaiwen.li21@imperial.ac.uk
3.Li, Yibin    yibin.li24@imperial.ac.uk
4.Zhang, Tianye  tianye.zhang24@imperial.ac.uk

**Tasks Overview**

**Task 1: Oak Species Identification**
The first task involves identifying tree species from a dataset, specifically focusing on species belonging to the 'Quercus' genus (oak trees). The code for this task can be found in the file oaks_debugme.py within the code folder.

The script reads input from a CSV file located in the data folder.
It checks each species to determine if it belongs to the 'Quercus' genus.
The results, including the identified oak species, are written to a CSV file in the results folder.

**Task 2: Sequence Alignment**

The second task is about aligning two DNA sequences from FASTA files. The relevant code is in align_seqs_fasta.py, which is also located in the code folder.

The script processes two input FASTA files from the data folder.
It aligns the sequences using a scoring system and outputs the best alignment to a file in the results folder.

**Important Note**
To ensure the scripts run correctly, please make sure to change your working directory (cd) to the code folder before executing the scripts, as we have used relative paths for accessing the data and output files.

**Task 3: PP_Regress_Loc**

This task analyses predator-prey mass relationships and visualizes these interactions based on feeding interaction type, predator life stage and location where data was collected, from the EcolArchives-E089-51-D1.csv dataset. The dataset is found in data, and the code in code. A CSV is saved in the results folder containing key statistics such as slope, intercept, R², p-value, F-statistic, based off feeding interaction type, predator life stage and location iterations. 

**Task 3: PP_Regress_Loc.R**

This task analyses predator-prey mass relationships and visualizes these interactions based on feeding interaction type, predator life stage and location where data was collected. The code for this task is found in the code file, and the data 'EcolArchives-E089-51-D1.csv' in the data file. 

The script outputs key statistics such as slope, intercept, R², p-value, F-statistic, based off feeding interaction type, predator life stage and location iterations, in a csv file in results called: PP_Regress_Loc_Results.csv.


