# Transcribing DNA into RNA

with open("in.txt", "r") as in_file, open("out.txt", "w") as out_file:
    dna = in_file.readline()
    out_file.write(dna.replace("T", "U"))