import unittest
from calculator import Calculator

#  class can be any name, but usually starts with Test, "unittest.TestCase" is required
class TestOperations(unittest.TestCase):

    def setUp(self):
        # any code that needs to be run before each test can go here
        self.calc = Calculator(8,2)

    def test_sum(self):
        answer = self.calc.get_sum()
        self.assertEqual(answer, 10, "The answer wasn't 10")

    def test_difference(self):
        answer = self.calc.get_difference()
        self.assertEqual(answer, 6, "The answer wasn't 6")

    def test_product(self):
        answer = self.calc.get_product()
        self.assertEqual(answer, 16, "The answer wasn't 16")

    def test_quotient(self):
        answer = self.calc.get_quotient()
        self.assertEqual(answer, 4, "The answer wasn't 4")
        
if __name__ == '__main__':
    unittest.main()