import unittest
from city_function import format_geo


class CitiesTest(unittest.TestCase):
    """Tests city_function"""
    def test_city_country(self):
        """Test for city & country arguments"""
        we_get = format_geo('berlin', 'germany')
        self.assertEqual(we_get, 'Berlin, Germany')


if __name__ == '__main__':
    unittest.main()
