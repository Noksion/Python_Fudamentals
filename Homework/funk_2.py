# Написать функцию, которая принимает любое количество аргументов и печатает последний элемент.


def ret_last(*args):
    checklist = []
    for i in args:
        checklist.append(i)
    print(checklist[-1])


ret_last(1, 2, 3, 4, 5, 6, 18)
