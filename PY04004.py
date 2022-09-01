from fractions import Fraction

a = [int(a) for a in input().split()]
res = Fraction(a[0], a[1]) + Fraction(a[2], a[3])
print(res.numerator, '/', res.denominator, sep='')