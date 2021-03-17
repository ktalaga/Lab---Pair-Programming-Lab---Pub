import unittest
from src.drink import Drink

class TestDrink(unittest.TestCase):

    def setUp(self):
        self.drink = Drink("Mango and Lemonade", 5, 2)

    def test_drink_has_name(self):
        self.assertEqual("Mango and Lemonade", self.drink.name)

    def test_drink_has_price(self):
        self.assertEqual(5, self.drink.price)

    def test_drink_has_alcohol_level(self):
        self.assertEqual(2, self.drink.alcohol_level)