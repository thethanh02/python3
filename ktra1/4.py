
for t in range(int(input())):
    s1 = input()
    s2 = input()

    s2_list = s2.split()

    s1_low = s1.lower().split()
    s2_low = s2.lower().split()
    for i in range(len(s2_low)):
        if s1_low.count(s2_low[i]) > 0:
            print(s2_list[i], end=' ')

    print()


    