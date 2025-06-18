#!/usr/bin/env python3

# Method definition for greetings
def greetings(name="noble stranger"):
    # ตรวจสอบว่าพารามิเตอร์เป็นสตริงหรือไม่
    if not isinstance(name, str):
        print("Error! It was not a name.")
    else:
        print(f"Hello, {name}.")

# เรียกใช้งานฟังก์ชันเพื่อทดสอบ
greetings("Alexandra")
greetings("Wil")
greetings()  # ใช้ชื่อเริ่มต้น
greetings(42)  # ไม่ใช่สตริง
