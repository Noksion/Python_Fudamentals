class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.country = 'Ukraine'
        self.status = 'Active'

    def describe_user(self):
        print('User description:\n\tFirst Name: ' + self.first_name + '\n\tLast Name: ' + self.last_name +
              '\n\tCountry: ' + self.country)

    def greeting_user(self):
        print('Hello ' + self.first_name + " " + self.last_name + ' from ' + self.country)


class Admin(User):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.privileges = ['edit posts', 'ban other users']

    def show_privileges (self):
        print('As an Admin, this user can: ')
        for i in self.privileges:
            print('\t- ' + i)


lissov = Admin('Anton', 'Lissov')
lissov.show_privileges()
