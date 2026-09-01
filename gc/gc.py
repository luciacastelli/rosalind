# Computing GC content
from re import search
from sys import exit

sequences = {}

with open("in.txt", "r") as file:
    for line in file:
        if matches := search(r"^>(Rosalind_\d{4})", line.strip()):
            sequence_name = matches.groups(1)[0]
            sequences[sequence_name] = ""
        else:
            sequences[sequence_name] += line.strip()

for name, seq in sequences.items():
    percent = (seq.count("G") + seq.count("C")) / len(seq) * 100
    sequences[name] = percent

with open("out.txt", "w") as file:
    i = 0
    for key, value in sorted(sequences.items(), key = lambda item: item[1], reverse = True):
        if i == 1:
            exit()
        file.write(f"{key}\n{value}\n")
        i += 1
