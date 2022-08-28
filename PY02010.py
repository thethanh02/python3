while 1:
    n = int(input())
    if n == 0:
        break
    arr = []
    for i in range(n):
        arr.append(int(input()))
    m1 = min(arr)
    m2 = max(arr)
    if m1 == m2:
        print("BANG NHAU")
    else:
        print(m1, m2)