def dem_so(n, k):
    pos = 0
    count = 0

    temp = n.find(k, pos, len(n))
    while True:
        temp = n.find(k, pos, len(n))
        if pos > len(n):
            break
        if temp != -1:
            count += 1
            pos = temp + len(k)
        else:
            break

    print(count)

t = int(input())
for i in range(t):
    n = input()
    k = input()
    dem_so(n, k)
    