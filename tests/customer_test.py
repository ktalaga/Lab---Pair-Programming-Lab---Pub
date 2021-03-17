import unittest
from src.customer import Customer
from src.drink import Drink
from src.pub import Pub
from src.food import Food

class TestCustomer(unittest.TestCase):

    def setUp(self):
        self.customer = Customer("Jack", 500, 18, 0)


    def test_customer_has_name(self):
        self.assertEqual("Jack", self.customer.name)

    def test_customer_has_wallet(self):
        self.assertEqual(500, self.customer.wallet)

    def test_buy_drink(self):
        customer = Customer("Jack", 500, 18, 0)
        drink_1 = Drink("Mango and Lemonade", 5, 2)
        pub = Pub("The Prancing Pony", 100.00)
        pub.sell_drink(customer, drink_1)
        customer.buy_drink(drink_1)
        self.assertEqual(495, customer.wallet)
        self.assertEqual(105, pub.till)

    def test_customer_has_drunkenness(self):
        self.assertEqual(0, self.customer.drunkenness)

    def test_increase_drunkenness(self):
        customer = Customer("Jack", 500, 18, 0)
        drink_1 = Drink("Mango and Lemonade", 5, 2)
        customer.increase_drunkenness(drink_1)
        self.assertEqual(2, customer.drunkenness)

    def test_decrease_drunkenness(self):
        customer = Customer("Bob", 500, 18, 20)
        food_1 = Food("Burger", 9.99, 7)
        customer.buy_food(food_1)
        self.assertEqual(13, customer.drunkenness)