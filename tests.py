import unittest

from operations import *
from calculator import *
from ui import *

class CalculatorTestCase(unittest.TestCase):

    # Test function
    def test_multiply(self):
		result = calculate_multiplication(3, 5)
        self.assertion(15, result)

    def test_calculate_subtraction_success(self):
        result = calculate_subtraction(10,5,1)
        self.assertEqual(4, result)


if __name__ == '__main__':
    unittest.main()
