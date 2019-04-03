class Restaurant:
    def __init__(self, name, cuisine_type):
        self.name = name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print('This restaurant is named "' + self.name.title() + '" and it serves '
              + self.cuisine_type.title() + " food.")

    def open_restaurant(self):
        print("The restaurant is now open")


class IceCreamStand(Restaurant):
    def __init__(self, name, cuisine_type='IceCream'):
        super().__init__(name, cuisine_type)
        self.flavors = ['vanilla', 'chocolate', 'strawberry']

    def get_flavors(self):
        print('You can choose an IceCream of one of the following flavors: \n')
        for i in self.flavors:
            print(' - ' + i)


billiecream = IceCreamStand('BilliCream')
billiecream.get_flavors()
