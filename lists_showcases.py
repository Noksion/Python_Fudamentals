dig = [4, 5, 18, 39]
print(sum(dig))


games = ['Wow', 'Diablo', 'StarCraft']
for i in games:
    print("I have played the game of " + i.upper() + ' for about a decade')


numbers = [i**3 for i in range(1, 11)]
print((sum(numbers)))


m_list = ['English', 'Ukrainian', 'Russian']
y_list = m_list[:]
m_list.append('Spanish')
y_list.append('German')
for i in y_list:
    print('My friend knows ' + str(i) + ' language')


sq = []
for v in range(1, 11):
        v = v ** 2
        sq.append(v)

