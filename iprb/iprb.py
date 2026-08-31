# Mendel's first law
# Given: a population of k (AA), m(Aa), and n(aa) organisms
# Return: probability that two randomly selected mates produce offspring with an A allele
# Can be solved using Hypergeometric distributions
from sys import argv

def main():
    k, m, n = map(int, (argv[1], argv[2], argv[3]))
    t = k + m + n
    p = k / t + ((m + n) * k + 0.75 * (m - 1) * m + m * n)  / (t * (t-1))
    print(p)

if __name__ == "__main__":
    main()
