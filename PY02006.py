def day_so_phu_hop(a, b):
    a.sort()
    b.sort()
    for i in range(len(a)):
        if a[i] > b[i]:
            return "NO"
    return "YES"

t = int(input())
for test in range(t):
    n = input()
    a = [int(a) for a in input().split()]
    b = [int(b) for b in input().split()]
    print(day_so_phu_hop(a, b))