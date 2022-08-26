import functools


def getMul(n):
    mul = 1
    for digit in str(n): 
      mul *= int(digit)      
    return mul
   
def compare(a, b):
    if getMul(a) < getMul(b):
        return -1
    elif getMul(a) > getMul(b):
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