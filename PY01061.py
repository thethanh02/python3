from math import sqrt


def prime(n):
    if n < 2:
        return False
    for i in range(2, int(sqrt(n))+1):
        if n%i == 0:
            return False
    return True

def dau_cuoi_nguyen_to(n):
    if prime(int(n[-3:])) and prime(int(n[:3])):
        return "YES"
    return "NO"

t = int(input())
for i in range(t):
    n = input()
    print(dau_cuoi_nguyen_to(n))