s = '01234'
def check(n):
    sum = 0
    for i in n:
        if s.find(i) == -1:
            return 'NO'
        sum += int(i)
    if sum != 5:
        return 'NO'
    return 'YES'

for t in range(int(input())):
    n = input()
    print(check(n))
    