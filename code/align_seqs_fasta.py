#!/usr/bin/env python3

"""
A Python script that reads two DNA sequences from a CSV file.

Calculates the best alignment, and saves the results (best alignment and score) to a file.

The script has two functions, one is calculate_score, which will calculate the result score of two sequences aligment.
The other is reads a FASTA file and extracts the sequence.

If no input files are given, the default files are used.
"""

__author__ = 'Yibin.Li Yibin.Li24@imperial.ac.uk'
__version__ = '0.0.1'

#import sys and os
import sys 
import os

#Base Directory Setup(relative path)
base_dir = "../data/"

# open the file containing the sample data
# if user arguments are given, use those, otherwise use the default files
if len(sys.argv) >= 3: 
    seq1  = os.path.join(base_dir, sys.argv[1])
    seq2  = os.path.join(base_dir, sys.argv[2])
else:
    seq1  = os.path.join(base_dir, "407228326.fasta")
    seq2  = os.path.join(base_dir, "407228412.fasta")

#define a function that reads FASTA files and extracts the DNA sequence
def read_fasta(filename): 
    """
    Designed to read sequences from the given CSV files.
    """   
    with open(filename, 'r') as f: 
        lines = f.readlines()
    sequence = ''.join([line.strip() for line in lines if not line.startswith(">")])    
    return sequence 

#loading and comparing the sequence
seq1 = read_fasta(seq1)
seq2 = read_fasta(seq2)

l1 = len(seq1) 
l2 = len(seq2) 
if l1 >= l2:
    s1 = seq1
    s2 = seq2
else:
    s1 = seq2
    s2 = seq1
    l1, l2 = l2, l1

# define a function to score matches
def calculate_score(s1, s2, l1, l2, startpoint):
    """
    Calculate the result score of two sequences aligment.
    The score is determined by the matching base pairs.
    """
    matched = ""
    score = 0
    for i in range(l2):
        if (i + startpoint) < l1:
            if s1[i + startpoint] == s2[i]: # if the bases match
                matched = matched + "*"
                score = score + 1
            else:
                matched = matched + "-"

    # print results to screen 
    print("." * startpoint + matched) 
    print("." * startpoint + s2)
    print(s1)
    print(score) 
    print(" ")

    return score

# Test the function with some example starting points:
# calculate_score(s1, s2, l1, l2, 0)
# calculate_score(s1, s2, l1, l2, 1)
# calculate_score(s1, s2, l1, l2, 5)

my_best_align = None
my_best_score = -1

# Save output to a txt file
with open('../results/DNA_seq.txt', 'w') as f:
    for i in range(l1):
        score = calculate_score(s1, s2, l1, l2, i)
        if score > my_best_score:
            my_best_align = "." * i + s2
            my_best_score = score
    f.write("Best alignment:\n")
    f.write(f"{my_best_align}\n{s1}\n")
    f.write(f"Best score: {my_best_score}\n")

print(my_best_align)
print(s1)
print("Best score:", my_best_score)