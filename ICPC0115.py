from math import factorial


def isKrish(n):
    sum = 0
    for i in n:
        sum += factorial(int(i))
    if sum == int(n):
        return "Yes"
    return "No"

t = int(input())
for test in range(t):
    n = input()
    print(isKrish(n))
