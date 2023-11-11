#!/usr/bim/python3

import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):
    def setUp(self):
        # This is the test fixture - creating an instance of the Calculator
        self.calculator = Calculator()

    def tearDown(self):
        # Cleanup actions, if needed
        pass

    def test_add(self):
        # Test case for the add method
        result = self.calculator.add(3, 5)
        self.assertEqual(result, 8)

    def testsubtract(self):
        # Test case for the subtract method
        result = self.calculator.subtract(8, 3)
        self.assertEqual(result, 5)

if __name__ == "__main__":
    unittest.main()

