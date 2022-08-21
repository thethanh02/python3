from math import sqrt

def tong_tich(n):
    sum = 0
    mul = 1
    for i in range(len(n)):
        if i%2 == 1:
            sum += int(n[i])
        else:
            if n[i] != '0':
                mul *= int(n[i])
    
    print(mul, sum)

t = int(input())
for i in range(t):
    n = input()
    tong_tich(n)