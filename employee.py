class Employee:
    def __init__(self, f_name, l_name, salary=50000):
        self.f_name = f_name
        self.l_name = l_name
        self.salary = salary

    def get_raise(self, amount=5000):
        self.salary += amount
