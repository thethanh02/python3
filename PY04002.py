
class Rectangle:
    def __init__(self, length, width, colour):
        self.length = length
        self.width = width
        self.colour = colour

    def perimeter(self):
        return 2*(self.length + self.width)

    def area(self):
        return self.length * self.width

    def color(self):
        return self.colour.title()

arr = input().split()

if int(arr[0]) <= 0 or int(arr[1]) <= 0:
    print('INVALID')
else:
    r = Rectangle(int(arr[0]), int(arr[1]), arr[2])
    print('{} {} {}'.format(r.perimeter(), r.area(), r.color()))