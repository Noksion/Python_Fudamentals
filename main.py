# Игра в угадывание чисел.
# Когда освою генератор рандомных чисел - значение переменной check будет генерироваться им
# И можно будет полноценно играть.
import random

check = random.randint(1, 30)

while True:
    digit = int(input('Try to guess the number: '))

    if digit < check:
        print('Too low, try again!')

    if digit > check:
        print('Too high, try again!')

    if digit == check:
        print("That's correct! Have a nice time!")
        break
