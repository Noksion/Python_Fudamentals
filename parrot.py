saying = "\nTell me something, and I'll repeat it back to you." \
         "\nOr enter 'quit' to quit the program: "
prompt = ''
while prompt != 'quit':
    print(prompt)
    prompt = input(saying)
print('Have a nice time!')


# Below is the showcase of breaking the string
prompt = 'If you tell us who you are, we can personalize messages you see ' \
         '\nPLease tell us your name: '
name = input(prompt)
print('Hello ' + name + '!')
