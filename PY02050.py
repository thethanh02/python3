
t = int(input())
for test in range(t):
    n = int(input())
    a = [int(a) for a in input().split()]
    stack = [0]
    res = [1] * n
    for i in range(1, n):
        while len(stack) != 0 and a[stack[-1]] <= a[i]:
            stack.pop()
        res[i] = (i + 1) if len(stack) == 0 else (i - stack[-1])
        stack.append(i)

    print(*res)