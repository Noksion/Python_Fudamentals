from classes.car_class import Car, ElectricCar

my = Car('Chevrolet', 'Camaro', 1995)
print(my.get_descriptive_name())

mo = ElectricCar('Tesla', 'Voltage', 2015)
print(mo.get_descriptive_name())
