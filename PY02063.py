n = int(input())
a = sorted([int(a) for a in input().split()])
nega = a[0] * a[1]
inte = a[-1] * a[-2]
print(max(nega*a[2], nega*a[-1], inte*a[0], inte*a[-3]))