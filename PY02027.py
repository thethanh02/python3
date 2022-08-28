import re


t = int(input())
list = []
for test in range(t):
    s = input()
    a = re.findall("[0-9]+", s)
    list += [int(x) for x in a]

print(*sorted(list), sep='\n')