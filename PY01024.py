
def chan_le(n):
    sum = 0
    for i in range(len(n)-1):
        sum += int(n[i])
        if(abs(int(n[i]) - int(n[i+1])) != 2):
            return "NO"

    if((sum+int(n[-1:])) % 10 != 0):
        return "NO"
    return "YES"

t = int(input())
for i in range(t):
    n = input()
    print(chan_le(n))