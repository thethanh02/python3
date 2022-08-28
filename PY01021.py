t = int(input())
for test in range(t):
    s = input()
    res = []
    sum = 0
    for i in s:
        if i.isdigit():
            sum += int(i)
        else:
            res.append(i)
    print(*sorted(res), sum, sep='')