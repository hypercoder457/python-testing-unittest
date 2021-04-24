from unittest import TestCase
import unittest

from .city_country import form_city_country_string


class CityCountryTestCase(TestCase):
    def test_city_country(self):
        city_country_string = form_city_country_string("Santiago", "Chile")
        self.assertEqual(city_country_string, "Santiago, Chile")

    def test_city_country_population(self):
        city_country_population_string = form_city_country_string(
            "Santiago", "Chile", population=50000)
        self.assertEqual(city_country_population_string,
                         "Santiago, Chile, population 50000")


if __name__ == '__main__':
    unittest.main()
