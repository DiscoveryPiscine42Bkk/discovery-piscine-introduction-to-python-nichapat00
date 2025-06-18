#!/usr/bin/env python3
import sys

# Check if there is exactly one parameter passed
if len(sys.argv) == 2:
    # Convert the parameter to lowercase and print it
    print(sys.argv[1].lower())
else:
    # If not exactly one parameter, print "none"
    print("none")
