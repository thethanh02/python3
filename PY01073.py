from itertools import permutations


s = input()

per = permutations(s)
for i in per:
    print(*i, sep='')