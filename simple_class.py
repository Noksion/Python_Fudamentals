class Dog:
    """A simple attempt to model a dog."""

    def __init__(self, name, age):
        """Initialize name and age attributes."""
        self.name = name
        self.age = age
        self.internal_value = 42

    def sit(self):
        """Simulate a dog sitting in response to a command."""
        print(self.name.title() + " is now sitting.")

    def print_age(self):
        """Simulate a dog sitting in response to a command."""
        print(self.name.title() + " is " + str(self.age) + " years old.")


corgi = Dog('Rex', 6)
corgi2 = Dog('Missy', 2)

corgi.sit()
corgi.print_age()
print("\n")
corgi2.sit()
corgi2.print_age()
