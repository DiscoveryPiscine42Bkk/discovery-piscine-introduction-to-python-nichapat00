#!/usr/bin/env python3
import sys

# Check if there are no parameters
if len(sys.argv) == 1:
    print("none")
else:
    # Loop through each parameter passed
    for param in sys.argv[1:]:
        if not param.endswith("ism"):  # If it doesn't end with "ism"
            print(param + "ism")
