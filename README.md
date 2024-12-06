# CMEE Biological Computing Bootcamp - Groupwork tasks

This repository contains the coursework of the Computational Methods in Ecology and Evolution (CMEE) module. Our team consists of the following members:

1.Pearce, Saskia   saskia.pearce21@imperial.ac.uk

2.Li, Kaiwen   kaiwen.li21@imperial.ac.uk

3.Li, Yibin    yibin.li24@imperial.ac.uk

4.Zhang, Tianye  tianye.zhang24@imperial.ac.uk


## Brief Description:

This repository contains the group work coursework element for the Computational Methods in Ecology and Evolution (CMEE). The exercises are based on TheMulQuaBio course notes (https://mhasoba.github.io/TheMulQuaBio/intro.html) from the Biological Computing course at the Department of Life Sciences, Imperial College London.

Project Structure and Usage: The repository contains code scripts located in the Code folder. The Data folder includes input files used by some scripts, while the sandbox folder contains experimental files and is not essential to the main coursework. Output files are generated in the results folder for this week’s coursework.

Project Structure

    Code folder: Contains all scripts.
    Data folder: Includes input files used by scripts.
    Results folder: Stores output files generated by the scripts.
    Sandbox folder: Used for experimental work (not essential for the coursework).

Languages:

    Linux Shell Scripting 
    Python 
    R version 4.4.0 
    python version 3.9 
    

Installation:

To clone this repository, use the following command:
bash
git clone git clone git@github.com:Kaiwen-Li3/CMEE-Group-2-Coursework.git 

Project Structure and Usage:
The repository contains 10 primary scripts located in the Code folder. The Data folder includes input files used by some scripts, while the sandbox folder contains experimental files and is not essential to the main coursework. Output files are generated in the results folder for this week’s coursework.

Overview of the scripts:


## Oak Species Filtering Script

This script reads a CSV file containing tree species data, identifies species from the **Quercus** genus (oak trees), and writes the filtered results to a separate CSV file. The input file is located in the `../data` directory, and the output will be saved in the `../results` directory. The script is designed to prevent duplicate oak species from appearing in the output.

### Running the Script

**Important:** This script uses relative paths for both input and output files. To ensure the script runs correctly, you **must execute the script from within the `code` folder**. This is necessary because the input data file (`TestOaksData.csv`) is located in the `../data` folder relative to the code, and the results will be saved in the `../results` folder.

## DNA Sequence Alignment Script

This script aligns two DNA sequences, identifies the best alignment based on matching bases, and saves the result. It takes DNA sequences from FASTA files, aligns one sequence against the other at various starting points, calculates an alignment score for each, and determines the alignment with the highest score.
Features

Functions

    read_fasta: Reads a DNA sequence from a FASTA file, ignoring the header.
    calculate_score: Aligns two sequences from a given start position and computes the score based on matching bases.

Input

    FASTA files: Two DNA sequences in FASTA format, provided as command-line arguments or default paths (seq1.fasta and seq2.fasta).
        Ensure that the files are in plain text (no .rtf or other extensions).

Output

    The script writes the best alignment and corresponding score to ../Results/DNA_seq.txt.
    Alignment details, including matching positions, are printed to the terminal.

Usage

To run the script, use the following format:

bash

python align_seqs_fasta.py <seq1.fasta> <seq2.fasta>

If no files are provided, the script will use default paths.
Example

Command:

bash

python align_seqs_fasta.py 407228326.fasta 407228412.fasta

Expected Output:

    Terminal display of alignment details with * indicating matching bases and - for mismatches.
    ../Results/DNA_seq.txt file containing the best alignment and score.



/CMEE-Group-2-Coursework/
    └── week3/
        ├── code/
        │   └── oaks_debugme.py
        ├── data/
        │   └── TestOaksData.csv
        └── results/
            └── oaks_debugme_results.csv
           
           
## PP_Regress_Loc.R
Functions

	Analyses predator-prey mass relationships and visualizes these interactions based on feeding interaction type, predator life stage and location where data was collected	
   
Input

	EcolArchives-E089-51-D1.csv: Dataset of predator-prey interactions, as well location data.
    
Output

	key statistics such as slope, intercept, R², p-value, F-statistic, based off feeding interaction type, predator life stage and location iterations. 
    
Usage

	input EcolArchives-E089-51-D1.csv
    
Command

	source("PP_Regress_Loc.R")
	
Expected Output
	
	csv file containing key statistics such as slope, intercept, R², p-value, F-statistic.

Here’s a basic template for the README file:

---

## TAutoCorr.R

### Overview

`TAutoCorr.R` is an R script designed to analyze autocorrelation in time-series data. It employs statistical methods to identify and interpret patterns, providing insights into temporal relationships within datasets.

### Features

- Computes autocorrelation functions for time-series data.
- Visualizes autocorrelation using plots.
- Supports various customizable parameters for detailed analysis.

### Requirements

- R (version 4.0 or higher recommended)
- Required packages:
  - **ggplot2**: For data visualization
  - **forecast**: For time-series analysis
  - Other dependencies as specified in the script

### Usage

1. Clone or download the script to your local machine.
2. Ensure the necessary packages are installed in your R environment.
3. Run the script with your time-series dataset. Modify input file paths and parameters as needed in the script.

### Example

```R
# Example usage in R
source("TAutoCorr.R")
# Customize parameters within the script to match your dataset
```

### Input and Output

- **Input**: The script accepts time-series datasets in formats like `.csv` or data frames loaded into R.
- **Output**: Visualizations of autocorrelation and related statistics are generated.

### Notes

- Ensure your input data is properly formatted (e.g., consistent time intervals).
- Refer to inline comments in the script for guidance on parameter adjustments.


Here’s the README based on your instructions:

---

## Florida-Group.tex

### Overview

`Florida-Group.tex` is a LaTeX file designed for creating a professional document with embedded images. The images are stored using relative paths, ensuring a well-structured and organized project layout.

### Instructions

1. **Set the Working Directory**:  
   Before running `Florida-Group.tex`, ensure that your working directory is set to the `code` folder. This is crucial as the file uses relative paths to reference images.

2. **Image Locations**:  
   - The images used in the document are located in the `data` folder.
   - File names: `1.png` and `2.png`.

3. **Handling Errors**:  
   - If the images fail to load, verify that the `data` folder is correctly placed in the same directory as the `code` folder.
   - As a fallback, a precompiled PDF version of the document is available in the `code` folder.

### Requirements

- A LaTeX distribution installed on your machine (e.g., TeX Live, MikTeX, Overleaf).
- Ensure that the LaTeX compiler supports `graphicx` for image handling.

### Compilation

To compile `main.tex`:
```bash
pdflatex main.tex
```

Ensure that the terminal or LaTeX editor is set to the `code` folder.

