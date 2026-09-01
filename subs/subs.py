# Finding a motif in DNA

with open("in.txt", "r") as in_file:
    lines = in_file.readlines()
    s = lines[0].strip()
    t = lines[1].strip()

indeces = []
substring_length = len(t)

for ix, letter in enumerate(s):
    substring = s[ix:ix+substring_length]

    if len(substring) != substring_length:
        break
    elif substring == t:
        indeces.append(ix + 1)

with open("out.txt", "w") as out_file:
    print(*indeces, file = out_file)
