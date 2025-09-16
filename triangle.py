import tkinter as tk
from tkinter import messagebox

def calculate_area():
    try:
        base = float(entry_base.get())
        height = float(entry_height.get())
        area = 0.5 * base * height
        messagebox.showinfo("ผลลัพธ์", f"พื้นที่สามเหลี่ยม = {area}")
    except ValueError:
        messagebox.showerror("ข้อผิดพลาด", "กรุณากรอกตัวเลขเท่านั้น")

root = tk.Tk()
root.title("คำนวณพื้นที่สามเหลี่ยม")
root.geometry("350x200")

font_thai = ("Noto Sans Thai", 14)   # ใช้ชื่อ family ตรง ๆ

label_base = tk.Label(root, text="ฐาน (Base):", font=font_thai)
label_base.pack(pady=5)
entry_base = tk.Entry(root, font=font_thai)
entry_base.pack()

label_height = tk.Label(root, text="สูง (Height):", font=font_thai)
label_height.pack(pady=5)
entry_height = tk.Entry(root, font=font_thai)
entry_height.pack()

btn_calculate = tk.Button(root, text="คำนวณพื้นที่", command=calculate_area, font=font_thai)
btn_calculate.pack(pady=10)

root.mainloop()
