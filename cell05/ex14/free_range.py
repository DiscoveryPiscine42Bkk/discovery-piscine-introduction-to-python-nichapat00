#!/usr/bin/env python3
import sys

# Check if exactly two parameters are passed
if len(sys.argv) != 3:
    print("none")
else:
    try:
        # Convert the parameters to integers
        start = int(sys.argv[1])
        end = int(sys.argv[2])

        # Create a list using range() and print it
        print(list(range(start, end + 1)))
    except ValueError:
        # In case the parameters are not integers, print "none"
        print("none")
