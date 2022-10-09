# def he_3(n):
#     for i in n:
#         if i != '0' and i != '1' and i != '2':
#             return "NO"
#     return "YES"

# t = int(input())
# for i in range(t):
#     n = input()
#     print(he_3(n))
    
t = int(input())
for i in range(t):
    n = input()
    a = [i for i in n if i == '0' or i == '1' or i == '2']
    print('YES' if len(a) == len(n) else 'NO')
    