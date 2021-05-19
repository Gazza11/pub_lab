class Customer:
    def __init__(self, name, wallet):
        self.name = name
        self.wallet = wallet

    def check_enough_money(self, drink):
        if self.wallet >= drink.price:
            return True
        return False

    def pay_for_drink(self,drink):
        self.wallet -= drink.price
