def chen_dau_phay(n):
    step = int(len(n)/3)
    if(len(n) % 3 == 0):
        step -= 1;
    res = ''
    s = n
    for i in range(step):
        res = ',' + s[-3:] + res
        s = s[:-3]
    res = s + res
    print(res)

# t = int(input())
# for i in range(t):
n = input()
# print(n[:-3])
chen_dau_phay(n)
    