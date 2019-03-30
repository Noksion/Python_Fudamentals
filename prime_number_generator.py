num1 = int(input("Please enter lowest number: "))
num2 = int(input("Please enter highest number: "))


def prime_num(name1, name2):
    for i in range(name1, 1 + name2):
        if name1 < 1:
            print('Please provide a number that is >= 1')
            return False
        x = 2
        c = True
        while i > x:
            if i % x == 0:
                c = False
                x = x + 1
            else:
                x = x + 1
        if c is True:
            print(str(i) + ' is a prime number')
        else:
            pass


prime_num(num1, num2)
