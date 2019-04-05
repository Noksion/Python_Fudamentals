from random import randint


class Dice:
    """Imitates the dice which can have as many sides as user wants. Default dice has 6 sides"""
    def __init__(self, sides=6):
        self.sides = sides

    def roll_the_dice(self):
        """Imitates the dice roll. Prints a random number between 1 and the amount of sides"""
        print(randint(1, self.sides))


billy = Dice()
dilly = Dice(10)
gilly = Dice(20)

for i in range(1, 11):
    billy.roll_the_dice()

print('')
for i in range(1, 11):
    dilly.roll_the_dice()

print('')
for i in range(1, 11):
    gilly.roll_the_dice()
