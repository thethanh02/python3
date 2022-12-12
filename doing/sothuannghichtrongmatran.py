import math
def nto(n):
    if(len(str(n)) < 2): return 0
    if str(n) != str(n)[::-1]: return 0
    return 1
n, m = [int(x) for x in input().split()]
a = [[] * m] * n
for i in range(n):
    a[i] = [int(x) for x in input().split()]
cnt = 0
for i in range(n):
    for j in range(m):
        if nto(a[i][j]) and a[i][j] > cnt:
            cnt = a[i][j]
if cnt == 0: print("NOT FOUND")
else:
    print(cnt)
    for i in range(n):
        for j in range(m):
            if a[i][j] == cnt:
                print("Vi tri [{}][{}]".format(i, j))