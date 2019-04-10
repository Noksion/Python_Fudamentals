import unittest

from Homework.funk_2 import get_last


class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual(4, get_last(1, 2, 3, 4))


if __name__ == '__main__':
    unittest.main()
