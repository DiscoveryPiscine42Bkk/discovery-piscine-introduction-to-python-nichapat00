#!/usr/bin/env python3
import re
import sys

# Check if there are exactly two parameters
if len(sys.argv) != 3:
    print("none")
else:
    keyword = sys.argv[1]
    text = sys.argv[2]

    # Use re.findall to find all occurrences of the keyword in the string
    occurrences = len(re.findall(re.escape(keyword), text))

    # If the keyword is found, print the number of occurrences, otherwise print "none"
    if occurrences > 0:
        print(occurrences)
    else:
        print("none")
