# Function Tests Program
# Project 2: Barista Coffee Assistant
#
# Name: Joanna Chou
# Section: 07
# Date: 1/29/2022 
#
from baristaCoffeeFuncs import *
import unittest

class MyTestCase(unittest.TestCase):    
    def test_coffee_cost(self):
        self.assertEqual(coffee_cost("Americano", "No extras", "Small"), 2.75)
        self.assertEqual(coffee_cost("americano", "No extras", "Medium"), 2.95)
        self.assertEqual(coffee_cost("aMeRiCaNo", "No extras", "Large"), 3.25)
        
        self.assertEqual(coffee_cost("Americano", "Milk on the side", "small"), 3.00)
        self.assertEqual(coffee_cost("Americano", "Milk on the side", "Medium"), 3.20)
        self.assertEqual(coffee_cost("Americano", "Milk on the side", "LARGE"), 3.50)

        self.assertEqual(coffee_cost("Espresso", "No extras", "Small"), 2.75)
        self.assertEqual(coffee_cost("espresso", "No extras", "Medium"), 2.95)
        self.assertEqual(coffee_cost("eSpReSsO", "No extras", "Large"), 3.25)

        self.assertEqual(coffee_cost("Espresso", "Milk on the side", "small"), 3.00)
        self.assertEqual(coffee_cost("Espresso", "Milk on the side", "Medium"), 3.20)
        self.assertEqual(coffee_cost("Espresso", "Milk on the side", "LARGE"), 3.50)

        self.assertEqual(coffee_cost("Latte", "No extras", "Small"), 2.85)
        self.assertEqual(coffee_cost("latte", "No extras", "Medium"), 3.75)
        self.assertEqual(coffee_cost("lAtTe", "No extras", "Large"), 4.15)

        self.assertEqual(coffee_cost("Flat White", "No extras", "Small"), 2.95)
        self.assertEqual(coffee_cost("flat white", "No extras", "Medium"), 3.00)
        self.assertEqual(coffee_cost("fLaT wHiTe", "No extras", "Large"), 3.75)

if __name__ == '__main__':
    unittest.main()
