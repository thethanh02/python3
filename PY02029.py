from typing import Counter

def bau_cu(a):
    coun = Counter(a)
    m1 = max(coun.values())
    key2 = 0
    val2 = 0
    for key, val in coun.items():
        if val2 < val and val != m1:
            key2 = key
            val2 = val
    return key2 if val2 != 0 else 'NONE'


# init
n = input().split()
a = [int(a) for a in input().split()]
print(bau_cu(a))