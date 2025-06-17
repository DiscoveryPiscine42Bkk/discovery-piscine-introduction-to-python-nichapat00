#!/usr/bin/env python3

try:
    # Get two numbers from the user
    num1 = float(input("Give me the first number: "))
    num2 = float(input("Give me the second number: "))

    print("Thank you!")

    # Perform and display calculations
    print(f"{num1:g} + {num2:g} = {num1 + num2:g}")
    print(f"{num1:g} - {num2:g} = {num1 - num2:g}")

    # Handle division by zero gracefully
    if num2 != 0:
        print(f"{num1:g} / {num2:g} = {num1 / num2:g}")
    else:
        print(f"{num1:g} / {num2:g} = Undefined (division by zero)")

    print(f"{num1:g} * {num2:g} = {num1 * num2:g}")

except ValueError:
    print("Please enter valid numbers.")
