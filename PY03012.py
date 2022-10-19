from filecmp import cmp
import functools


class SinhVien:
    def __init__(self, name, acceptedSubmit, totalSubmit):
        self.name = name
        self.acceptedSubmit = acceptedSubmit
        self.totalSubmit = totalSubmit

    def __gt__(self, a):
        if self.acceptedSubmit > a.acceptedSubmit:
            return 1
        elif self.acceptedSubmit < a.acceptedSubmit:
            return 0
        if self.totalSubmit < a.totalSubmit:
            return 1
        elif self.totalSubmit > a.totalSubmit:
            return 0
        if self.name < a.name:
            return 1
        return 0

    def __str__(self):
        return self.name + ' ' + str(self.acceptedSubmit) + ' ' + str(self.totalSubmit)

def mycomp(a, b):
    if a > b:
        return -1
    elif b > a:
        return 1
    return 0

t = int(input())
list = []
for test in range(t):
    s = input()
    a = input().split()
    list.append(SinhVien(s, int(a[0]), int(a[1])))

list.sort(key=functools.cmp_to_key(mycomp))
for i in list:
    print(i, sep='\n')
