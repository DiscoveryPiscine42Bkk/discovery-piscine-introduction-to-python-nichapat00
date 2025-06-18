#!/usr/bin/env python3

# Define the original array of numbers
original_array = [2, 8, 9, 48, 8, 22, -12, 2]

# Filter the values greater than 5, add 2 to each, and store them in a set (to remove duplicates)
new_array = {x + 2 for x in original_array if x > 5}

# Display both the original array and the new array (as a set)
print(f"{original_array}")
print(f"{new_array}")
