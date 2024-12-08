# math_operations.py

def add(x, y):
    return float(x) + float(y)

def subtract(x, y):
    return float(x) - float(y)

def multiply(x, y):
    return float(x) * float(y)

def divide(x, y):
    if y == 0:
        raise ValueError("Division by zero is undefined.")
    return float(x) / float(y)