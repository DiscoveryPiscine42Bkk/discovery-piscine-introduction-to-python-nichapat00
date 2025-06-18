#!/usr/bin/env python3
import sys

# Check if the number of parameters passed is different from 1
if len(sys.argv) != 2:
    print("none")
else:
    # Get the parameter passed
    parameter = sys.argv[1]
    
    # Ask the user to enter a word
    user_input = input("What was the parameter? ")

    # Check if the user's input matches the parameter
    if user_input == parameter:
        print("Good job!")
    else:
        print(f"Nope, sorry...\n")
