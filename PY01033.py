import math

def nguyen_to_cung_nhau(l, r):
    for i in range(l, r-1):
        for j in range(i+1, r):
            for k in range(j+1, r+1):
                if math.gcd(i, j) == 1 and math.gcd(i, k) == 1 and math.gcd(j, k) == 1:
                    print(f'({i}, {j}, {k})')

# t = int(input())
# for i in range(t):
n, k = [int(n) for n in input().split()]
nguyen_to_cung_nhau(n, k)