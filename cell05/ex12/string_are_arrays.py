#!/usr/bin/env python3
import sys

# Check if exactly one parameter is passed
if len(sys.argv) != 2:
    print("none")
else:
    string = sys.argv[1]
    
    # Count occurrences of 'z' in the string
    z_count = string.count('z')
    
    # If no 'z' found, print "none", otherwise print 'z' for each occurrence
    if z_count > 0:
        print('z' * z_count)
    else:
        print("none")
