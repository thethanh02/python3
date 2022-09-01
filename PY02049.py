t = int(input())
for test in range(t):
    n, p = [int(n) for n in input().split()]
    x = 0
    for i in range(1, n+1):
        temp = i
        while temp % p == 0:
            x += 1
            temp //= p
    
    print(x)