def dau_cuoi(n):
    x = len(n)
    if n[0] == n[x-2] and n[1] == n[x-1]:
        return "YES"
    return "NO"

t = int(input())
for i in range(t):
    n = input()
    print(dau_cuoi(n))
    