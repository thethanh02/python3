import math

def nguyen_to_cung_nhau(n, k):
    count = 0
    for i in range(pow(10, k-1), pow(10, k)):
        if math.gcd(n, i) == 1:
            count += 1
            print(i, end=' ')
        if count == 10:
            print()
            count = 0

# t = int(input())
# for i in range(t):
n, k = [int(n) for n in input().split()]
nguyen_to_cung_nhau(n, k)