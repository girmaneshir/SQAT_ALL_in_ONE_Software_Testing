import pytest

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

# Test cases
@pytest.mark.parametrize("input1, input2, expected, operation", [
    (5, 3, 8, "add"),
    (-2, -3, -5, "add"),
    (0, 7, 7, "add"),
    (10, 4, 6, "subtract"),
    (5, 8, -3, "subtract"),
    (-5, -3, -2, "subtract"),
    (4, 5, 20, "multiply"),
    (-3, 6, -18, "multiply"),
    (0, 9, 0, "multiply"),
    (12, 4, 3, "divide"),
    (-15, 3, -5, "divide"),
    (0, 5, 0, "divide"),
    (5, 0, None, "divide"),  # Placeholder for exception
    (-10, -2, 5, "divide"),
])
def test_operations(input1, input2, expected, operation):
    if operation == "add":
        assert add(input1, input2) == expected
    elif operation == "subtract":
        assert subtract(input1, input2) == expected
    elif operation == "multiply":
        assert multiply(input1, input2) == expected
    elif operation == "divide":
        if input2 == 0:
            with pytest.raises(ValueError, match="Division by zero is undefined."):
                divide(input1, input2)
        else:
            assert divide(input1, input2) == expected

# To run the tests, use the command: pytest <filename>.py
# To install: pip install pytest
# To run test:pytest test_pytest_operations.py
# to run with detail report: pytest -v test_pytest_operations.py