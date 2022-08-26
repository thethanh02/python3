from collections import Counter
from math import gcd


n = input()
a = [float(a) for a in input().split()]
coun = Counter()
sum = 0
for i in a:
    sum += i
    coun[i] += 1
maxx = max(a)
minn = min(a)
sum = (sum - maxx*coun[maxx] - minn*coun[minn]) / (len(a) - coun[maxx] - coun[minn])
print("%.2f" %sum)