# Scientific Calculator
import math

def calculator():
    print("=== Scientific Calculator ===")
    print("Operations: +, -, *, /, sqrt, pow, sin, cos, tan, log")
    op = input("Enter operation: ").strip()
    if op in ['+', '-', '*', '/']:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        if op == '+': print(f"Result: {a + b}")
        elif op == '-': print(f"Result: {a - b}")
        elif op == '*': print(f"Result: {a * b}")
        elif op == '/': print(f"Result: {a / b}" if b != 0 else "Cannot divide by zero!")
    elif op == 'sqrt':
        a = float(input("Enter number: "))
        print(f"Result: {math.sqrt(a)}")
    elif op == 'pow':
        a = float(input("Enter base: "))
        b = float(input("Enter exponent: "))
        print(f"Result: {math.pow(a, b)}")
    elif op in ['sin', 'cos', 'tan']:
        a = float(input("Enter angle in degrees: "))
        rad = math.radians(a)
        if op == 'sin': print(f"Result: {math.sin(rad)}")
        elif op == 'cos': print(f"Result: {math.cos(rad)}")
        elif op == 'tan': print(f"Result: {math.tan(rad)}")
    elif op == 'log':
        a = float(input("Enter number: "))
        print(f"Result: {math.log(a)}")

calculator()
