for i in range(0, 100):
    x = 2
    c = True
    while i > x:
        if i % x == 0:
            c = False
            x = x + 1
        else:
            x = x + 1
    if c is True:
        print(str(i) + 'is a prime number')
    else:
        pass
