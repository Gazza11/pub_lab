import unittest

from src.customer import Customer
from src.pub import Pub
from src.drink import Drink

class TestCustomer(unittest.TestCase):

    def setUp(self):
        self.customer1 = Customer("sadie", 30.00, 30)
        self.customer2 = Customer('matt', 0.00, 14)

        self.drink1 = Drink('beer', 4.50, 5)
        self.drink2 = Drink('cider', 4.00, 8)
        list_of_drinks = [self.drink1, self.drink2]
        self.pub = Pub('codeclan arms', 100.00, list_of_drinks)


    def test_customer_name(self):
        self.assertEqual("sadie", self.customer1.name)


    def test_has_wallet(self):
        self.assertEqual(30.00, self.customer1.wallet)


    def test_check_enough_money__has_enough(self):
        affordability_check = self.customer1.check_enough_money(self.drink1)
        self.assertEqual(True, affordability_check)


    def test_check_enough_money__does_not_has_enough(self):
        affordability_check = self.customer2.check_enough_money(self.drink1)
        self.assertEqual(False, affordability_check)

    def test_money_left_wallet(self):
        self.customer1.pay_for_drink(self.drink1, self.pub)
        self.assertEqual(25.50, self.customer1.wallet)
    
    def test_money_reached_pub(self):
        self.customer1.pay_for_drink(self.drink1, self.pub)
        self.assertEqual(104.50, self.pub.till)
    
    def test_check_drink_exists__does(self):
        drink_that_youre_looking_for = self.pub.get_drink_by_name('beer')
        existence_check = self.pub.check_drink_exists(drink_that_youre_looking_for)
        self.assertEqual(True, existence_check )

    def test_check_drink_exists__doesnot(self):
        drink_that_youre_looking_for = self.pub.get_drink_by_name('wine')
        existence_check = self.pub.check_drink_exists(drink_that_youre_looking_for)
        self.assertEqual(False, existence_check)

    def test_buy_a_drink__drink_exists(self):
        self.customer1.buy_a_drink('beer', self.pub)
        self.assertEqual(25.50, self.customer1.wallet)
        self.assertEqual(104.50, self.pub.till)

    def test_buy_a_drink__drink_does_not_exists(self):
        self.customer1.buy_a_drink('wine', self.pub)
        self.assertEqual(30.00, self.customer1.wallet)
        self.assertEqual(100.00, self.pub.till)

    @unittest.skip("Delete this line to run the test")
    def test_customer_has_age(self):
        self.assertEqual(30, self.customer1.age)

    @unittest.skip("Delete this line to run the test")
    def test_customer_has_drunkenness_level(self):
        self.assertIsNotNone(self.customer1.drunkenness_level)

    @unittest.skip("Delete this line to run the test")
    def test_customer_gets_drunk__one_drink(self):
        self.customer1.drink_drink('beer')
        self.assertEqual(5, self.customer1.drunkenness_level)

    @unittest.skip("Delete this line to run the test")
    def test_customer_gets_drunk__multiple_drinks(self):
        self.customer1.drink_drink('beer')
        self.customer1.drink_drink('cider')
        self.assertEqual(13, self.customer1.drunkenness_level)
