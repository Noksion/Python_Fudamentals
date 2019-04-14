import unittest
from employee import Employee


class TestEmployee(unittest.TestCase):
    """Tests for Employee class"""
    def setUp(self):
        """Creating an instance of a class. Salary is standard, 50000"""
        self.jensen = Employee('Adam', 'Jensen')

    def test_standard_raise(self):
        """Tests standard raise of 5000"""
        self.jensen.get_raise()
        self.assertEqual(self.jensen.salary, 55000)

    def test_manual_raise(self):
        """Tests manual raise"""
        self.jensen.get_raise(13000)
        self.assertEqual(self.jensen.salary, 63000)


if __name__ == '__main__':
    unittest.main()
