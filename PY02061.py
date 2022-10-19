def tichchap(n, m, a, b):
    c = []
    for i in range(n):
        tmp = [0]*m
        c.append(tmp)
    
    sum = 0
    for x in range(n - 2):
        for y in range(m - 2):
            for i in range(3):
                for j in range(3):
                    c[x][y] += a[x + i][y + j] * b[i][j]
                
            sum += c[x][y]

    return sum

for t in range(int(input())):
    n, m = [int(n) for n in input().split()]
    a = []
    b = []
    for i in range(n):
        tmp = [int(x) for x in input().split()]
        a.append(tmp)
    
    for i in range(3):
        tmp = [int(x) for x in input().split()]
        b.append(tmp)

    print(tichchap(n, m, a, b))
