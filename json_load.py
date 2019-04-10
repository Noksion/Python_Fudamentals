import json


file = 'numbers.json'
with open(file) as obj:
    numbers = json.load(obj)

print(numbers)
