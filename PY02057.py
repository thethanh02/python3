n, m = [int(n) for n in input().split()]
a = [0]*n
m2 = 0
m1 = 1e6
for i in range(n):
    a[i] = [int(n) for n in input().split()]
    m2 = max(max(a[i]), m2)
    m1 = min(min(a[i]), m1)
        
res = []
for i in range(n):
    for j in range(m):
        if a[i][j] == m2 - m1:
            res.append(f'Vi tri [{i}][{j}]')
if len(res) == 0:
    print('NOT FOUND')
else:
    print(m2 - m1)
    print(*res, sep='\n')