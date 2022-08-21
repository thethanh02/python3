
t = int(input())
for i in range(t):
    n, d = [int(n) for n in input().split()]
    a = [n for n in input().split()]
    print(*a[d:], *a[:d])