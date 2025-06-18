#!/usr/bin/env python3
import sys

# Method to shrink a string to the first 8 characters
def shrink(s):
    print(s[:8])  # ใช้ slicing เพื่อตัดเอาแค่ 8 ตัวแรก

# Method to enlarge a string to 8 characters by adding 'Z'
def enlarge(s):
    print(s + 'Z' * (8 - len(s)))  # เติม 'Z' ให้ครบ 8 ตัว

# ตรวจสอบว่ามีพารามิเตอร์หรือไม่
if len(sys.argv) < 2:
    print("none")
else:
    # Loop ผ่านทุกพารามิเตอร์
    for arg in sys.argv[1:]:
        if len(arg) > 8:
            shrink(arg)  # ถ้ายาวกว่า 8 ตัว ให้เรียก shrink
        elif len(arg) < 8:
            enlarge(arg)  # ถ้าสั้นกว่า 8 ตัว ให้เรียก enlarge
        else:
            print(arg)  # ถ้ายาวพอดี 8 ตัว ก็แสดงมันเลย
