from numbers import Complex

for t in range(int(input())):
    arr = [int(x) for x in input().split()]
    a = complex(arr[0], arr[1])
    b = complex(arr[2], arr[3])
    res1 = (a + b)*a
    tmp1 = '+' if res1.imag >= 0 else '-'
    res2 = (a + b) ** 2
    tmp2 = '+' if res2.imag >= 0 else '-'
    print(f'{int(res1.real)} {tmp1} {abs(int(res1.imag))}i, {int(res2.real)} {tmp2} {abs(int(res2.imag))}i')