import string

ascii = string.ascii_letters

def check(s1, s2):
    for i in range(len(s1)-1):
        if abs(ascii.find(s1[i]) - ascii.find(s1[i-1])) != abs(ascii.find(s2[i]) - ascii.find(s2[i-1])): 
            return "NO"
    return "YES"


t = int(input())
for i in range(t):
    s1 = input()
    s2 = s1[::-1]
    print(check(s1, s2))
    
    