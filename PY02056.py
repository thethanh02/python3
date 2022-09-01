def thuan_nghich(n):
    temp = str(n)
    return temp == temp[::-1]

n, m = [int(n) for n in input().split()]
a = [0]*n
maxx = 10
for i in range(n):
    a[i] = [int(n) for n in input().split()]
    for j in a[i]:
        if j > maxx and thuan_nghich(j):
            maxx = j
        
if maxx == 10:
    print('NOT FOUND')
else:
    print(maxx)
    for i in range(n):
        for j in range(m):
            if a[i][j] == maxx:
                print(f'Vi tri [{i}][{j}]')