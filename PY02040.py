
n = int(input())
matrix = [0] * n
topSum = botSum = 0
for i in range(n):
    matrix[i] = [int(x) for x in input().split()]
    for j in range(n):
        if i > n - j - 1: topSum += matrix[i][j]
        elif i < n - j - 1: botSum += matrix[i][j]
k = int(input())
res = abs(topSum-botSum)
print("YES" if res <= k else "NO") 
print(res)