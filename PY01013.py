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
    x, y = [int(x) for x in input().split()]
    z = str(math.gcd(x, y))
    sum = 0
    for i in range(len(z)):
        sum += int(z[i])
    print(prime(sum))