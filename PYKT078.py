import operator


t = int(input())
for test in range(t):
    n, k = [int(a) for a in input().split()]
    a = [int(a) for a in input().split()]
    a.insert(a.index(max(a)), k)
    b = [i for i in a if i < 0]
    c = [i for i in a if i >= 0]
    print(*b, *c)
    