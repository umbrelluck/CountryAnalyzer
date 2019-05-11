"""Doctests for CountriesAST"""
import unittest
from unittest import TestCase
from country import CountriesADT, Country
import random


class TestCountriesADT(TestCase):
    def setUp(self):
        best_countries = ["Grenada", "Brunei", "Seychelles", "Kuwait"]
        print('Creating ADT...')
        self.ADT = CountriesADT(best_countries)

    def test_correct_ADT(self):
        for country in self.ADT:
            self.assertEqual(isinstance(country, Country),
                             'elements in ADT are not children of Country')

    def test_append(self):
        random.seed(692)
        for i in range(32):
            neg = random.random()
            pos = random.random()
            interest = random.random()
            if pos + neg > 1:
                pos /= 2
            self.ADT.append(Country('Country ' + str(i + 1), -neg, 1 - pos - neg, pos, interest))
        for i in range(4):
            self.ADT.countries.pop(0)
        for country in self.ADT:
            self.assertTrue(isinstance(country, Country),
                            'elements in ADT are not children of Country')

    def test__stable(self):
        self.assertTrue(True)

    def test_stability(self):
        self.assertTrue(not self.ADT.stability(), 'should be stable')


if __name__ == '__main__':
    unittest.main()
