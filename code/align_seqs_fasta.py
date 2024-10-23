import sys

# Function to read FASTA file and return the sequence as a string
def read_fasta(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()[1:]  # Skip the header (first line)
        return ''.join([line.strip() for line in lines])

# Determine input files: Use command line arguments if provided, otherwise default
if len(sys.argv) == 3:
    seq1_file = sys.argv[1]
    seq2_file = sys.argv[2]
else:
    print("No arguments provided, defaults used")
    seq1_file = '../../week3/data/407228412.fasta'
    seq2_file = '../../week3/data/407228326.fasta'

# Read sequences from files
s1 = read_fasta(seq1_file)
s2 = read_fasta(seq2_file)

# Assign the longer sequence to s1, and the shorter to s2
if len(s2) > len(s1):
    s1, s2 = s2, s1

l1, l2 = len(s1), len(s2)
print(f"Length of longer sequence: {l1}")
print(f"Length of shorter sequence: {l2}")

# Define function to calculate match score from a given startpoint
def calculate_score(s1, s2, startpoint):
    score = sum(1 for i in range(len(s2)) if s1[startpoint + i] == s2[i])
    return score

# Find the best alignment and score
best_score = -1
best_alignment = ""

for i in range(l1 - l2 + 1):  # Loop over possible alignment startpoints
    score = calculate_score(s1, s2, i)
    if score > best_score:
        best_score = score
        best_alignment = "." * i + s2  # Align s2 with s1 starting at position i

# Output results
print("Best alignment is:")
print(f"Best score: {best_score}")
print(best_alignment)
print(s1)

# Save results to file
output_file = "../results/Best_Alignment.csv"
with open(output_file, 'w') as f:
    f.write(f"Best alignment is:\nBest score: {best_score}\n{best_alignment}\n{s1}\n")

print(f"Results saved to {output_file}")
