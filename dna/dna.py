# Counting DNA Nucleotides

with open("in.txt", "r") as in_file, open("out.txt", "w") as out_file:
    sequence = in_file.readline()
    counts = [sequence.count(base) for base in "ACGT"]
    print(*counts, file = out_file)
