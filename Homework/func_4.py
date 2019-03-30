# Написать функцию, которая принимает любое кол-во key-value аргументов
# и выводит *список* ключей (keys) в качестве рузельтата


def ret_keys(arguments):
    keys_list = []
    for i in arguments.keys():
        keys_list.append(i)
    return keys_list


proof = ret_keys({'blue': 5, 'yellow': 7, 'red': 9, 'orange': 13})
print(proof)
