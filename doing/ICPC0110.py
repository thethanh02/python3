import heapq
import re
import sys

input = sys.stdin.readline
t = int(input())
while t > 0:
    t -= 1

    input()
    arrStr = input().replace(' ', '  ')
    arrStr = ' ' + arrStr[0:len(arrStr) - 1] + ' '

    check = 3
    sum = 0
    i = 8
    while i > -9 and check > 0:
        if i > 0:
            s = ' ' + '\d'*abs(i) + ' '
        elif i < 0:
            s = '-' + '\d'*abs(i) + ' '
        else:
            i -= 1
            continue
        
        if i == 1:
            for x in reversed(range(10)):
                s = ' ' + str(x) + ' '
                y = arrStr.count(s)
                if y > check:
                    sum += check * int(s)
                    break
                else:
                    sum += y * int(s)
                check -= y

        elif i == -1:
            for x in range(1, 10):
                s = '-' + str(x) + ' '
                y = arrStr.count(s)
                if y > check:
                    sum += check * int(s)
                    break
                else:
                    sum += y * int(s)
                check -= y

        else:
            tmpArr = re.findall(s, arrStr)
            intArr = [int(x) for x in tmpArr]
            if len(intArr) <= check:
                for x in intArr:
                    sum += x
                check -= len(intArr)
            else:
                for x in heapq.nlargest(check, intArr):
                    sum += x
                break
        i -= 1
    print(sum)