# simple_calculator.py
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b

a, b = 10, 5
print(f"Add: {add(a, b)}")
print(f"Subtract: {subtract(a, b)}")
print(f"Multiply: {multiply(a, b)}")
print(f"Divide: {divide(a, b)}")
