from itertools import combinations


n, k = [int(n) for n in input().split()]
a = sorted(set(input().split()))
c = combinations(a, k)
for i in c:
    print(*i)