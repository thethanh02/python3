from math import sqrt


N = pow(10, 6)
prime = []
for i in range(N+1):
    prime.append(1)
prime[0] = prime[1] = 0
for i in range(2, int(sqrt(N))+1):
    if prime[i] == 1:
        for j in range(i*i, N+1, i):
            prime[j] = 0

n, m = (int(n) for n in input().split())
matrix = [0] * n
for i in range(n):
    matrix[i] = [int(x) for x in input().split()]
    for j in range(m):
        matrix[i][j] = prime[matrix[i][j]]

for i in range(len(matrix)):
    print(*matrix[i])