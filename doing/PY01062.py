import math

def prime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num))+1):
        if num%i == 0:
            return False
    return True

def chu_so_nguyen_to(n):
    if not prime(len(n)):
        return "NO"
    count = 0
    for i in n:
        if prime(int(i)):
            count += 1
    if count > len(n)-count:
        return "YES"
    return "NO"

t = int(input())
for i in range(t):
    n = input()
    print(chu_so_nguyen_to(n))
    