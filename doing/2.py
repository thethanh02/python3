
from math import sqrt

N = pow(10, 6)
prime = [1] * (N + 1)
check = [1] * (N + 1)
prime[0] = prime[1] = 0
check[0] = check[1] = 0
cnt = 1
for i in range(2, int(sqrt(N))+1):
    if check[i] == 1:
        prime[i] = cnt
        cnt += 1
        for j in range(i*i, N+1, i):
            prime[j] = 0
            check[j] = 0

for i in range(4, N + 1):
    if prime[i] == 0:
        prime[i] = prime[i - 1]

n = int(input())
if n < 36:
    print(0)
else:
    # count = prime[int(sqrt(n / 4))] - 1
    count = prime[int(n ** (1/8))]

    for i in range(2, 10 ** 9, 1):
        if i * i > sqrt(n):
            break
        if prime[int(sqrt(n / i / i))] - prime[i] <= 0 or check[i] == 0:
            continue
        count += prime[int(sqrt(n / i / i))] - prime[i]
    print(count)

# 36  (2 * 3)^2
# 100 (2 * 5)^2
# 196 (2 * 7)^2
# 225 (3 * 5)^2
# 256 (4 * 4)^2
# 441 (3 * 7)^2
# 484 (2 * 11)^2
# 676 (2 * 13)^2