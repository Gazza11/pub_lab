import unittest

from src.drink import Drink

class TestDrink(unittest.TestCase):
    def setUp(self):
        self.drink = Drink("martini", 8.50)

    def test_drink_has_name(self):
        self.assertEqual("martini", self.name)

    def test_drink_has_price(self):
        self.assertEqual(8.50, self.price)
