
from math import comb

n = int(input())
a = ['0'] * n
sum = 0
for i in range(n):
    # b = [b for b in input().split()]
    b = input()
    a[i] = b
    count = b.count('C')
    if count >= 2:
        sum += comb(count, 2)

for i in range(n):
    count = 0
    for j in range(n):
        if a[j][i] == 'C':
            count += 1

    if count >= 2:
        sum += comb(count, 2)

print(sum)
