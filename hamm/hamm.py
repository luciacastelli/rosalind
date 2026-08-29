# Counting Point Mutations
# Hamming distance: # of positions where the corresponding symbols are different

with open("in.txt", "r") as in_file, open("out.txt", "w") as out_file:
    hamming = 0
    sequences = [line.strip() for line in in_file]

    for i, nucleotide in enumerate(sequences[0]):
        if nucleotide != sequences[1][i]:
            hamming += 1

    print(hamming, file = out_file)
