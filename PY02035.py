from typing import Counter


n = input()
k = int(input())
res = []
coun = Counter()
for i in range(2, len(n), 2):
    temp = int(n[i-2:i])
    if coun[temp] == 0:
        res.append(temp)
    coun[temp] += 1

if max(coun.values()) < k:
    print('NOT FOUND')
else:
    for i in res:
        if coun[i] >= k:
            print(i, coun[i])