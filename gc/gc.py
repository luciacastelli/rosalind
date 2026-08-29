with open("datasets/rosalind_gc.txt", "r") as file:
    data = file.readlines()

    seqs = {}

    for line in data:
        line = line.strip()
        if '>' in line:
            seq = ""
            seqname = line
        else:
            seq = seq + line
        seqs[seqname] = seq

for key, value in seqs.items():
    percent = 0
    percent = (value.count("G") + value.count("C")) / len(value) * 100
    print(key)
    print(percent)

# Write output file
with open("outputs/gc_out.txt", "w") as file:
    file.write()