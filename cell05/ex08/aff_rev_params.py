#!/usr/bin/env python3
import sys

# Check if there are fewer than two parameters (excluding the script name)
if len(sys.argv) < 2:
    print("none")
else:
    # Reverse the parameters and print each one on a new line
    for param in reversed(sys.argv[1:]):
        print(param)
