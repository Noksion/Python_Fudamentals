import unittest
from lambda_showcase import *


class TestLambdas(unittest.TestCase):
    def test_increment(self):
        self.x = increment_5()
        self.assertEqual(self.x(75), 80)

    def test_order_of_sum(self):
        self.y = order_of_sum(3)
        self.assertEqual(self.y(1, 4), 125)


if __name__ == '__main__':
    unittest.main()
