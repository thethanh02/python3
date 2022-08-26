import functools


def getSum(n):
    sum = 0
    for digit in str(n): 
      sum += int(digit)      
    return sum
   
def compare(a, b):
    if getSum(a) < getSum(b):
        return -1
    elif getSum(a) > getSum(b):
        return 1
    if a < b:
        return -1
    return 1

t = int(input())
for test in range(t):
    n = input()
    arr = [int(x) for x in input().split()]
    arr.sort(key=functools.cmp_to_key(compare))
    print(*arr, sep=' ')