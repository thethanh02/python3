from collections import Counter


t = int(input())
for test in range(t):
    map = Counter();
    q = int(input())
    ans = 0
    for query in range(q):
        x = int(input())
        map[x] += 1
        if map[ans] < map[x]:
            ans = x
        elif map[ans] == map[x]:
            ans = x if x < ans else ans
    
    print(ans)
            