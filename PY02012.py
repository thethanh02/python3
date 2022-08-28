import functools


def mycomp(x, y):
    return y - x

n = int(input())
a = [int(a) for a in input().split()]
while len(a) < n:
    a += [int(a) for a in input().split()]
chan = []
le = []
for i in a:
    if i % 2 == 0:
        chan.append(i)
    else:
        le.append(i)

chan.sort(key = functools.cmp_to_key(mycomp))
le.sort()

for i in a:
    if i % 2 == 0:
        print(chan[-1], end = ' ')
        chan.pop()
    else:
        print(le[-1], end = ' ')
        le.pop()