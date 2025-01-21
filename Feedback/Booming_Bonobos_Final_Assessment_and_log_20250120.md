
# Booming Bonobos Final Assessment and Feedback

---

## Feedback on Project Structure and Workflow

### Strengths:
1. **Directory Structure**:
   - The project followed a clear and logical structure, with folders for `code`, `data`, `results`, and `sandbox`.
   - `.gitignore` was used effectively to exclude temporary files and results.

2. **README File**:
   - The README provided detailed descriptions of scripts and their workflows.
   - Instructions for running scripts and setting up the environment were clear.

### Areas for Improvement:
1. **README**:
   - Include examples of input and expected output for each script to aid usability.
   - Add installation instructions for required R and Python libraries, such as `fuzzywuzzy` and `ggplot2`.

2. **Results Directory**:
   - The `results` folder contained output files, such as `PP_Regress_Loc_Results.csv`, which should not be version-controlled.

---

## Feedback on Scripts and Errors

### General Observations:
1. The scripts were well-documented, with consistent use of comments and docstrings.
2. Error handling was inconsistent across scripts, leading to runtime issues in some cases.

### Script-Specific Feedback:

#### **PP_Regress_Loc.R**
- **Strengths**:
  - Efficiently performed group-specific regression analysis using `tidyverse`.
  - Produced detailed summary statistics, including slopes, intercepts, and p-values.
- **Improvements**:
  - Replace the deprecated `cur_data()` function with `pick()` to avoid warnings.
  - Add inline comments explaining key data wrangling steps.
  - Use `tryCatch` to handle potential errors during linear regression.
- **Issues**:
  - Warnings about "perfect fit" indicate potential data quality issues.

#### **TAutoCorr.R**
- **Strengths**:
  - Implemented permutation tests to analyze autocorrelation effectively.
  - Provided clear and interpretable visualizations.
- **Improvements**:
  - Add explanatory comments for steps such as matrix creation and correlation calculation.
  - Handle missing `KeyWestAnnualMeanTemperature.RData` gracefully with a clear error message.
- **Issues**:
  - Failed due to a missing data file during testing.

#### **align_seqs_fasta.py**
- **Strengths**:
  - The script was modular, with reusable functions like `read_fasta` and `calculate_score`.
  - Clear documentation was provided for each function.
- **Improvements**:
  - Handle cases where the output directory (`../Results`) does not exist.
  - Use logging instead of print statements for debugging.
- **Issues**:
  - Failed due to a missing results directory, causing a `FileNotFoundError`.

#### **oaks_debugme.py**
- **Strengths**:
  - Utilized doctests to validate the `is_an_oak` function.
  - Processed tree species data effectively, filtering oak species and avoiding duplicates.
- **Improvements**:
  - Refine `is_an_oak` to handle edge cases, such as leading/trailing spaces in genus names.
  - Add error handling for missing input files.

#### **Florida-Group.tex**
- **Strengths**:
  - The LaTeX report was well-organized and concise, with clear sections for objectives, methods, and results.
  - Figures were referenced correctly, with appropriate captions and labels.
- **Improvements**:
  - Expand the discussion to include implications of observed autocorrelation on broader climatic trends.

---

## Specific Feedback on Florida Autocorrelation Practical

### Code:
- **Strengths**:
  - The `TAutoCorr.R` script correctly implemented autocorrelation analysis and permutation testing.
  - Visualization outputs were clear and informative.
- **Improvements**:
  - Include functionality to dynamically adjust the number of permutations.
  - Add inline comments explaining key steps in the analysis.
  - Improve error handling for missing data files.

### Write-Up:
- **Strengths**:
  - The LaTeX report provided a thorough analysis of Florida's temperature autocorrelation.
  - Results were presented with statistical rigor, supported by clear visualizations.
- **Improvements**:
  - Discuss broader implications of findings for climate dynamics.

---

## Git Practices

### Strengths:
1. Regular commits demonstrated consistent progress throughout the project.
2. The `.gitignore` file effectively excluded temporary and unnecessary files.

### Areas for Improvement:
1. **Commit Messages**:
   - Many commit messages were vague (e.g., "update"). Use descriptive messages, such as "Refactor regression analysis script to improve clarity."
2. **Contribution Analysis**:
   - **Kaiwen Li** contributed extensively, particularly to regression analysis and merging branches.
   - **Saskia Pearce** made significant contributions to the DNA alignment and README updates.
   - **Tianye Zhang** focused on LaTeX reports and visualizations.
   - **Yibin Li** contributed sporadically, with many minor README updates.

### Recommendations:
1. Adopt a branching strategy for major updates to isolate changes.
2. Use tags to mark milestones, such as `v1.0`, for better version management.

---

## Conclusion
Your team demonstrated good programming and analytical skills. The project was well-structured, and scripts were functional and well-documented. Hopefully this exercise gave you hands-on experience and whetted your appetite for more collaborative development in the future!