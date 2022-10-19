import heapq
import re
import sys

input = sys.stdin.readline
t = int(input())
while t > 0:
    t -= 1

    n = input()
    arrStr = ' ' + input().replace(' ', '  ') + ' '

    arr = []
    i = -8
    while i < 9 and len(arr) < 4:
        if i < 0:
            str = '-' + '\d'*abs(i) + ' '
        elif i > 0:
            str = ' ' + '\d'*abs(i) + ' '
        else:
            i += 1
            continue

        tmpArr = re.findall(str, arrStr)
        arr += [int(x) for x in tmpArr]
        i += 1
    
    sum = 0
    for x in heapq.nsmallest(3, arr):
        sum += x
    print(sum)