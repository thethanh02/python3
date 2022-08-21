from math import sqrt

def tong_tich(n):
    sum = 0
    sum_check = 0
    mul = 1
    for i in range(len(n)):
        if i%2 == 0:
            sum += int(n[i])
        else:
            sum_check += int(n[i])
            if n[i] != '0':
                mul *= int(n[i])
    
    if sum_check == 0:
        mul = 0
    print(sum, mul)

t = int(input())
for i in range(t):
    n = input()
    tong_tich(n)