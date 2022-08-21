from math import sqrt


def prime(n):
    if n < 2:
        return False
    for i in range(2, int(sqrt(n))+1):
        if n%i == 0:
            return False
    return True

def perfect_prime(n):
    if not prime(int(n)) or not prime(int(n[::-1])):
        return "No"

    sum = 0
    for i in n:
        if not prime(int(i)):
            return "No"
        sum += int(i)
    if not prime(sum):
        return "No"
    return "Yes"

t = int(input())
for i in range(t):
    n = input()
    print(perfect_prime(n))