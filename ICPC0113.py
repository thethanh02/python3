from math import sqrt
from typing import Counter

N = pow(10, 6)
# prime = Counter()
prime = []
for i in range(N+1):
    prime.append(1)
prime[0] = prime[1] = 0
for i in range(2, int(sqrt(N))+1):
    if prime[i] == 1:
        for j in range(i*i, N+1, i):
            prime[j] = 0

def emirp_number(n, limit):
    m = n[::-1]
    if n == m or not prime[int(n)] or not prime[int(m)] or int(m) > limit or int(m) < int(n):
        return False
    return True

t = int(input())
for test in range(t):
    n = int(input())
    for i in range(n):
        if emirp_number(str(i), int(n)):
            print(i, str(i)[::-1], end=' ')
    print()
    