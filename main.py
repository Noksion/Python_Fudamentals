def pure_pop(list):
    return list[0: -1]

'''
dig = [4, 5, 18, 39]
print(sum(dig))


games = ['Wow', 'Diablo', 'StarCraft']
for i in games:
   print("I have played the game of " + i.upper() + ' for about a decade')


numbers = [i**3 for i in range(1, 11)]
print((sum(numbers)))


m_list = ['English', 'Ukrainian', 'Russain']
y_list = m_list[:]
m_list.append('Spanish')
y_list.append('German')
for i in y_list:
    print('My friend knows ' + str(i) + ' language')
    
    
favorite_languages = {
 'jen': 'python',
 'sarah': 'c',
 'edward': 'ruby',
 'phil': 'python',
 }
for i in set(favorite_languages.values()):
    print(i.title())

'''

'''
sq = []
for v in range (1, 11):
    v = v**2
    sq.append(v)


favorite_languages = {
 'jen': ['python', 'ruby'],
 'sarah': ['c'],
 'edward': ['ruby', 'go'],
 'phil': ['python', 'haskell'],
 }
for name, languages in favorite_languages.items():
    print("\n" + name.title() + "'s favorite languages are:")
    for i in languages:
        print("\t" + i.title())


m = 45.3
h = 1.59
imt = m / (h**2)
print(imt)


prompt = 'If you tell us who you are, we can personalize messages you see ' \
         '\nPLease tell us your name: '
name = input(prompt)
print('Hello ' + name + '!')
'''

saying = "\nTell me something, and I'll repeat it back to you." \
         "\nOr enter 'quit' to quit the program: "
prompt = ''
while prompt != 'quit':
    print(prompt)
    prompt = input(saying)

print('Have a nice time!')
