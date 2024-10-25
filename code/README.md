# Oak Species Filtering Script

This script reads a CSV file containing tree species data, identifies species from the **Quercus** genus (oak trees), and writes the filtered results to a separate CSV file. The input file is located in the `../data` directory, and the output will be saved in the `../results` directory. The script is designed to prevent duplicate oak species from appearing in the output.

## Running the Script

**Important:** This script uses relative paths for both input and output files. To ensure the script runs correctly, you **must execute the script from within the `code` folder**. This is necessary because the input data file (`TestOaksData.csv`) is located in the `../data` folder relative to the code, and the results will be saved in the `../results` folder.

# DNA Sequence Alignment Script

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
           



