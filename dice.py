from random import randint


class Dice:
    """Imitates the dice which can have as many sides as user wants. Default dice has 6 sides"""
    def __init__(self, sides=6):
        self.sides = sides

    def roll_the_dice(self):
        """Imitates the dice roll. Prints a random number between 1 and the amount of sides"""
        print(randint(1, self.sides))


dice_6 = Dice()
dice_10= Dice(10)
dice_20 = Dice(20)

for i in range(1, 11):
    dice_6.roll_the_dice()

print('')
for i in range(1, 11):
    dice_10.roll_the_dice()

print('')
for i in range(1, 11):
    dice_20.roll_the_dice()
