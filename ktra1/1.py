for t in range(int(input())):
    n = input()
    print('YES' if n[0:2] == n[len(n) - 2:len(n)][::-1] else 'NO')