t = int(input())
for i in range(t):
    n, x, m = [float(x) for x in input().split()]
    count = 0
    while n < m:
        n += n*x/100
        count += 1
    print(count)
