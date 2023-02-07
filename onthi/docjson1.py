import json
  
f = open('flights.json')
b = json.load(f)

# in hang cot (no la so thuoc tinh va so du lieu cua thuoc tinh)
print(len(b['flights']), len(b['flights'][0]))