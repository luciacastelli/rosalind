# Rabbits and recurrence relations
from functools import lru_cache

@lru_cache # memoization (dynamic programming)
def fibonacci(n, k): # returns number of pairs at given month
    if n <= 2:
        return 1
    else:
        return (fibonacci(n - 1, k) +  k * fibonacci(n - 2, k))

def main():
    print(fibonacci(36, 4))

if __name__ == "__main__":
    main()