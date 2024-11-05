 import unittest
import math
from scientific_calculator import sin, cos, tan, sqrt, log, exp

class TestScientificCalculator(unittest.TestCase):
    
    def check_invalid_input(self, func):
        with self.assertRaises(TypeError):
            func("varma")

    # Test cases for sin function
    def test_sin(self):
        self.assertAlmostEqual(sin(90), 1)
        self.assertAlmostEqual(sin(-90), -1)
        self.assertAlmostEqual(sin(0), 0)
        self.check_invalid_input(sin)

    # Test cases for cos function
    def test_cos(self):
        self.assertAlmostEqual(cos(0), 1)
        self.assertAlmostEqual(cos(180), -1)
        self.check_invalid_input(cos)

    # Test cases for tan function
    def test_tan(self):
        self.assertAlmostEqual(tan(45), 1)
        self.check_invalid_input(tan)

    # Test cases for sqrt function
    def test_sqrt(self):
        self.assertEqual(sqrt(16), 4)
        with self.assertRaises(ValueError):
            sqrt(-1)
        self.check_invalid_input(sqrt)

    # Test cases for log function
    def test_log(self):
        self.assertAlmostEqual(log(10), math.log(10))
        with self.assertRaises(ValueError):
            log(0)
        self.check_invalid_input(log)

    # Test cases for exp function
    def test_exp(self):
        self.assertAlmostEqual(exp(1), math.exp(1))
        self.check_invalid_input(exp)

if __name__ == '__main__':
    unittest.main()
