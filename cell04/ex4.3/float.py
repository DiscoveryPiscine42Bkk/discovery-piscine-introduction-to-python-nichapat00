#!/usr/bin/env python3

num_str = input("Give me a number: ")

try:
    num = float(num_str)
    # Check if the number is effectively an integer (e.g., 42.00)
    if num.is_integer():
        print("This number is an integer.")
    else:
        print("This number is a decimal.")
except ValueError:
    print("Please enter a valid number.")
