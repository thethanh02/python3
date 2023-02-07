from datetime import datetime

def format_name(s):
    return ' '.join([i.lower().capitalize() for i in s.split()])

class Person:
    def __init__(self, name, time_start, time_end) -> None:
        self.name = name
        self.duration = (datetime.strptime(time_end, '%d/%m/%Y %H:%M:%S') - datetime.strptime(time_start, '%d/%m/%Y %H:%M:%S')).seconds // 60 + (datetime.strptime(time_end, '%d/%m/%Y %H:%M:%S') - datetime.strptime(time_start, '%d/%m/%Y %H:%M:%S')).days * 24 * 60

    def __str__(self) -> str:
        return f'{format_name(self.name)} {self.duration}'


file = open('ONLINE.in')

n = int(file.readline().strip())
list_customer = []
for i in range(n):
    list_customer.append(
        Person(file.readline().strip(), file.readline().strip(), file.readline().strip()))

list_customer.sort(key=lambda x: (-x.duration, x.name))
for customer in list_customer:
    print(customer)
