def giai_ma(n):
    for i in range(0, len(n), 2):
        for j in range(int(n[i+1])):
            print(n[i], end="")


t = int(input())
for i in range(t):
    n = input()
    giai_ma(n)
    print()
