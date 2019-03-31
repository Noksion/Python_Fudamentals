# Игра в угадывание чисел.
import random


def game():
    check = random.randint(1, 10)
    attempts = 0

    while True:
        digit = int(input('Try to guess the number: '))
        attempts += 1

        if digit < check:
            print('Too low, try again!')

        if digit > check:
            print('Too high, try again!')

        if digit == check:
            print("\nThat's correct! It took you " + str(attempts) + " attempts to hit the right number."
                                                                     "\n\t Have a nice time!")
            break

