import unittest
from src.pub import Pub
from src.customer import Customer
from src.drink import Drink
from src.pub import Pub

class TestPub(unittest.TestCase):

    def setUp(self):
        
        self.pub = Pub("The Prancing Pony", 100.00)

    def test_pub_has_name(self):
        self.assertEqual("The Prancing Pony", self.pub.name)

    def test_pub_has_till(self):
        self.assertEqual(100, self.pub.till)

    def test_pub_has_drinks(self):
        self.assertEqual({"Mango and Lemonade":100, "whisky":100, "beer":1000}, self.pub.drinks)

    def test_check_age(self):
        customer_1 = Customer("Jack", 500, 18, 0)
        self.assertEqual(True, self.pub.check_age(customer_1))
    
    def test_refuse_to_sell_if_drunk(self):
        customer_1 = Customer("Jack", 500, 18, 0)
        customer_2 = Customer("Mike", 300, 70, 20)
        customer_3 = Customer("Susan", 100, 16, 0)
        self.assertEqual(True, self.pub.refuse_to_sell_if_drunk(customer_1))
        self.assertEqual(False, self.pub.refuse_to_sell_if_drunk(customer_2))


        

    def test_sell_drink(self):
        customer = Customer("Jack", 500, 18, 0)
        drink_1 = Drink("Mango and Lemonade", 5, 2)
        pub = Pub("The Prancing Pony", 100.00)
        pub.sell_drink(customer, drink_1)
        self.assertEqual(99, pub.drinks["Mango and Lemonade"])