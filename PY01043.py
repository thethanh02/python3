from queue import Queue

def thuan_nghich_chan(n):
    q = Queue()
    for i in range(2, 9, 2):
        q.put(str(i))
    while True:
        s = q.get()
        s_revered = s[::-1]
        concat = s + s_revered
        if int(concat) >= int(n):
            break
        print(concat, end=' ')
        for i in range(0, 9, 2):
            q.put(s+str(i))


t = int(input())
for i in range(t):
    n = input()
    thuan_nghich_chan(n)
    print()
    