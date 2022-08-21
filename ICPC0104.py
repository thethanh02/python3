import re
import sys


t = int(input())
for i in range(t):
    n = input()
    a = re.findall("[0-9]+", n)
    minn = sys.maxsize
    for i in a:
        minn = min(minn, int(i))
    print(minn)