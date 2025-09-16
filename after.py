import tkinter as tk

def countdown(n):
    if n > 0:
        label.config(text=f"{n} วินาที")
        root.after(1000, countdown, n-1)
    else:
        label.config(text="เวลาเสร็จสิ้น!")
        # แสดงข้อมูลนักเรียน
        info = (
            "ชื่อ - นามสกุล: ภูมิฉัตร ปานทุ่ง\n"
            "ชื่อเล่น: ภูมิ\n"
            "ห้องเรียน: 5/8\n"
            "แผนการเรียน: วิทย์-คณิต\n"
            "อยากเรียนคณะอะไร: วิศวะเครื่องกล\n"
        )
        info_label.config(text=info)

root = tk.Tk()
root.title("นับเวลาถอยหลัง")

label = tk.Label(root, text="", font=("Arial", 24))
label.pack(pady=20)

info_label = tk.Label(root, text="", font=("Arial", 14), justify="left")
info_label.pack(pady=10)

# เริ่มนับถอยหลัง 10 วินาที
countdown(10)

root.mainloop()
