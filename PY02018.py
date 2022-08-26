from collections import Counter

def so_nho_nhat_con_thieu(coun, left, right):
    for i in range(left, right+1):
        if coun[i] == 0:
            return i
    return 1 if left > 1 else right +1

n = int(input())
a = [int(a) for a in input().split()]
coun = Counter()
for i in a:
    coun[i] += 1
print(so_nho_nhat_con_thieu(coun, min(a), max(a)))