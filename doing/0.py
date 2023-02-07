a, b, c = [int(x) for x in input().split()]

def checkTriangle(a, b, c):
    if a + b <= c or a + c <= b or b + c <= a:
        return 'Khong phai tam giac'
    else:
        if a*a + b*b == c*c or c*c + b*b == a*a or a*a + c*c == b*b:
            return 'Tam giac vuong'
        elif a == b and b == c:
            return 'Tam giac deu'
        elif a == b or a == c or b == c:
            return 'Tam giac can'
        else:
            return 'Tam giac thuong'

