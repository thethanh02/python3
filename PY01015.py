def so_khong_giam(n):
    for i in range(len(n)-1):
        if n[i+1] < n[i]:
            return "NO"
    return "YES"

t = int(input())
for i in range(t):
    n = input()
    print(so_khong_giam(n))
