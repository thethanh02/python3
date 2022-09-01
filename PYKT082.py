def transScore(n):
    if n >= 39:
        return 9
    if n >= 37:
        return 8.5
    if n >= 35:
        return 8
    if n >= 33:
        return 7.5
    if n >= 30:
        return 7
    if n >= 27:
        return 6.5
    if n >= 23:
        return 6
    if n >= 20:
        return 5.5
    if n >= 16:
        return 5
    if n >= 13:
        return 4.5
    if n >= 10:
        return 4
    if n >= 7:
        return 3.5
    if n >= 5:
        return 3
    if n >= 3:
        return 2.5
    return 0

def bigRound(n):
    decimal = n - int(n)
    if decimal >= 0.75:
        return int(n) + 1
    if decimal >= 0.25:
        return int(n) + 0.5
    return int(n)

t = int(input())
for test in range(t):
    a = [float(a) for a in input().split()]
    overall = (transScore(a[0]) + transScore(a[1]) + a[2] + a[3]) / 4
    print("%.1f"%bigRound(overall))