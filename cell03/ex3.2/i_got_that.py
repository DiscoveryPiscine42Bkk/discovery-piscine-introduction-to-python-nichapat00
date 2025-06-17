#!/usr/bin/env python3

# First prompt
user_input = input("What you gotta say? : ")

# Loop until the user types "STOP" (case-sensitive)
while user_input != "STOP":
    print("I got that! Anything else? : ", end="")
    user_input = input()
