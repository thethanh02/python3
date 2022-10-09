
from math import sqrt


def divisor(n):
  x = len([i for i in range(1,n+1) if not n % i])
  return x

n = int(input())
count = 0
for i in range(2, int(sqrt(n)) + 1):
    if divisor(i * i) == 9:
        count += 1
print(count)