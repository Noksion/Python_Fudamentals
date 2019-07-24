sum_of = []


def sum_of_previous(n):
    if n < 0:
        return False
    elif n == 0:
        return 0
    else:
        for i in range(1, n+1):
            sum_of.append(i)


sum_of_previous(5)
print(sum(sum_of))
