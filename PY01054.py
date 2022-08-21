from math import sqrt

def tich_chu_so(n):
    res = 1
    for i in n:
        if i != '0':
            res *= int(i)
    print(res)

t = int(input())
for i in range(t):
    n = input()
    tich_chu_so(n)