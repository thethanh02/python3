import string


conv = '0123456789' + string.ascii_uppercase

def decimalToK(val, k):
    if val >= 1:
        decimalToK(val // k, k)
    
    res.append(conv[val % k])

t = int(input())
for test in range(t):
    res = []
    n, k = [int(n) for n in input().split()]
    decimalToK(n, k)
    while res[0] == '0' and len(res) > 0:
        res = res[1:]
    print(*res, sep = '')