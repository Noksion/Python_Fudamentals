class Car:
    """A simple attempt to represent the car"""
    def __init__(self, brand, model, year):
        """Initialize attributes to describe a car."""
        self.brand = brand
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = str(self.year) + " " + self.brand + " " + self.model
        return long_name.title()

    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self, mileage):
        """
        Set the odometer reading to the given value.
        Reject the change if it attempts to roll the odometer back.
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""
        self.odometer_reading += miles


class Battery:
    """A simple attempt to model a battery for an electric car."""
    def __init__(self, battery_size=70):
        """Initialize the battery's attributes."""
        self.battery_size = battery_size

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print("This car has a " + str(self.battery_size) + "-kWh battery.")

    def upgrade_battery(self,):
        if self.battery_size == 70:
            self.battery_size += 15
        print('The battery was upgraded')

    def get_range(self):
        if self.battery_size == 70:
            print('This car can go approximately 210 miles on a full charge.')
        elif self.battery_size == 85:
            print('This car can go approximately 255 miles on a full charge.')


class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""
    def __init__(self, brand, model, year):
        """
         Initialize attributes of the parent class.
         Then initialize attributes specific to an electric car.
         """
        super().__init__(brand, model, year)
        self.battery = Battery()


tesla = ElectricCar('Tesla', 'Voltage', 2017)
print(tesla.get_descriptive_name())
tesla.battery.get_range()
tesla.battery.upgrade_battery()
tesla.battery.get_range()
