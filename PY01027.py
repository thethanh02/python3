def so_loc_phat_dep(n):
    if n[0] == '8':
        return "NO"
    for i in n:
        if i != '6' and i != '8':
            return "NO"
    for i in range(2, len(n)):
        if n[i] == '8' and n[i-1] == '8' and n[i-2] == '8':
            return "NO"
    return "YES"
n = input()
print(so_loc_phat_dep(n))
