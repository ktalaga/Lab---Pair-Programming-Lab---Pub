# from src.drink import Drink
from src.pub import Pub

class Customer:
    def __init__(self,name, wallet, age, drunkenness):
        self.name = name
        self.wallet = wallet
        self.age = age
        self.drunkenness = drunkenness

    def increase_drunkenness(self, drink):
        self.drunkenness += drink.alcohol_level

    def buy_drink(self, drink):
        self.wallet -= drink.price

    def buy_food(self, food):
        self.wallet -= food.price
        self.drunkenness -= food.rejuvenation_level



    #     def buy_drink(self, drink):
    # self.wallet -= drink.price
    # pub.till += drink.price


        