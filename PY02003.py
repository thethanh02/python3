cnt = []
coun = dict()

# init
for i in range(65):
    x = pow(5, i)
    for j in range(65):
        y = 0
        if (x * pow(3, j) <= 10**18):
            y = x * pow(3, j)
        else:
            break
        for k in range(65):
            if y * pow(2, k) <= 10**18:
                cnt.append(y * pow(2, k))
            else:
                break

t = int(input())


cnt.sort()
coun = {cnt[i]: i for i in range(len(cnt))}

while t > 0:
    t -= 1
    n = int(input())
    try:
        print(coun[n]+1)
    except:
        print("Not in sequence")