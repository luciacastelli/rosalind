# Rabbits and recurrence relations

def fibonacci(n, k): # returns number of pairs (k) at given month (n)
    if n <= 2:
        return 1
    
    previous = 0
    current = 1

    for i in range(2, n + 1):
        previous, current = current, previous * k + current
        print(i, current)

    return current

def main():
    print(fibonacci(6, 3))

if __name__ == "__main__":
    main()
