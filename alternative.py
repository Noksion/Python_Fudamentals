for i in range(1, 10):
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
        print(str(i) + ' является простым числом')
    else:
        pass
