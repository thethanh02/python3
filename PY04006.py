from math import sqrt

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def distance(self, Point):
        a = self.x - Point.x
        b = self.y - Point.y
        return sqrt(a**2 + b**2)

    def isTriangle(self, a, b):
        d1 = self.distance(a)
        d2 = self.distance(b)
        d3 = b.distance(a)
        if d1 + d2 > d3 and d2 + d3 > d1 and d1 + d3 > d2:
            area = (d1 + d2 + d3)*(d1 + d2 - d3)*(-d1 + d2 + d3)*(d1 - d2 + d3)
            return '%.2f'%(sqrt(area)/4)
        return 'INVALID'
        

t = int(input())
arr = []
for test in range(t):
    arr += [float(x) for x in input().split()]

for test in range(t):
    p1 = Point(arr[0 + test*6], arr[1 + test*6])
    p2 = Point(arr[2 + test*6], arr[3 + test*6])
    p3 = Point(arr[4 + test*6], arr[5 + test*6])
    for i in arr:
        if abs(i) > 1000:
            print('INVALID')
    else:
        print(p1.isTriangle(p2, p3))