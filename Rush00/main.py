tasks = []

def show_menu():
    print("====== Smart Farm Task Organizer ======")
    print("1. เพิ่มงานในฟาร์ม")
    print("2. แสดงรายการงานทั้งหมด")
    print("3. ลบงาน")
    print("4. สรุปจำนวนงานในแต่ละประเภท")
    print("5. ออกจากโปรแกรม")

def add_task():
    name = input("ชื่องาน: ")
    date = input("วันที่ (dd/mm/yyyy): ")
    task_type = input("ประเภทงาน (พืชผัก/ปศุสัตว์/อื่นๆ): ").upper()
    tasks.append({"date": date, "name": name, "type": task_type})
    print("เพิ่มงานสำเร็จ!\n")

def show_tasks():
    if not tasks:
        print("ยังไม่มีงานในรายการ\n")
    else:
        print("รายการงานทั้งหมด:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task['date']} - {task['name']} (Type {task['type']})")
        print()

def delete_task():
    if not tasks:
        print("ยังไม่มีงานให้ลบ\n")
        return

    show_tasks()
    try:
        index = int(input("ลำดับของงานที่ต้องการลบ: "))
        if 1 <= index <= len(tasks):
            removed_task = tasks.pop(index - 1)
            print(f"ลบงาน: {removed_task['name']} แล้ว\n")
        else:
            print("หมายเลขไม่ถูกต้อง\n")
    except ValueError:
        print("กรุณาใส่ตัวเลขเท่านั้น\n")

def summarize_tasks():
    if not tasks:
        print("ยังไม่มีข้อมูลสำหรับสรุป\n")
        return

    summary = {}
    for task in tasks:
        task_type = task["type"]
        summary[task_type] = summary.get(task_type, 0) + 1

    print("สรุปจำนวนงานแต่ละประเภท:")
    for t_type, count in summary.items():
        print(f"- Type {t_type}: {count} งาน")
    print()
#โปรเเกรมหลัก
while True:
    show_menu()
    choice = input("เลือกเมนู (1-5): ")
    if choice == "1":
        add_task()
    elif choice == "2":
        show_tasks()
    elif choice == "3":
        delete_task()
    elif choice == "4":
        summarize_tasks()
    elif choice == "5":
        print("ขอบคุณที่ใช้โปรแกรม Smart Farm!")
        break
    else:
        print("กรุณาเลือกเมนู 1-5 เท่านั้น\n")