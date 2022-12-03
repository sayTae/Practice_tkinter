from tkinter import *
import tkinter.ttk as ttk

root = Tk()
root.title("코딩코딩")
root.geometry("480x360")

values = [str(i) + "일" for i in range(1, 32)]
combobox = ttk.Combobox(root, height=10, values=values, state="readonly")
combobox.pack()
combobox.set("카드 결제일")

def btncmd():
    print(combobox.get())
    
btn = ttk.Button(root, text="선택", command=btncmd).pack()

root.mainloop()