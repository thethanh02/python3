def chia_het_3(n):
    if n%3 == 0:
        return "YES"
    return "NO"

t = int(input())
for i in range(t):
    n = input()
    print(chia_het_3(int(n)))
    