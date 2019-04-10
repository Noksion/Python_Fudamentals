import unittest

from classes.check_class import Cartoon


class TestCartoon(unittest.TestCase):

    def test_description(self):
        zootopia = Cartoon(2016, 90)
        self.assertEqual('This cartoon is 3 years old, and it is 90 minutes long.', zootopia.get_description())


if __name__ == '__main__':
    unittest.main()
