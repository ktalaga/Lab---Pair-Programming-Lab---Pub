# from src.customer import Customer
# from src.drink import Drink





class Pub:
    def __init__(self,name, till):
        self.name = name
        self.till = till
        self.drinks = {"Mango and Lemonade":100, "whisky":100, "beer":1000}

    def sell_drink(self, customer, drink):
        if drink == "Mango and Lemonade":
            self.drinks["Mango and Lemonade"] -= 1
        self.till += drink.price


    def check_age(self, customer):
        if customer.age >= 18:
            return True
        else:
            return False
    
    def refuse_to_sell_if_drunk(self, customer):
        if customer.drunkenness <= 10:
            return True
        else:
            return False



