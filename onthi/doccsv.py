import csv

dulieu = []
with open('flights.csv') as file:
    data = csv.reader(file)
    dulieu = [row for row in data]

# in hang` cot`
print (len(dulieu) - 1, len(dulieu[0]))