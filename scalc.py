import math
import unittest
from scientific_calculator import sin, cos, tan, sqrt, log, exp

class TestScientificCalculator(unittest.TestCase):

    # Test cases for sin function
    def test_sin_positive(self):
        self.assertAlmostEqual(sin(90), 1)

    def test_sin_negative(self):
        self.assertAlmostEqual(sin(-90), -1)

    def test_sin_zero(self):
        self.assertAlmostEqual(sin(0), 0)

    def test_sin_invalid_input(self):
        with self.assertRaises(TypeError):
            sin("hello")

    # Test cases for cos function
    def test_cos_positive(self):
        self.assertAlmostEqual(cos(0), 1)

    def test_cos_negative(self):
        self.assertAlmostEqual(cos(180), -1)

    def test_cos_invalid_input(self):
        with self.assertRaises(TypeError):
            cos("cos")

    # Test cases for tan function
    def test_tan_positive(self):
        self.assertAlmostEqual(tan(45), 1)

    def test_tan_invalid_input(self):
        with self.assertRaises(TypeError):
            tan("abc")

    # Test cases for sqrt function
    def test_sqrt_positive(self):
        self.assertEqual(sqrt(16), 4)

    def test_sqrt_negative(self):
        with self.assertRaises(ValueError):
            sqrt(-1)

    def test_sqrt_invalid_input(self):
        with self.assertRaises(TypeError):
            sqrt("348")

    # Test cases for log function
    def test_log_positive(self):
        self.assertAlmostEqual(log(10), math.log(10))

    def test_log_non_positive(self):
        with self.assertRaises(ValueError):
            log(0)

    def test_log_invalid_input(self):
        with self.assertRaises(TypeError):
            log("test")

    # Test cases for exp function
    def test_exp_positive(self):
        self.assertAlmostEqual(exp(1), math.exp(1))

    def test_exp_non_positive(self):
        self.assertAlmostEqual(exp(1), math.exp(1))

    def test_exp_invalid_input(self):
        with self.assertRaises(TypeError):
            exp("err")

if __name__ == '__main__':
    unittest.main()
