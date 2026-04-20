def add(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        return "Error: Only numbers allowed!"
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        return "Error: Only numbers allowed!"
    if b == 0:
        return "Error: Division by zero!"
    return round(a / b, 2)

def power(a, b):
    return a ** b

def modulus(a, b):
    return a % b

print("Calculator Results:")
print("Add:", add(10, 5))
print("Subtract:", subtract(10, 5))
print("Multiply:", multiply(10, 5))
print("Divide:", divide(10, 5))
print("Power:", power(3, 4))
print("Modulus:", modulus(10, 3))