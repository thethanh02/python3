for t in range(int(input())):
    s1 = input()
    s2 = input()
    print(f'Test {t+1}:', 'YES' if sorted(s1) == sorted(s2) else 'NO')