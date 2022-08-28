import queue

# prepare
arr = []
q = queue.Queue()
q.put('1')
q.put('2')
while len(arr) < 1000:
    x = q.get()
    if x.count('2') > x.count('1') + x.count('0'):
        arr.append(x)
    
    for i in '012':
        q.put(x + i)

# main
t = int(input())
for test in range(t):
    n = int(input())
    for i in range(n):
        print(arr[i], end=' ')
    print()