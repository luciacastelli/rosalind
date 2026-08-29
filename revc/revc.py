# Complementing a Strand of DNA

with open("in.txt", "r") as in_file, open("out.txt", "w") as out_file:
    s = in_file.readline().strip()
    complementary = {"A": "T", "T": "A", "C": "G", "G": "C"}
    sc = "".join([complementary[base] for base in s[::-1]])
    out_file.write(sc)
