import classes.car_class


class Dog:
    """A simple attempt to model a dog."""

    def __init__(self, name, age):
        """Initialize name and age attributes."""
        self.name = name
        self.age = age

    def sit(self):
        """Simulate a dog sitting in response to a command."""
        print(self.name.title() + " is now sitting.")

    def roll_over(self):
        """Simulate rolling over in response to a command."""
        print(self.name.title() + " rolled over!")


my = classes.car_class.Car('Chevrolet', 'Camaro', 1995)
print(my.get_descriptive_name())

mo = classes.car_class.ElectricCar('Tesla', 'Voltage', 2015)
print(mo.get_descriptive_name())
