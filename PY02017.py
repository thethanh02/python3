t = int(input())
for test in range(t):
    n = int(input())
    a = [int(a) for a in input().split()]
    ans = a[0]
    for i in range(1, n):
        ans ^= a[i]
    print(ans)