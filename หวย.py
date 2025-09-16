import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time
from datetime import datetime
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def fetch_lottery():
    try:
        options = Options()
        options.add_argument("--headless=new")
        service = Service()
        driver = webdriver.Chrome(service=service, options=options)

        driver.get("https://www.lottery.co.th/small")
        time.sleep(3)
        html = driver.page_source
        driver.quit()

        soup = BeautifulSoup(html, "lxml")
        buttons = soup.find_all("button", class_="btn btn-primary")

        numbers = [btn.find("strong").text.strip()
                   for btn in buttons if btn.find("strong")]
        result_text = []
        if len(numbers) >= 6:
            result_text.append("รางวัลที่ 1 : " + numbers[0])
            result_text.append("")
            result_text.append("เลขท้าย 2 ตัว : " + numbers[1])
            result_text.append("เลขหน้า 3 ตัว : {} , {}".format(numbers[2], numbers[3]))
            result_text.append("เลขท้าย 3 ตัว : {} , {}".format(numbers[4], numbers[5]))
        else:
            result_text = [f"- {n}" for n in numbers]

        result_box.config(state=tk.NORMAL)
        result_box.delete("1.0", tk.END)
        result_box.insert(tk.END, "\n".join(result_text))
        result_box.config(state=tk.DISABLED)

        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        status_label.config(text=f"อัปเดตล่าสุด: {now}")
    except Exception as e:
        messagebox.showerror("Error", f"ไม่สามารถดึงข้อมูลได้\n{e}")
      
root = tk.Tk()
root.title("โปรแกรมตรวจผลสลากกินแบ่งรัฐบาล")
root.geometry("650x550")

title_label = tk.Label(
    root, text="ผลสลากกินแบ่งรัฐบาล", font=("Arial", 20, "bold"), fg="blue"
)
title_label.pack(pady=10)

btn_frame = tk.Frame(root)
btn_frame.pack(pady=5)

btn_fetch = ttk.Button(btn_frame, text="ดึงผลรางวัล", command=fetch_lottery)
btn_fetch.pack(side=tk.LEFT, padx=10)

btn_exit = ttk.Button(btn_frame, text="ออก", command=root.quit)
btn_exit.pack(side=tk.LEFT, padx=10)

frame = tk.Frame(root)
frame.pack(fill="both", expand=True, padx=20, pady=10)

scrollbar = tk.Scrollbar(frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

result_box = scrolledtext.ScrolledText(
    frame, wrap="word", font=("Arial", 12), yscrollcommand=scrollbar.set
)
result_box.pack(fill="both", expand=True)

scrollbar.config(command=result_box.yview)
result_box.config(state=tk.DISABLED)

status_label = tk.Label(root, text="ยังไม่ได้ดึงข้อมูล", anchor="w")
status_label.pack(fill="x", padx=20, pady=(0, 10))

root.mainloop()
