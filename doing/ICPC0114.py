from math import sqrt


def prime(n):
    m = int(n)
    if m < 2:
        return False
    for i in range(2, int(sqrt(m)/2)+1):
        if m%int(i) == 0:
            return False
    return True

def perfect_prime(n):
    if not (prime(n) or prime(n[::-1])):
        return "No"
    
    sum = 0
    for i in n:
        if not prime(i):
            return "No"
        sum += int(i)
    if not prime(str(sum)):
        return "No"
    return "Yes"

t = int(input())
for i in range(t):
    n = input()
    print(perfect_prime(n))