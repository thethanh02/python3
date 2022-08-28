from typing import Counter


n = input()
res = []
coun = Counter()
for i in range(2, len(n), 2):
    temp = int(n[i-2:i])
    if coun[temp] == 0:
        res.append(temp)
    coun[temp] += 1
print(*res)
