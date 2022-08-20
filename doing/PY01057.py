from math import sqrt

def prime(n):
    if n < 2:
        return False
    for i in range(2, int(sqrt(n))+1):
        if n%i == 0:
            return False
    return True

def vi_tri_nguyen_to(n):
    for i in range(len(n)):
        if prime(i):
            if not prime(int(n[i])):
                return "NO"
        else:
            if prime(int(n[i])):
                return "NO"

    return "YES"

t = int(input())
for i in range(t):
    n = input()
    print(vi_tri_nguyen_to(n))