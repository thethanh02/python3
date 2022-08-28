from typing import Counter

t = int(input())
for test in range(t):
    n = [int(n) for n in input().split()]
    a = [int(n) for n in input().split()]
    b = [int(n) for n in input().split()]
    c = [int(n) for n in input().split()]

    coun1 = Counter(a)
    coun2 = Counter(b)
    coun3 = Counter(c)

    inte = sorted(set(a).intersection(set(b), set(c)))
    if len(inte) == 0:
        print("NO")
    else:
        for i in inte:
            for j in range(min(coun1[i], coun2[i], coun3[i])):
                print(i, end=' ')
        print()