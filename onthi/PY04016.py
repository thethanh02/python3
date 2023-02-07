from datetime import datetime

def format_name(s):
    return ' '.join([i.lower().capitalize() for i in s.split()])

class Person:
    def __init__(self, id, name, soPhong, time_start, time_end, tienDV):
        self.id = 'KH%02d'%(id+1)
        self.name = name
        self.soPhong = soPhong
        self.duration = (datetime.strptime(time_end, '%d/%m/%Y') - datetime.strptime(time_start, '%d/%m/%Y')).days + 1
        self.tienDV = tienDV
        self.setThanhTien()

    def setThanhTien(self):
        if self.soPhong[0] == '1':
            self.thanhTien = 25
        elif self.soPhong[0] == '2':
            self.thanhTien = 34
        elif self.soPhong[0] == '3':
            self.thanhTien = 50
        else:
            self.thanhTien = 80
        
        self.thanhTien = self.thanhTien * self.duration + self.tienDV

    def __str__(self):
        return f'{self.id} {self.name} {self.soPhong} {self.duration} {self.thanhTien}'


test = int(input())
arr = []
for t in range(test):
    arr.append(Person(t, input(), input(), input().strip(), input().strip(), int(input())))

arr = sorted(arr, key=lambda x:x.thanhTien, reverse=True)
print(*arr, sep='\n')
