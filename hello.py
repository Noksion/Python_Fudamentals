num = 4
for i in range (2, num -1):
    if num % i == 0:
        print (str (num) + ' is not a prime number')
        break
    else:
        print (str (num) + ' is a prime number')
        break
