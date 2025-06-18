#!/usr/bin/env python3

# Prompt the user
print("Enter a number")
try:
    num = int(input())

    # Display multiplication table from 0 to 9
    for i in range(10):
        print(f"{i} x {num} = {i * num}")
except ValueError:
    print("Please enter a valid integer.")
