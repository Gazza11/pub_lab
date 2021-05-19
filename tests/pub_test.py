import unittest

from src.pub import Pub
from src.drink import Drink

class TestPub(unittest.TestCase):
    def setUp(self):
        self.drink1 = Drink('beer', 4.50)
        self.drink2 = Drink('cider', 4.00)
        list_of_drinks = [self.drink1, self.drink2]
        self.pub = Pub('codeclan arms', 100.00, list_of_drinks)

    def test_pub_has_name(self):
        self.assertEqual("codeclan arms", self.pub.name)

    def test_pub_has_till(self):
        self.assertEqual(100.00, self.pub.till)

    def test_pub_has_drinks(self):
        self.assertEqual(2, len(self.pub.list_of_drinks))
    
    def test_get_drink_by_name(self):
        drink_to_be_found = self.pub.get_drink_by_name('beer')
        self.assertEqual(self.drink1, drink_to_be_found)
