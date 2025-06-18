# การสร้างฟังก์ชัน add_one ที่รับพารามิเตอร์แล้วเพิ่มค่า 1
def add_one(num):
    return num + 1  # เพิ่ม 1 แล้วส่งค่ากลับ

# เริ่มต้นโปรแกรมหลัก
if __name__ == "__main__":
    # กำหนดค่าตัวแปรเริ่มต้น
    my_variable = 5
    
    # แสดงค่าตัวแปรก่อนการเพิ่มค่า
    print("ก่อนการเพิ่มค่า:", my_variable)
    
    # เรียกฟังก์ชัน add_one และอัพเดตค่าของ my_variable
    my_variable = add_one(my_variable)
    
    # แสดงค่าตัวแปรหลังจากที่เพิ่มค่า
    print("หลังการเพิ่มค่า:", my_variable)

