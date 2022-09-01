from fractions import Fraction

a = [int(a) for a in input().split()]
res = Fraction(a[0], a[1])
print(res.numerator, '/', res.denominator, sep='')