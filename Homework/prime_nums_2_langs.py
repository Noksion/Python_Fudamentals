# Выводит два отдельных списка, Рус и Англ.

num1 = int(input("Please enter lowest number: "))
num2 = int(input("Please enter highest number: "))


def prime_gen(name1, name2):
    prime_list = []
    if name1 < 1:
        print('Please try again and provide number that is >= 1')
        return False
    for k in range(name1, 1 + name2):
        x = 2
        c = True
        while k > x:
            if k % x == 0:
                c = False
                x = x + 1
            else:
                x = x + 1
        if c is True:
            prime_list.append(k)
        else:
            pass
    return prime_list


material = prime_gen(num1, num2)

print('')
for i in material:
    print(str(i) + ' is a prime number')
print('')
for i in material:
    print(str(i) + ' Является простым числом')
