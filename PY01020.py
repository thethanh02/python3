def loc_phat(s):
    if s[-2:] == '86':
        return "YES"
    return "NO"


t = int(input())
for i in range(t):
    s = input()
    print(loc_phat(s))