
def so_duyen_no(n):
    if n[0] == n[-1]:
        return "YES"
    return "NO"

t = int(input())
for test in range(t):
    n = input()
    print(so_duyen_no(n))
