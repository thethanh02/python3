import sys

s = sys.stdin.read().lower().split()
s[0] = s[0][:1].upper() + s[0][1:]
for i in range(len(s)):
    if s[i][-1] == '.' or s[i][-1] == '!' or s[i][-1] == '?':
        s[i] = s[i][:-1]
        if i+1 < len(s):
            s[i+1] = '\n' + s[i+1][:1].upper() + s[i+1][1:]
print(*s)