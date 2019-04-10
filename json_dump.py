import json


numbers = [1, 18, 19, 2, 14, 6, 4, 91]
f_name = 'numbers.json'
with open(f_name, 'w') as f_obj:
    json.dump(numbers, f_obj)
