from math import sqrt

# check prime
N = pow(10, 3)
prime = []
for i in range(N+1):
    prime.append(1)
prime[0] = prime[1] = 0
for i in range(2, int(sqrt(N))+1):
    if prime[i] == 1:
        for j in range(i*i, N+1, i):
            prime[j] = 0

# init
n = int(input())
a = [int(a) for a in input().split()]
listPrime = []

for i in a:
    if prime[i]:
        listPrime.append(i)

listPrime.sort()
for i in reversed(range(n)):
    if prime[a[i]]:
        a[i] = listPrime[-1]
        listPrime.pop()

print(*a)
