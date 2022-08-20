import math

t = int(input())
for i in range(t):
    n = int(input())
    d = 0
    print(1, end="")
    for i in range(2, n+1):
        d = 0
        while n % i == 0:
            d += 1
            n /= i
        if d >= 1:
            print(end=" * ")
            print(i, end="^") 
            print(d, end="")
    print()