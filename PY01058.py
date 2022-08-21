from math import sqrt


def prime(n):
    if n < 2:
        return "NO"
    for i in range(2, int(sqrt(n))+1):
        if n%i == 0:
            return "NO"
    return "YES"

t = int(input())
for i in range(t):
    n = input()
    print(prime(int(n[-4:])))