# Написать функцию, которая принимает любое кол-во key-value аргументов
# и выводит *список* ключей (keys) в качестве рузельтата


def ret_keys(**arguments):
    return arguments.keys()


print(ret_keys(blue=5, yellow=7, red=9, orange=13))
