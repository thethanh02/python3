from math import sqrt

def so_xen_ke(n):
    if len(n)%2 == 0 or n[0] == n[1]:
        return "NO"
    for i in range(0, len(n), 2):
        if n[i] != n[i+2]:
            return "NO"
    return "YES"

t = int(input())
for i in range(t):
    n = input()
    print(so_xen_ke(n))