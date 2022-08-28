n, m = [int(n) for n in input().split()]
a = [int(n) for n in input().split()]
b = [int(n) for n in input().split()]

inte = sorted(set(a).intersection(set(b)))
print(*inte)

sub1 = sorted(set(a).difference(set(b)))
print(*sub1)

sub2 = sorted(set(b).difference(set(a)))
print(*sub2)