# Mortal Fibonacci Rabbits
from sys import argv

# Returns pairs after n-th month if all rabbits live for k months
def mortal_fibonacci(n, k):
    populations = {0:1, 1:1, 2:1} # populations[0] = 1 for mathematical convenience
    for i in range(3, n + 1):
        die = 0 if i <= k else populations[i-k-1]
        populations[i] = populations[i-1] + populations[i-2] - die
    return populations[n]
    
def main():
    print(mortal_fibonacci(int(argv[1]), int(argv[2])))

if __name__ == "__main__":
    main()
