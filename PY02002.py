f = []
f.append(0)
f.append(1)
for i in range(2, 93):
    f.append(f[i-1] + f[i-2])

t = int(input())
for test in range(t):
    l, r = [int(l) for l in input().split()]
    for i in range(l, r+1):
        print(f[i], end=' ')
    print()
