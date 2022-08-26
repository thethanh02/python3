from math import gcd


n = input()
a = sorted([int(a) for a in input().split()])
for i in range(len(a)):
    for j in range(i+1, len(a)):
        if gcd(a[i], a[j]) == 1:
            print(a[i], a[j])