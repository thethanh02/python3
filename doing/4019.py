class NhanVien:
    def __init__(self, ord, name, diem1, diem2):
        self.id = 'TS0' + str(ord)
        self.name = name
        self.diem1 = (diem1 / 10) if diem1 > 10 else diem1
        self.diem2 = (diem2 / 10) if diem2 > 10 else diem2
        self.trungBinh = (self.diem1 + self.diem2) / 2
        
        if self.trungBinh < 5:
            self.loai = 'TRUOT'
        elif self.trungBinh < 8:
            self.loai = 'CAN NHAC'
        elif self.trungBinh <= 9.5:
            self.loai = 'DAT'
        else:
            self.loai = 'XUAT SAC'

    def __str__(self):
        return self.id + ' ' + self.name + ' %.2f'%(self.trungBinh) + ' ' + self.loai
        
if __name__ == '__main__':
    t = int(input())
    list = []
    for test in range(t):
        list.append(NhanVien(test + 1, input(), float(input()), float(input())))

    list.sort(key=lambda x: x.trungBinh, reverse=True)
    for i in list:
        print(i, sep='\n')
