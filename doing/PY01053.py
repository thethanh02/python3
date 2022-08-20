
def chia_het_3(n):
    sum = 0
    for i in n:
        sum += int(i)
    if sum%3 == 0:
        return "YES"
    return "NO"

t = int(input())
for i in range(t):
    n = input()
    print(chia_het_3(n))
    