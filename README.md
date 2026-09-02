# Rosalind — Bioinformatics Stronghold

Solutions to the "Bioinformatics Stronghold" problems from [Rosalind](https://rosalind.info/), written in Python. This repository is a work in progress: problems will be added as I solve them.

## Repository Structure

Each Rosalind problem has its own directory:

```text
rosalind/
├── dna/
│   ├── dna.py
│   ├── in.txt
│   └── out.txt
├── rna/
│   ├── rna.py
│   ├── in.txt
│   └── out.txt
├── prot/
│   ├── prot.py
│   ├── in.txt
│   └── out.txt
├── ...
└── README.md
```

* `<problem>/<problem>.py` — Python solution
* `in.txt` — Rosalind problem input, when applicable
* `out.txt` — expected/output result, when applicable

Some problems may only contain the Python solution if an input/output file is not needed.

## Problems

### Bioinformatics Stronghold

| Problem | Description                      | Solution           |
| ------- | -------------------------------- | ------------------ |
| DNA     | Counting DNA Nucleotides         | [`dna/`](./dna/)   |
| RNA     | Transcribing DNA into RNA        | [`rna/`](./rna/)   |
| REVC    | Complementing a Strand of DNA    | [`revc/`](./revc/) |
| FIB     | Rabbits and Recurrence Relations | [`fib/`](./fib/)   |
| GC      | Computing GC Content             | [`gc/`](./gc/)     |
| HAMM    | Counting Point Mutations         | [`hamm/`](./hamm/) |
| IPRB    | Mendel's First Law               | [`iprb/`](./iprb/) |
| PROT    | Translating RNA into Protein     | [`prot/`](./prot/) |
| SUBS    | Finding a Motif in DNA           | [`subs/`](./subs/) |
| FIBD    | Mortal Fibonacci Rabbits         | [`fibd/`](./fibd/) |

*The table will be expanded as I solve more problems.*

## Goals

* Practice problem solving in Python
* Perform biological sequence analysis programmatically
* Understand common bioinformatics concepts and algorithms
* Document my progress
* Provide guidance to whomever may need it
