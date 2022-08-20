import math

def thuan_nghich(num):
    n = 0
    for i in range(len(num)):
        n += int(num[i])
    n = str(n)
    if len(n) <= 1:
        return "NO"
    for i in range(int(len(n)/2)):
        if n[i] != n[len(n)-i-1]:
            return "NO"
    return "YES"

t = int(input())
for i in range(t):
    n = input()
    print(thuan_nghich(n))
    