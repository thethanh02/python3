def ql(s, cnt2, cnt3, cnt5, cnt7, m):
    if len(s) == 10: return
    if len(s) == m and cnt2 and cnt3 and cnt5 and cnt7 and s[-1] != '2': print(s)
    ql(s + '2', cnt2 + 1, cnt3, cnt5, cnt7, m)
    ql(s + '3', cnt2, cnt3 + 1, cnt5, cnt7, m)
    ql(s + '5', cnt2, cnt3, cnt5 + 1, cnt7, m)
    ql(s + '7', cnt2, cnt3, cnt5, cnt7 + 1, m)

n = int(input())
for i in range(4, n + 1): ql('', 0, 0, 0, 0, i)