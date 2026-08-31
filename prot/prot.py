# Translating RNA into protein
import re
import pandas as pd
from sys import exit

# Read infile and verify open reading frame(s)
with open("in.txt", "r") as in_file:
    s = in_file.readline().strip()
    pattern = r"AUG(?:[AUGC]{3})*?(?:UAA|UAG|UGA){1}"

    if orfs := re.findall(pattern, s):
        print(f"{len(orfs)} ORFs found", end = "")
    else:
        exit("No ORFs found.")

# Make conversion table and translate into protein
convert = pd.read_csv("codon_table.csv").set_index("rna_codon")["single_letter"].to_dict()
proteins = []
for orf in orfs:
    protein = ""
    for j in range(0, len(orf) - 3, 3):
        codon = orf[j:j+3]
        protein = protein + convert[codon]
    proteins.append(protein)

with open("out.txt", "w") as out_file:
    out_file.writelines('\n'.join(proteins))
