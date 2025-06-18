#!/usr/bin/env python3

# Prompt the user for a number
try:
    number = float(input())
    
    # Check the value and print the appropriate message
    if number < 0:
        print("This number is negative.")
    elif number > 0:
        print("This number is positive.")
    else:
        print("This number is both positive and negative.")
except ValueError:
    print("Please enter a valid number.")
