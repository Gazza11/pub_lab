class Customer:
    def __init__(self, name, wallet, age):
        self.name = name
        self.wallet = wallet
        self.age = age
        self.drunkenness_level = 0

    def check_enough_money(self, drink):
        if self.wallet >= drink.price:
            return True
        return False

    def pay_for_drink(self, drink):
        self.wallet -= drink.price

    def drink_drink(self, drink):
        self.drunkenness_level += drink.alcohol_level

    # def buy_a_drink(self, drink_name, pub):
    #     drink_to_buy = pub.get_drink_by_name(drink_name)
    #     if drink_to_buy != None:
    #         if self.check_enough_money(drink_to_buy) == True:
    #             self.pay_for_drink(drink_to_buy, pub)
