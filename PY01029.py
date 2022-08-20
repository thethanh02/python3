import math

def dao_nguyen_to_cung_nhau(a):
    b = a[::-1]
    if math.gcd(int(a), int(b)) == 1:
        return "YES"
    return "NO"


t = int(input())
for i in range(t):
    a = input()
    print(dao_nguyen_to_cung_nhau(a))