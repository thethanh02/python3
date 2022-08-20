a, k, n = [int(a) for a in input().split()]

right = int(n/k) + 1
left = int(a/k)
if a % k != 0:
    left += 1
if right - left <= 1:
    print(-1)
else:
    for i in range(left, right):
        print(i*k-a, end=" ")