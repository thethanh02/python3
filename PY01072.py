from itertools import combinations


n, k = [int(n) for n in input().split()]
a = [int(a) for a in input().split()]

s = set(a)
com = combinations(sorted(s), k)
for i in com:
    print(*i)