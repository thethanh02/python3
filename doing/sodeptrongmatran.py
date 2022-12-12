n, m = [int(x) for x in input().split()]
a = [[] * m] * n
for i in range(n):
    a[i] = [int(x) for x in input().split()]
cnt = 0
max = -10**20
min = 10**20
for i in range(n):
    for j in range(m):
        if a[i][j] > max: max = a[i][j]
        if a[i][j] < min: min = a[i][j]

for i in range(n):
    for j in range(m):
        if a[i][j] == max - min:
            cnt += 1
if cnt == 0: print("NOT FOUND")
else:
    print(max- min)
    for i in range(n):
        for j in range(m):
            if a[i][j] == max - min:
                print("Vi tri [{}][{}]".format(i, j))