import heapq
import re
import sys

input = sys.stdin.readline
t = int(input())
while t > 0:
    t -= 1

    n = input()
    arrStr = ' ' + input().replace(' ', '  ') + ' '

    check = 3
    sum = 0
    i = -18
    while i < 19 and check != 0:
        if i < 0:
            str = '-' + '\d'*abs(i) + ' '
        elif i > 0:
            str = ' ' + '\d'*abs(i) + ' '
        else:
            i += 1
            continue

        tmpArr = re.findall(str, arrStr)
        
        if len(tmpArr) != 0:
            arr = [int(x) for x in tmpArr]
            if len(tmpArr) <= check:
                for x in arr:
                    sum += x
                check -= len(tmpArr)
            else:
                for x in heapq.nsmallest(check, arr):
                    sum += x
                break
        i += 1
    
    print(sum)