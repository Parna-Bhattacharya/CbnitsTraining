class Calculator:
    def __init__(self):
        pass

    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        pass

    def multiply(self, a, b):
        pass

    def divide(self, a, b):
        # if b == 0:
        #     return "Error! Division by zero is not allowed."
        # return a / b
        return a / b


# Creating object of Calculator class
calc = Calculator()

while True:
    print("\nSimple OOP Calculator")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == '5':
        print("Exiting calculator...")
        break

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == '1':
        print("Result:", calc.add(num1, num2))
    elif choice == '2':
        print("Result:", calc.subtract(num1, num2))
    elif choice == '3':
        print("Result:", calc.multiply(num1, num2))
    elif choice == '4':
        print("Result:", calc.divide(num1, num2))
    else:
        print("Invalid choice! Please try again.")
