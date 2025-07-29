lang=input("Enter the programming language: ")
print(f"You entered: {lang} is a great language!")

try:
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    result = float(num1) , float(num2)
    print(result)
except ValueError:
    print("Invalid input! Please enter valid integers.")
else:
    operation = input("Enter the operation (add/subtract/multiply/divide): ").strip().lower()
    if operation == "add":
        print(f"The sum is: {num1 + num2}")
    elif operation == "subtract":
        print(f"The difference is: {num1 - num2}")
    elif operation == "multiply":
        print(f"The product is: {num1 * num2}")
    elif operation == "divide":
        try:
            if num2 != 0:
                print(f"The quotient is: {num1 / num2}")
        except ZeroDivisionError:
            print("Error: Division by zero is not allowed.")
    else:
        print("Invalid operation! Please choose from add, subtract, multiply, or divide.")