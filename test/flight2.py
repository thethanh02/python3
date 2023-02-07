import json
  
f = open('flights.json')
b = json.load(f)
print(len(b['flights']), len(b['flights'][0]))