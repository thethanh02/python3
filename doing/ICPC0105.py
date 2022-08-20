import re
import sys


t = int(input())
for i in range(t):
    n = input()
    a = re.findall("[0-9]+", n)
    maxx = -sys.maxsize
    for i in a:
        maxx = max(maxx, int(i))
    print(maxx)