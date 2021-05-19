import unittest

from src.pub import Pub
from src.drink import Drink

class TestPub(unittest.TestCase):
    def setUp(self):
        self.drink1 = ('beer', 4.50)
        self.drink2 = ('cider', 4.00)
        list_of_drinks = [self.drink1, self.drink2]
        self.pub = Pub('codeclan arms', 100.00, list_of_drinks)

    @unittest.skip("Delete this line to run the test")   
    def test_pub_has_name(self):
        self.assertEqual("codeclan arms", self.name)

    @unittest.skip("Delete this line to run the test")
    def test_pub_has_till(self):
        self.assertEqual(100.00, self.till)

    @unittest.skip("Delete this line to run the test")
    def test_pub_has_drinks(self):
        self.assertEqual(2, len(self.list_of_drinks))
    
    @unittest.skip("Delete this line to run the test")
    def test_get_drink_by_name(self):
        get_drink_by_name(self.drink1)
        self.assertEqual('beer', self.drink1)
