from math import sqrt


def prime(n):
    if n < 2:
        return False
    for i in range(2, int(sqrt(n))+1):
        if n%i == 0:
            return False
    return True

def chan_le_nguyen_to(n):
    sum = 0
    for i in range(len(n)):
        sum += int(n[i])
        if i%2 == 0 and int(n[i])%2 != 0:
            return "NO"
        if i%2 == 1 and int(n[i])%2 == 0:
            return "NO"
    if prime(sum):
        return "YES"
    return "NO"

t = int(input())
for i in range(t):
    n = input()
    print(chan_le_nguyen_to(n))