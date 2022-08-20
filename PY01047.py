import math

def prime(n):
    num = int(n[-4:])
    if num < 2:
        return "NO"
    for i in range(2, int(math.sqrt(num))+1):
        if num%i == 0:
            return "NO"
    return "YES"

t = int(input())
for i in range(t):
    n = input()
    print(prime(n))
    