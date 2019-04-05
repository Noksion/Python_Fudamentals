from random import randint


class Dice:
    def __init__(self, sides=6):
        self.sides = sides

    def roll_the_dice(self):
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
