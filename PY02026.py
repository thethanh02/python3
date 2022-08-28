n = [int(n) for n in input().split()]
a = [int(n) for n in input().split()]
b = [int(n) for n in input().split()]

set1 = sorted(set(a))
set2 = sorted(set(b))
print("YES" if set1 == set2 else "NO")