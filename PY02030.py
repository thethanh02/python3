from math import sqrt
from typing import Counter


# check prime
N = pow(10, 6)
prime = []
for i in range(N+1):
    prime.append(1)
prime[0] = prime[1] = 0
for i in range(2, int(sqrt(N))+1):
    if prime[i] == 1:
        for j in range(i*i, N+1, i):
            prime[j] = 0

def phan_chia_nguyen_to(a):
    b = []
    coun = Counter()
    for i in a:
        if coun[i] == 0:
            b.append(i)
            coun[i] += 1

    sumList = sum(b)
    sumLeft = 0
    for i in range(len(b)):
        sumLeft += b[i]
        if prime[sumLeft] and prime[sumList - sumLeft]:
            return i
    return 'NOT FOUND'

# init
n = int(input())
a = [int(a) for a in input().split()]
print(phan_chia_nguyen_to(a))