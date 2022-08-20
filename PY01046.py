def tower(n, a, b, c):
    if n == 1:
        print(f'{a} -> {c}')
        return
    tower(n-1, a, c, b)
    tower(1, a, b, c)
    tower(n-1, b, a, c)
    return

# t = int(input())
# for i in range(t):
n = int(input())
tower(n, 'A', 'B', 'C')
    