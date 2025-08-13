from tkinter import *
root = Tk()
root.title("kuiyai")

def Showmessage():
    Label(text = "ชื่อ ภูมิฉัตร ปานทุ่ง" , fg="purple",font="60",bg="white").pack()
    Label(text = "ชั้นม.5/8" ,fg="purple",font="60",bg="white").pack()
    Label(text = "เลขที่ 4" ,fg="purple",font="60",bg="white").pack()
    
btnl = Button(root,text="information",comand=Showmessage).pack()

root.geometry("750x500")
root.mainloop()