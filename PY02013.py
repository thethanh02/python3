while 1:
    n = int(input())
    if n == 0:
        break
    count = 1
    while n != 1:
        n = n/2 if n%2 == 0 else n*3 + 1
        count += 1
    print(count)

