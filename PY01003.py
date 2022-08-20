def lam_tron(x):
    for i in range(len(x)-1, 0, -1):
        if int(x[i]) >= 5:
            x[i-1] = int(x[i-1]) + 1
        x[i] = 0
    for i in range(0, len(x)):
        print(x[i], end="")

n = int(input())
for i in range(n):
    temp = input()
    if (len(temp) == 1): 
        print(temp)
    else :
        x = list(temp)
        lam_tron(x)
    print()
