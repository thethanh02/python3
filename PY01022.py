n = input()
count = 0
while 1:
    sum = 0
    count += 1
    for i in n:
        sum += ord(i) - ord('0')
    n = str(sum)
    if (len(n) == 1):
        print(count)
        break
