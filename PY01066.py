def xau_thang_bang(s1):
    s2 = s1[::-1]
    for i in range(1, len(s1)):
        if abs(ord(s1[i]) - ord(s1[i-1])) != abs(ord(s2[i]) - ord(s2[i-1])):
            return "NO"
    return "YES"

t = int(input())
for test in range(t):
    s1 = input()    
    print(xau_thang_bang(s1))
