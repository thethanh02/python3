    
n, m = [int(n) for n in input().split()]
a = [0]*n
for i in range(n):
    a[i] = [int(n) for n in input().split()]

count = 0
while n > m:
    n -= 1
    del a[count]
    count += 1

count = 1
while m > n:
    m -= 1
    for i in range(n):
        del a[i][count]
    count += 1

for i in a:
    print(*i)