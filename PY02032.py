n = input()
s = set()
for i in range(2, len(n), 2):
    s.add(int(n[i-2:i]))
print(*sorted(s))
