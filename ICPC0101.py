from collections import deque

n = int(input())
a = [int(a) for a in input().split()]
st = []
for i in a:
    if len(st) == 0:
        st.append(i)
    else:
        if (i + st[-1]) % 2 == 0:
            st.pop()
        else:
            st.append(i)
print(len(st))