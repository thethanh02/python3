n, k = [int(a) for a in input().split()]
a = [int(a) for a in input().split()]

count = 1
arr = sorted(a)
for i in range(len(arr)):
    if arr[i] - arr[i - 1] > k:
        count += 1

print(count)