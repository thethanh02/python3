temp = "ABCDEFGHIJKLMNOPQRSTUVWXYZ_."
p = list(temp)

def ma_hoa(k, s):
    for i in range(len(s)):
        for j in range(len(p)):
            if p[j] == s[i]:
                s[i] = p[(j+k)%28]
                break
    
    for i in range(len(s)-1, -1, -1):
        print(s[i], end="")
    
    print()

while True:
    k = [k for k in input().split()]
    if k[0] == "0":
        break
    ma_hoa(int(k[0]), list(k[1]))