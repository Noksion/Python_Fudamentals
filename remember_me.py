import json

username = input('What is your name?: ')
filename = 'username.json'

with open(filename, 'w') as obj:
    json.dump(username, obj)
    print("We'll remember you when you come back, " + username + '!')
