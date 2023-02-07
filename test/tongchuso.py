# import pickle
# import re

# with open("DATA.in", "wb") as f:
#     num = ['Jhsf00dklT12uhf780LPPZH', 'AAAAddd0000000000000000001T']
#     pickle.dump(num, f)
# with open("DATA.in", "rb") as f:
#     a = pickle.load(f)
#     print(a)

# import array
# import pickle
# import re

# with open("DATA.in", "rb") as f:
#     arr = array.array('f')
#     arr.fromfile(f)
#     for i in arr:
#         s = 0
#         n = ""
#         tmp = str(i)
#         newarr = re.findall('[0-9]', tmp)
#         for j in newarr:
#             n += j
#             s += int(j)
                
#         print(int(n), s)

import datetime

ma = 3.26
a = round(ma, 1)
print(a)