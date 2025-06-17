#!/usr/bin/env python3

# Ask the user for their age
try:
    age = int(input("Please tell me your age: "))

    # Display the current and future ages
    print(f"You are currently {age} years old.")
    print(f"In 10 years, you'll be {age + 10} years old.")
    print(f"In 20 years, you'll be {age + 20} years old.")
    print(f"In 30 years, you'll be {age + 30} years old.")
except ValueError:
    print("Please enter a valid number for your age.")
