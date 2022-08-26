from math import sqrt
from collections import Counter

N = pow(10, 6)
prime = []
for i in range(N+1):
    prime.append(1)
prime[0] = prime[1] = 0
for i in range(2, int(sqrt(N))+1):
    if prime[i] == 1:
        for j in range(i*i, N+1, i):
            prime[j] = 0


n = input()
a = [int(a) for a in input().split()]
coun = Counter()
for i in a:
    if prime[i]:
        coun[i] += 1
for i in coun.items():
    print(*i)