t = int(input())
preLen = 0
list = []
count = 5
for test in range(t):
    s = input().split()
    if len(s) == 7 and (len(s) != preLen or count > 4):
        count = 0
        list.append(2)
    if (len(s) == 6 or len(s) == 8) and preLen != 6 and preLen != 8:
        list.append(1)

    count += 1
    preLen = len(s)

print(len(list))
print(*list, sep='\n')