import unittest 
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        """Create an instance of SimpleCalculator for testing."""
        self.calc =SimpleCalculator()

        def test_addition(self):
            #Test the add method.
            self.assertEqual(self.calc.add(2, 3), 5)
            self.assertEqual(self.calc.add(-2, 2), 0)
            self.assertEqual(self.calc.add(-4, -6), 10)

        def test_subtract(self):
            self.assertEqual(self.calc.subtract(5, 3), 2)
            self.assertEqual(self.calc.subtract(3, 5), -2)
            self.assertEqual(self.calc.subtract(0, 0), 0)
            self.assertEqual(self.calc.subtract(-3, -7), 4)

        def test_multiply(self):
            self.assertEqual(self.calc.multiply(4, 5), 20)
            self.assertEqual(self.calc.multiply(0, 5), 0)
            self.assertEqual(self.calc.multiply(-3, 7), -21)
            self.assertEqual(self.calc.multiply(-4, -2), 8)

        def test_division(self):
            self.assertEqual(self.calc.divide(6, 3), 2)
            self.assertEqual(self.calc.divide(5, 2), 2.5)
            self.assertEqual(self.calc.divide(-10, 2), -5)
            self.assertEqual(self.calc.divide(-10, -2), 5)
            self.assertIsNone(self.calc.divide(5, 0), "Division by zero should return None")

if __name__ == "_main_":
    unittest.main()
