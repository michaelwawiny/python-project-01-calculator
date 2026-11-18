
# ==========================================
# PROJECT 01: PYTHON CALCULATOR
# Developer: Michael
# Language: Python 3
# ==========================================


# 1. MATHEMATICAL FUNCTIONS

def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero!")

    return a / b


def power(a, b):
    return a ** b


def modulus(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot calculate modulus with zero!")

    return a % b


# 2. DISPLAY CALCULATOR MENU

def display_menu():

    print("\n" + "=" * 40)
    print("          PYTHON CALCULATOR")
    print("=" * 40)

    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Exponentiation (**)")
    print("6. Modulus (%)")
    print("0. Exit")

    print("=" * 40)


# 3. GET VALID NUMBER INPUT

def get_number(message):

    while True:

        try:
            number = float(input(message))
            return number

        except ValueError:
            print("Invalid input! Please enter a valid number.")


# 4. PERFORM CALCULATION

def calculate(num1, num2, operation):

    if operation == "1":
        return add(num1, num2)

    elif operation == "2":
        return subtract(num1, num2)

    elif operation == "3":
        return multiply(num1, num2)

    elif operation == "4":
        return divide(num1, num2)

    elif operation == "5":
        return power(num1, num2)

    elif operation == "6":
        return modulus(num1, num2)

    else:
        raise ValueError("Invalid operation selected!")


# 5. MAIN CALCULATOR FUNCTION

def calculator():

    print("\nWelcome to the Python Calculator!")

    while True:

        display_menu()

        operation = input("Select an operation (0-6): ").strip()

        # Exit application

        if operation == "0":
            print("\nThank you for using our calculator!")
            print("Goodbye!")
            break

        # Validate operation

        if operation not in ["1", "2", "3", "4", "5", "6"]:
            print("\nInvalid choice! Select an operation from 0 to 6.")
            continue

        # Get numbers

        num1 = get_number("Enter first number: ")
        num2 = get_number("Enter second number: ")

        # Perform calculation

        try:

            result = calculate(num1, num2, operation)

            print("\n" + "-" * 40)
            print(f"First number:  {num1:g}")
            print(f"Second number: {num2:g}")
            print(f"Result:        {result:g}")
            print("-" * 40)

        except ZeroDivisionError as error:

            print(f"\nError: {error}")

        except OverflowError:

            print("\nError: The calculation produced a number too large to display.")

        # Ask whether to continue

        choice = input(
            "\nDo you want another calculation? (yes/no): "
        ).strip().lower()

        if choice not in ["yes", "y"]:
            print("\nThank you for using our calculator!")
            print("Goodbye!")
            break


# 6. PROGRAM ENTRY POINT

if __name__ == "__main__":
    calculator()
