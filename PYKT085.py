t = int(input())
list = []
index = [-1]
for test in range(t):
    s = input()
    list.append(s)
    if s == '':
        index.append(test)

index.append(t)
for i in range(len(index)-1):
    print(f'{list[index[i]+1]}: {index[i+1] - index[i] - 2}')