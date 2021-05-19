class Pub:
    def __init__(self, name, till, list_of_drinks):
        self.name = name
        self.till = till
        self.list_of_drinks = list_of_drinks

    def get_drink_by_name(self, drink_name):
        for drink in self.list_of_drinks:
            if drink.name == drink_name:
                return drink

    def check_drink_exists(self, input_drink):
        for drink in self.list_of_drinks:
            if drink == input_drink:
                return True
        return False

    def sell_a_drink(self, drink_name, customer):
        drink_to_sell = self.get_drink_by_name(drink_name)
        if self.check_drink_exists(drink_to_sell) == True:
            if customer.age >= 18:
                if customer.check_enough_money(drink_to_sell) == True:
                    customer.pay_for_drink(drink_to_sell)
                    self.till += drink_to_sell.price



