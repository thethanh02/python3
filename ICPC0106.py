from math import log2


hexa = "0123456789ABCDEF"

def doi_co_so(n, b):
    step = int(log2(b))
    while len(n)%step != 0:
        n = '0' + n
    for i in range(0, len(n), step):
        token = 0
        for j in range(i, i+step):
            if n[j] == '1':
                token += pow(2, step - j%step - 1)
        print(hexa[token], end='')
    print()

t = int(input())
for i in range(t):
    b = int(input())
    n = input()
    doi_co_so(n, b)