from queue import Queue

p = ["0", "2", "4", "6", "8"]

def so_dep(n):
    q = Queue()

    for i in range(1,len(p)):
        q.put(p[i])

    while True:
        temp = q.get()
        num = temp + temp[::-1]
        
        if (int(num) < n):
            print(num, end=" ")
        else:
            break
        
        for i in p:
            q.put(temp+i)
    

t = int(input())
for i in range(t):
    n = int(input())
    so_dep(n)
    print()
    