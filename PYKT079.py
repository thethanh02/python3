from collections import Counter


t = int(input())
for test in range(t):
    n = int(input())
    a = [int(a) for a in input().split()]
    b = Counter(a)
    print(max(a) - min(a) + 1 - len(b))