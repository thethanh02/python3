n = int(input())
a = [[]] * n
for i in range(n):
    a[i] = [int(x) for x in input().split()]
k = int(input())
tren = 0
duoi = 0
for i in range(n):
    for j in range(n):
        if i  < j: tren += a[i][j]
        elif j  < i: duoi += a[i][j]
if abs(tren - duoi) <= k: print("YES")
else: print("NO")
print(abs(tren - duoi))