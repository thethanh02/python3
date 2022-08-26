from curses.ascii import SO
from typing import Counter


def Solution(coun, n):
    for key, value in coun.items():
        if value > int(n/2):
            return key
    return "NO"

t = int(input())
for test in range(t):
    n = int(input())
    arr = [int(arr) for arr in input().split()]
    coun = Counter()
    for i in arr:
        coun[i] += 1

    print(Solution(coun, n))