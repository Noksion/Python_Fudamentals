responses = {}
active = True

while active:
    name = input('What is your name?: ')
    response = input("What is your favorite city?: ")
    responses[name] = response

    check = input('Do you want another person to take a poll? (yes / no): ')
    if check.lower() == 'no':
        active = False

print('\n\t--- Poll Results ---\n')
for name, city in responses.items():
    print(name.title() + "'s favorite city is: " + city.title())
