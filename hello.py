def is_prime(num):
    if num < 1:
        return False
    if num <= 3:
        return True

    for n in range(2, num - 1):
        if num % n == 0:
            return False
        else:
            return True


for i in range(0, 100):
    if is_prime(i):
        print (str(i) + ' is a prime number')



