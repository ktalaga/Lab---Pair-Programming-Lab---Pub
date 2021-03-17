import unittest
from src.food import Food

class TestFood(unittest.TestCase):

    def setUp(self):
        self.food = Food("Burger", 9.99, 7)

    def test_food_has_name(self):
        self.assertEqual("Burger", self.food.name)

    def test_food_has_price(self):
        self.assertEqual(9.99, self.food.price)
    
    def test_food_has_rejuvenation_level(self):
        self.assertEqual(7, self.food.rejuvenation_level)