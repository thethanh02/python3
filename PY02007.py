
a = [int(a)%42 for a in input().split()]
cond = len(a)
s = set(a)
while (cond < 10):
    a = [int(a)%42 for a in input().split()]
    cond += len(a)
    s.update(a)
print(len(s))