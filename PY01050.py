import functools


n = int(input())
arr = []


def compare(a, b):
    if len(a) < len(b):
        return -1
    elif len(a) == len(b) and a < b:
        return 1
    return 0


def back(s, cntA, cntB, cntC):
    if (len(s) > n):
        return

    if cntA > 0 and cntB >= cntA and cntC >= cntB:
        arr.append(s)
    back(s + "A", cntA+1, cntB, cntC)
    back(s + "B", cntA, cntB+1, cntC)
    back(s + "C", cntA, cntB, cntC+1)


back("", 0, 0, 0)
arr.sort(key=functools.cmp_to_key(compare))
for i in arr:
    print(i)
#Ky tu ABC