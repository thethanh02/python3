def divide7(n):
    if n % 7 == 0:
        return n
    sum = n
    for i in range(1000):
        m = str(sum)[::-1]
        sum += int(m)
        if sum % 7 == 0:
            return sum
    return -1

t = int(input())
for i in range(t):
    n = int(input())
    print(divide7(n))