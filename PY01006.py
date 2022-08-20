def so_may_man(n):
    for i in range(len(n)):
        if(n[i] != '4' and n[i] != '7'):
            return "NO"
    return "YES"

t = int(input())
for i in range(t):
    n = input() 
    print(so_may_man(n))
