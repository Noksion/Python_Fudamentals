import datetime


class Cartoon:
    def __init__(self, year, length):
        self.year = year
        self.length = length

    def calculate_age(self):
        return datetime.datetime.now().year - self.year

    def get_description(self):
        return 'This cartoon is ' + str(self.calculate_age()) + ' years old, and it is ' + str(self.length)\
               + ' minutes long.'
