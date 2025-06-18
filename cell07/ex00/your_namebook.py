# การสร้างฟังก์ชัน array_of_names ที่รับ dictionary เป็นพารามิเตอร์
def array_of_names(persons):
    # สร้าง list ใหม่โดยรวมชื่อและนามสกุลแล้วทำให้ตัวแรกเป็นตัวพิมพ์ใหญ่
    full_names = [f"{first.capitalize()} {last.capitalize()}" for first, last in persons.items()]
    return full_names

# เริ่มต้นโปรแกรมหลัก
if __name__ == "__main__":
    # สร้าง dictionary ของชื่อและนามสกุล
    persons = {
        "jean": "valjean",
        "grace": "hopper",
        "xavier": "niel",
        "fifi": "brindacier"
    }
    
    # เรียกใช้ฟังก์ชัน array_of_names และพิมพ์ผลลัพธ์
    print(array_of_names(persons))
