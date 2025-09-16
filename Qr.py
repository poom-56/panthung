
from tkinter import *
import pyqrcode
from PIL import Image, ImageTk

def generate_qr():
    name = name_entry.get()
    link = link_entry.get()

    if name.strip() == "" or link.strip() == "":
        status_label.config(text="กรุณากรอกข้อมูลให้ครบ", fg="red")
        return

    qr = pyqrcode.create(link)
    file_name = f"{name}.png"
    qr.png(file_name, scale=8)

    img = Image.open(file_name)
    img = img.resize((200, 200))
    img_tk = ImageTk.PhotoImage(img)

    qr_label.config(image=img_tk)
    qr_label.image = img_tk
    status_label.config(text=f"Create {file_name} Finished!", fg="green")

root = Tk()
root.title("QRCode Generator")
canvas = Canvas(root, width=400, height=500)
canvas.pack()

app_label = Label(root, text="QRCode Generator", font=('Arial', 20, 'bold'))
canvas.create_window(200, 40, window=app_label)

name_label = Label(root, text="QR Name")
canvas.create_window(200, 80, window=name_label)

name_entry = Entry(root)
canvas.create_window(200, 100, window=name_entry)

link_label = Label(root, text="URL / Text")
canvas.create_window(200, 140, window=link_label)

link_entry = Entry(root)
canvas.create_window(200, 160, window=link_entry)

button = Button(text="Create QR Code", command=generate_qr)
canvas.create_window(200, 200, window=button)

qr_label = Label(root)
canvas.create_window(200, 300, window=qr_label)

status_label = Label(root, text="", font=("Arial", 10))
canvas.create_window(200, 400, window=status_label)

root.mainloop()
