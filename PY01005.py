def so_may_man(n):
    count = 0
    for i in range(len(n)):
        if(n[i] == '4' or n[i] == '7'):
            count+=1
    if(count == 4 or count == 7): 
        return "YES"
    return "NO"

n = input()
print(so_may_man(n))
