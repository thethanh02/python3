from math import sqrt

N = pow(10, 6)
# prime = Counter() 
# dung thu Counter bi IR
prime = []
for i in range(N+1):
    prime.append(0)
prime[0] = prime[1] = 1
for i in range(2, int(sqrt(N))+1):
    if prime[i] == 0:
        for j in range(i*i, N+1, i):
            prime[j] = 1

prime_triplet = []
for i in range(12):
    prime_triplet.append(0)
for i in range(12, 14):
    prime_triplet.append(1)
for i in range(14, N+1):
    prime_triplet.append(prime_triplet[i-1])
    if not prime[i-1]:
        if not prime[i-3] and not prime[i-7]:
            prime_triplet[i] += 1
        if not prime[i-5] and not prime[i-7]:
            prime_triplet[i] += 1

t = int(input())
for test in range(t):
    n = int(input())
    print(prime_triplet[n])