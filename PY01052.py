import math

def prime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num))+1):
        if num%i == 0:
            return False
    return True

def chu_so_nguyen_to(n):
    sum = 0
    for i in n:
        sum += int(i)
    if prime(sum):
        return "YES"
    return "NO"

t = int(input())
for i in range(t):
    n = input()
    print(chu_so_nguyen_to(n))
    