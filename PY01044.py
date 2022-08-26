s1 = sorted(input().lower().split())
s2 = sorted(input().lower().split())
print(*sorted(set(s1).union(set((s2)))))
print(*sorted(set(s1).intersection(set((s2)))))
