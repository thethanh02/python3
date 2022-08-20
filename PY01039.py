def so_dep(n):
    # a = []
    # for i in range(10):
    #     a.append(0)
    if n[0] == n[1]:
        return "NO"

    for i in range(0, len(n)-2, 2):
        if n[i] != n[i+2]:
            return "NO"
    for i in range(1, len(n)-2, 2):
        if n[i] != n[i+2]:
            return "NO"

    return "YES"

t = int(input())
for i in range(t):
    n = input()
    print(so_dep(n))
    