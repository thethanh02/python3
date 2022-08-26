from math import sqrt


N = pow(10, 5)
check = []
prime = []
for i in range(N+1):
    check.append(1)
check[0] = check[1] = 0
for i in range(2, int(sqrt(N))+1):
    if check[i] == 1:
        for j in range(i*i, N+1, i):
            check[j] = 0
for i in range(len(check)):
    if check[i]:
        prime.append(i)

a, b = [int(a) for a in input().split()]
arr = []
arr.append(b)
for i in range(a):
    arr.append(prime[i]+arr[i])
for i in arr:
    print(i, end=' ')