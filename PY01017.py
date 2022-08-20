def giai_ma(n):
    count = 1
    for i in range(len(n)-1):
        if n[i+1] == n[i]:
            count += 1
        else:
            print(str(count)+n[i],end="")
            count = 1

t = int(input())
for i in range(t):
    n = input()
    n += "."
    giai_ma(n)
    print()
