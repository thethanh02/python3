import csv

dulieu = []
with open('flights.csv') as file:
    data = csv.reader(file)
    dulieu = [row for row in data]

# print(dulieu)
print (len(dulieu) - 1, len(dulieu[0]))