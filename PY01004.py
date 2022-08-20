import math

def prime(x):
    if(x < 2): 
        return "NO"
    for i in range(2, int(math.sqrt(x)) + 1):
        if(x % i == 0): 
            return "NO"
    return "YES"

t = int(input())
for i in range(t):
    n = int(input())
    count = 0
    for j in range(1, n):
        if(math.gcd(j, n) == 1): count+=1
    print(prime(count))