import unittest

# Functions to perform operations
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        raise ValueError("Division by zero is undefined.")
    return x / y

# Test cases class
class TestMathOperations(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(5, 3), 8)
        self.assertEqual(add(-2, -3), -5)
        self.assertEqual(add(0, 7), 7)

    def test_subtract(self):
        self.assertEqual(subtract(10, 4), 6)
        self.assertEqual(subtract(5, 8), -3)
        self.assertEqual(subtract(-5, -3), -2)

    def test_multiply(self):
        self.assertEqual(multiply(4, 5), 20)
        self.assertEqual(multiply(-3, 6), -18)
        self.assertEqual(multiply(0, 9), 0)

    def test_divide(self):
        self.assertEqual(divide(12, 4), 3)
        self.assertEqual(divide(-15, 3), -5)
        self.assertEqual(divide(0, 5), 0)
        with self.assertRaises(ValueError) as context:
            divide(5, 0)
        self.assertEqual(str(context.exception), "Division by zero is undefined.")
        self.assertEqual(divide(-10, -2), 5)

# Run the tests
if __name__ == '__main__':
    unittest.main()

# to run test: python -m unittest test_unittest_operations.py
# run with detai report: python -m unittest -v test_operations_unittest.py