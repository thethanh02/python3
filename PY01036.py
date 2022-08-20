def tong_phan_thuc(n):
    s = 0
    for i in range(n, 0, -2):
        s += 1/i
    print('%.6f'%s)

t = int(input())
for i in range(t):
    n = int(input())
    tong_phan_thuc(n)