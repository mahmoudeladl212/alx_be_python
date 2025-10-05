#!/usr/bin/env python3
"""
Unit tests for SimpleCalculator class
"""

import unittest
from simple_calculator import SimpleCalculator


class TestSimpleCalculator(unittest.TestCase):
    """Test cases for SimpleCalculator class"""

    def setUp(self):
        """Set up a calculator instance before each test"""
        self.calc = SimpleCalculator()

    def test_add(self):
        """Test addition method with various scenarios"""
        # Test positive numbers
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(10, 15), 25)
        
        # Test negative numbers
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(-5, -3), -8)
        
        # Test with zero
        self.assertEqual(self.calc.add(0, 5), 5)
        self.assertEqual(self.calc.add(7, 0), 7)
        self.assertEqual(self.calc.add(0, 0), 0)
        
        # Test floating point numbers
        self.assertEqual(self.calc.add(2.5, 3.5), 6.0)
        self.assertEqual(self.calc.add(-1.5, 2.5), 1.0)

    def test_subtract(self):
        """Test subtraction method with various scenarios"""
        # Test positive numbers
        self.assertEqual(self.calc.subtract(5, 3), 2)
        self.assertEqual(self.calc.subtract(10, 15), -5)
        
        # Test negative numbers
        self.assertEqual(self.calc.subtract(-1, 1), -2)
        self.assertEqual(self.calc.subtract(-5, -3), -2)
        
        # Test with zero
        self.assertEqual(self.calc.subtract(0, 5), -5)
        self.assertEqual(self.calc.subtract(7, 0), 7)
        self.assertEqual(self.calc.subtract(0, 0), 0)
        
        # Test floating point numbers
        self.assertEqual(self.calc.subtract(5.5, 2.5), 3.0)
        self.assertEqual(self.calc.subtract(1.5, 2.5), -1.0)

    def test_multiply(self):
        """Test multiplication method with various scenarios"""
        # Test positive numbers
        self.assertEqual(self.calc.multiply(2, 3), 6)
        self.assertEqual(self.calc.multiply(5, 4), 20)
        
        # Test negative numbers
        self.assertEqual(self.calc.multiply(-2, 3), -6)
        self.assertEqual(self.calc.multiply(-2, -3), 6)
        
        # Test with zero
        self.assertEqual(self.calc.multiply(0, 5), 0)
        self.assertEqual(self.calc.multiply(7, 0), 0)
        self.assertEqual(self.calc.multiply(0, 0), 0)
        
        # Test floating point numbers
        self.assertEqual(self.calc.multiply(2.5, 4), 10.0)
        self.assertEqual(self.calc.multiply(1.5, 2.0), 3.0)
        
        # Test identity property
        self.assertEqual(self.calc.multiply(1, 5), 5)
        self.assertEqual(self.calc.multiply(5, 1), 5)

    def test_divide(self):
        """Test division method with various scenarios"""
        # Test normal division
        self.assertEqual(self.calc.divide(6, 3), 2.0)
        self.assertEqual(self.calc.divide(10, 2), 5.0)
        
        # Test negative numbers
        self.assertEqual(self.calc.divide(-6, 3), -2.0)
        self.assertEqual(self.calc.divide(6, -3), -2.0)
        self.assertEqual(self.calc.divide(-6, -3), 2.0)
        
        # Test floating point results
        self.assertEqual(self.calc.divide(5, 2), 2.5)
        self.assertEqual(self.calc.divide(1, 4), 0.25)
        
        # Test division by one
        self.assertEqual(self.calc.divide(7, 1), 7.0)
        
        # Test division of zero
        self.assertEqual(self.calc.divide(0, 5), 0.0)

    def test_divide_by_zero(self):
        """Test division by zero returns None"""
        self.assertIsNone(self.calc.divide(5, 0))
        self.assertIsNone(self.calc.divide(-5, 0))
        self.assertIsNone(self.calc.divide(0, 0))

    def test_operations_with_large_numbers(self):
        """Test operations with large numbers"""
        # Large positive numbers
        self.assertEqual(self.calc.add(1000000, 2000000), 3000000)
        self.assertEqual(self.calc.multiply(1000, 1000), 1000000)
        
        # Large negative numbers
        self.assertEqual(self.calc.add(-1000000, -2000000), -3000000)


if __name__ == '__main__':
    # Run the tests
    unittest.main()