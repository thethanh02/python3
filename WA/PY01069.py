from itertools import permutations
from queue import Queue

def chu_so_nguyen_to(n):
    q = Queue()
    q.put('2357')
    while 1:
        s = q.get()
        if len(s) > n:
            return

        for i in '2357':
            q.put(s + i)

        comb = permutations(sorted(s))
        for i in comb:
            print(*i, sep='')
    return

n = int(input())
chu_so_nguyen_to(n)