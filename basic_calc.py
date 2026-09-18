# ```python
import math

history = []


def add_history(expression, result):
    history.append(f"{expression} = {result}")


def show_history():
    print("\n===== CALCULATION HISTORY =====")

    if len(history) == 0:
        print("No calculations yet.")
        return

    for i, calculation in enumerate(history, start=1):
        print(f"{i}. {calculation}")


def basic_calculator():
    print("\n===== BASIC CALCULATOR =====")

    try:
        num1 = float(input("Enter first number: "))
        operator = input("Enter operator (+, -, *, /, %, **): ").strip()
        num2 = float(input("Enter second number: "))

        if operator == "+":
            result = num1 + num2

        elif operator == "-":
            result = num1 - num2

        elif operator == "*":
            result = num1 * num2

        elif operator == "/":
            if num2 == 0:
                print("Error: Cannot divide by zero.")
                return
            result = num1 / num2

        elif operator == "%":
            if num2 == 0:
                print("Error: Cannot divide by zero.")
                return
            result = num1 % num2

        elif operator == "**":
            result = num1 ** num2

        else:
            print("Error: Invalid operator.")
            return

        print("Result:", result)
        add_history(f"{num1} {operator} {num2}", result)

    except ValueError:
        print("Error: Please enter valid numbers.")


def scientific_calculator():
    print("\n===== SCIENTIFIC CALCULATOR =====")
    print("1. Square")
    print("2. Square Root")
    print("3. Cube")
    print("4. Power")
    print("5. Factorial")
    print("6. Sine")
    print("7. Cosine")
    print("8. Tangent")
    print("9. Natural Log")
    print("10. Log Base 10")

    choice = input("\nChoose an operation: ").strip()

    try:
        if choice == "1":
            num = float(input("Enter number: "))
            result = num ** 2
            expression = f"{num}^2"

        elif choice == "2":
            num = float(input("Enter number: "))

            if num < 0:
                print("Error: Cannot calculate the square root of a negative number.")
                return

            result = math.sqrt(num)
            expression = f"sqrt({num})"

        elif choice == "3":
            num = float(input("Enter number: "))
            result = num ** 3
            expression = f"{num}^3"

        elif choice == "4":
            num = float(input("Enter base: "))
            power = float(input("Enter power: "))
            result = num ** power
            expression = f"{num}^{power}"

        elif choice == "5":
            num = int(input("Enter a non-negative integer: "))

            if num < 0:
                print("Error: Factorial cannot be negative.")
                return

            result = math.factorial(num)
            expression = f"{num}!"

        elif choice == "6":
            num = float(input("Enter angle in degrees: "))
            result = math.sin(math.radians(num))
            expression = f"sin({num})"

        elif choice == "7":
            num = float(input("Enter angle in degrees: "))
            result = math.cos(math.radians(num))
            expression = f"cos({num})"

        elif choice == "8":
            num = float(input("Enter angle in degrees: "))

            # Prevent extremely large tangent values around 90 + 180n degrees
            radians = math.radians(num)
            cosine = math.cos(radians)

            if abs(cosine) < 1e-12:
                print("Error: Tangent is undefined at this angle.")
                return

            result = math.tan(radians)
            expression = f"tan({num})"

        elif choice == "9":
            num = float(input("Enter number: "))

            if num <= 0:
                print("Error: Logarithm requires a positive number.")
                return

            result = math.log(num)
            expression = f"ln({num})"

        elif choice == "10":
            num = float(input("Enter number: "))

            if num <= 0:
                print("Error: Logarithm requires a positive number.")
                return

            result = math.log10(num)
            expression = f"log10({num})"

        else:
            print("Error: Invalid choice.")
            return

        print("Result:", result)
        add_history(expression, result)

    except ValueError:
        print("Error: Please enter a valid number.")


def percentage_calculator():
    print("\n===== PERCENTAGE CALCULATOR =====")

    try:
        number = float(input("Enter number: "))
        percentage = float(input("Enter percentage: "))

        result = (number * percentage) / 100

        print(f"{percentage}% of {number} = {result}")

        add_history(f"{percentage}% of {number}", result)

    except ValueError:
        print("Error: Please enter valid numbers.")


def constants():
    print("\n===== MATHEMATICAL CONSTANTS =====")
    print("1. Pi (π)")
    print("2. Euler's Number (e)")

    choice = input("Choose a constant: ").strip()

    if choice == "1":
        result = math.pi
        print("π =", result)
        add_history("π", result)

    elif choice == "2":
        result = math.e
        print("e =", result)
        add_history("e", result)

    else:
        print("Error: Invalid choice.")


def main():
    while True:
        print("\n" + "=" * 40)
        print("       ADVANCED PYTHON CALCULATOR")
        print("=" * 40)

        print("1. Basic Calculator")
        print("2. Scientific Calculator")
        print("3. Percentage Calculator")
        print("4. Mathematical Constants")
        print("5. Calculation History")
        print("6. Exit")

        choice = input("\nEnter your choice: ").strip()

        if choice == "1":
            basic_calculator()

        elif choice == "2":
            scientific_calculator()

        elif choice == "3":
            percentage_calculator()

        elif choice == "4":
            constants()

        elif choice == "5":
            show_history()

        elif choice == "6":
            print("\nCalculator closed.")
            break

        else:
            print("\nError: Please choose a number from 1 to 6.")


if __name__ == "__main__":
    main()