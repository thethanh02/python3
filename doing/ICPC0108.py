
t = int(input())
for i in range(t):
    n = input()
    a = [int(a) for a in input().split()]
    count = 0
    for i in range(len(a)):
        for j in range(i+1, len(a)):
            for k in range(j+1, len(a)):
                if a[i] + a[j] + a[k] == 0:
                    count += 1
    
    print(count)