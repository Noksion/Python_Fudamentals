print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")

while True:
    f_n = input('First number: ')
    if f_n == 'q':
        break
    s_n = input('Second number: ')
    if s_n == 'q':
        break
    try:
        answer = int(f_n) / int(s_n)
    except ZeroDivisionError:
        print("You can't divide by zero!")
    else:
        print(answer)


filename = 'alice.txt'

try:
    with open(filename) as f_obj:
        contents = f_obj.read()
except FileNotFoundError:
    print("Sorry, the " + filename + " file doesn't exist.")

title = 'Alice in Wonderland'
print(len(title.split()))
