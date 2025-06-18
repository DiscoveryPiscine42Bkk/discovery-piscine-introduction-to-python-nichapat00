#!/usr/bin/env python3
import sys

# Method definition for downcase_it
def downcase_it(s):
    return s.lower()  # ใช้ .lower() เพื่อแปลงข้อความเป็นตัวพิมพ์เล็ก

# Check if there are parameters passed
if len(sys.argv) < 2:
    print("none")
else:
    # Loop through all parameters and apply downcase_it
    for arg in sys.argv[1:]:  # เริ่มจาก index 1 เพราะ index 0 คือตัวชื่อโปรแกรม
        print(downcase_it(arg))
