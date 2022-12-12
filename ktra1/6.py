import functools

class DoiTuyen:
    def __init__(self, name, diemSo, hieuSo, chiSoFair):
        self.name = name
        self.diemSo = diemSo
        self.hieuSo = hieuSo
        self.chiSoFair = chiSoFair

    def __gt__(self, a):
        if self.diemSo > a.diemSo:
            return 1
        elif self.diemSo < a.diemSo:
            return 0

        if self.hieuSo > a.hieuSo:
            return 1
        elif self.hieuSo < a.hieuSo:
            return 0

        if self.chiSoFair > a.chiSoFair:
            return 1
        elif self.chiSoFair < a.chiSoFair:
            return 0
        return 0

    def __str__(self):
        return self.name + ' ' + str(self.diemSo) + ' ' + str(self.hieuSo) + ' ' + str(self.chiSoFair)

def mycomp(a, b):
    if a > b:
        return -1
    elif a < b:
        return 1
    return 0

list = []
for t in range(int(input())):
    name = input()
    a = input().split()
    list.append(DoiTuyen(name, int(a[0]), int(a[1]), int(a[2])))

list.sort(key=functools.cmp_to_key(mycomp))
for i in list:
    print(i)
    