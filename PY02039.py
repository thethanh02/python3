
n = int(input())
matrix = [0] * n
topSum = botSum = 0
for i in range(n):
    matrix[i] = [int(x) for x in input().split()]
    for j in range(n):
        if j > i: topSum += matrix[i][j]
        elif i > j: botSum += matrix[i][j]
k = int(input())
res = abs(topSum-botSum)
print("YES" if res <= k else "NO") 
print(res)
