
for t in range(int(input())):
    n, m = [int(n) for n in input().split()]
    a = []
    for i in range(n):
        tmp = [int(x) for x in input().split()]
        a.append(tmp)
    
    res = []
    for i in range(n):
        tmp = [0] * n
        res.append(tmp)

    for i in range(n):
        for j in range(n):
            for k in range(m):
                res[i][j] += a[i][k] * a[j][k]

    for i in range(n):
        print(*res[i])