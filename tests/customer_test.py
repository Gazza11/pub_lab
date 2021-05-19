import unittest

from src.customer import Customer
from src.pub import Pub
from src.drink import Drink

class TestCustomer(unittest.TestCase):

    def setUp(self):
        self.customer1 = Customer("sadie", 30.00)
        self.customer2 = Customer('matt', 0.00)

        self.drink1 = Drink('beer', 4.50)
        self.drink2 = Drink('cider', 4.00)
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

    @unittest.skip("Delete this line to run the test")
    def test_money_left_wallet(self):
        pay_for_drink(self.customer1, self.drink1)
        self.assertEqual(25.50, self.customer1.wallet)
    
    @unittest.skip("Delete this line to run the test")
    def test_money_reached_pub(self):
        pay_for_drink(self.customer1, self.drink1)
        self.assertEqual(104.50, self.pub.till)
    
    @unittest.skip("Delete this line to run the test")
    def test_check_drink_exists__does(self):
        drink_that_youre_looking_for = self.pub.get_drink_by_name('beer')
        check_drink_exists(drink_that_youre_looking_for)
        self.assertEqual(True, check_drink_exists)

    @unittest.skip("Delete this line to run the test")
    def test_check_drink_exists__doesnot(self):
        drink_that_youre_looking_for = self.pub.get_drink_by_name('wine')
        check_drink_exists(drink_that_youre_looking_for)
        self.assertEqual(False, check_drink_exists)