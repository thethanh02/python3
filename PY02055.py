def isPrime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** (0.5)) + 1):
        if n % i == 0:
            return False
    return True

n, m = [int(n) for n in input().split()]
a = [0]*n
maxx = 0
for i in range(n):
    a[i] = [int(n) for n in input().split()]
    for j in a[i]:
        if j > maxx and isPrime(j):
            maxx = j
        
if maxx == 0:
    print('NOT FOUND')
else:
    print(maxx)
    for i in range(n):
        for j in range(m):
            if a[i][j] == maxx:
                print(f'Vi tri [{i}][{j}]')