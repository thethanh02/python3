# from typing import Counter


# n = input()
# k = int(input())
# res = []
# coun = Counter()
# for i in range(2, len(n), 2):
#     temp = int(n[i-2:i])
#     if coun[temp] == 0:
#         res.append(temp)
#     coun[temp] += 1

# if max(coun.values()) < k:
#     print('NOT FOUND')
# else:
#     for i in res:
#         if coun[i] >= k:
#             print(i, coun[i])

from typing import Counter


n = input()
k = int(input())
res = []
coun = Counter()
for i in range(2, len(n)+1, 2):
    temp = int(n[i-2:i])
    coun[temp] += 1

maxx = max(coun, key = coun.get)
print(coun.most_common())
if coun[maxx] < k:
    print('NOT FOUND')
else:
    coun = sorted(coun.items(), key=lambda pair: pair[0])
    for key, value in coun:
        if value >= k: 
            print(key, value)