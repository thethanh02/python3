

from typing import Counter, OrderedDict

def binary_search(arr, low, high, x):
 
    # Check base case
    if high >= low:
        mid = (high + low) // 2
        if arr[mid] == x:
            return True
 
        elif arr[mid] > x:
            return binary_search(arr, low, mid - 1, x)
 
        else:
            return binary_search(arr, mid + 1, high, x)
    else:
        return False

t = int(input())
for i in range(t):
    n = int(input())
    a = [int(a) for a in input().split()]
    # b = Counter(a)
    # count = 0
    # for i in range(0, len(a)):
    #     for j in range(i+1, len(a)):
    #         temp = a[i] + a[j]
    #         if b[-temp] != 0:
    #             count += b[-temp]
    #             b.pop(b[-temp])

    a.sort()
    count = 0
    for i in range(n-2):
        for j in range(i+1, n):
            if binary_search(a, j + 1, n - 1, -a[i]-a[j]):
                count += 1

    print(count)


# 2
# 5
# 0 -1 2 -3 1 
# 5
# 1 -2  1  0  5