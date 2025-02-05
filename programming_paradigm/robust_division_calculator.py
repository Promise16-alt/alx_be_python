import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    # Test addition method
    def test_addition(self):
        """Test the addition method."""
        self.assertEqual(self.calc.add(2, 3), 5)  # normal case
        self.assertEqual(self.calc.add(-1, 1), 0)  # negative number
        self.assertEqual(self.calc.add(0, 0), 0)  # zero addition
        self.assertEqual(self.calc.add(-2, -3), -5)  # both negative

    # Test subtraction method
    def test_subtraction(self):
        """Test the subtraction method."""
        self.assertEqual(self.calc.subtract(5, 3), 2)  # normal case
        self.assertEqual(self.calc.subtract(3, 5), -2)  # negative result
        self.assertEqual(self.calc.subtract(0, 0), 0)  # zero subtraction
        self.assertEqual(self.calc.subtract(-3, -2), -1)  # negative numbers

    # Test multiplication method
    def test_multiplication(self):
        """Test the multiplication method."""
        self.assertEqual(self.calc.multiply(2, 3), 6)  # normal case
        self.assertEqual(self.calc.multiply(-2, 3), -6)  # negative result
        self.assertEqual(self.calc.multiply(0, 5), 0)  # multiplication by zero
        self.assertEqual(self.calc.multiply(-2, -3), 6)  # both negative

    # Test division method
    def test_division(self):
        """Test the division method."""
        self.assertEqual(self.calc.divide(10, 2), 5.0)  # normal division
        self.assertEqual(self.calc.divide(-10, 2), -5.0)  # negative result
        self.assertEqual(self.calc.divide(0, 5), 0.0)  # division by any number when numerator is 0
        self.assertEqual(self.calc.divide(5, 0), None)  # division by zero should return None
        self.assertEqual(self.calc.divide(10, -2), -5.0)  # negative divisor

    # Edge case: Test division by zero specifically for error handling
    def test_division_by_zero(self):
        """Test division by zero error handling."""
        result = self.calc.divide(5, 0)
        self.assertIsNone(result, "Expected None when dividing by zero")

if __name__ == "__main__":
    unittest.main()
