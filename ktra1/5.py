import functools


def tich_vi_tri_le(n):
    mul = 1
    for i in range(len(n)):
        if i % 2 == 0 and n[i] != '0':
            mul *= int(n[i])
    return mul

def mycomp(a, b):
    c = tich_vi_tri_le(a)
    d = tich_vi_tri_le(b)
    if c < d:
        return -1
    elif c > d:
        return 1
    if int(a) < int(b):
        return -1
    elif int(a) > int(b):
        return 1
    return 0

for t in range(int(input())):
    n = int(input())
    l = input().split()
    while len(l) < n:
        l += input().split()
    l.sort(key=functools.cmp_to_key(mycomp))
    print(*l)