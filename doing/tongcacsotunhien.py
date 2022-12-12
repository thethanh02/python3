a = []
b = [0] * 100
def ql(sum, vt ,sl):
    if sum == n:
        for i in range(0, sl):
            a.append(b[i])
    for i in range(vt, 0, -1):
        if sum + i <= n:
            b[sl] = i
            ql(sum + i, i, sl + 1)
t = int(input())
for i in range(t):
    n = int(input())
    sum, cnt, ok = n, 0, 1
    ql(0, n, 0)
    for i in a: cnt += i
    print(int(cnt / n))
    for i in a:
        if n - i >= 0:
            if ok == 1 :
                print("(", end = "")
                ok = 0
            print(i, end = "")
            if n  - i != 0: print(" ", end = "")
            n = n - i
        if n == 0: 
            ok = 1
            n = sum
            print(")", end = " ")
    print()    
    a.clear()