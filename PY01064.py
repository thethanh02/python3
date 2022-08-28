fb = [0]
fb.append(1)
for i in range(2, 26):
    fb.append(fb[i-1]*2 + 1)

def kth_character(n, k):
    if k == 1:
        return 'A'
    p = fb[n]//2 + 1
    if k == p:
        return chr(ord('A') + n - 1)
    elif k > p:
        return kth_character(n - 1, k - p)
    return kth_character(n - 1, k)

t = int(input())
for test in range(t):
    n, k = [int(n) for n in input().split()]
    print(kth_character(n, k))