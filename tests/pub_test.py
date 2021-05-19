from src.customer import Customer
import unittest

from src.pub import Pub
from src.drink import Drink
from src.customer import Customer

class TestPub(unittest.TestCase):
    def setUp(self):
        self.drink1 = Drink('beer', 4.50, 5)
        self.drink2 = Drink('cider', 4.00, 8)
        list_of_drinks = [self.drink1, self.drink2]
        self.pub = Pub('codeclan arms', 100.00, list_of_drinks)

        self.customer1 = Customer("sadie", 30.00, 30)
        self.customer2 = Customer('matt', 0.00, 14)

    def test_pub_has_name(self):
        self.assertEqual("codeclan arms", self.pub.name)

    def test_pub_has_till(self):
        self.assertEqual(100.00, self.pub.till)

    def test_pub_has_drinks(self):
        self.assertEqual(2, len(self.pub.list_of_drinks))
    
    def test_get_drink_by_name(self):
        drink_to_be_found = self.pub.get_drink_by_name('beer')
        self.assertEqual(self.drink1, drink_to_be_found)

    def test_money_reached_pub(self):
        self.pub.sell_a_drink('beer', self.customer1)
        self.assertEqual(104.50, self.pub.till)

    @unittest.skip("Delete this line to run the test")
    def test_check_customer_age(self):
        self.assertEqual(30, self.pub.check_customer_age(self.customer1))

    @unittest.skip("Delete this line to run the test")
    def test_refuse_drink__too_young(self):
        self.assertEqual(None, self.customer2.buy_a_drink(self.drink1))
        self.assertEqual(0.00, self.customer2.wallet)
        self.assertEqual(100.00, self.pub.till)

    @unittest.skip("Delete this line to run the test")
    def test_refuse_drink__too_drunk(self):
        self.customer1.drink_drink('beer')
        self.customer1.drink_drink('cider')
        self.assertEqual(None, self.customer1.buy_a_drink(self.drink1))
        self.assertGreater(self.pub.drunkenness_cut_off, self.customer1.drunkenness_level)