# from tkinter import * 

# app = Tk()
# app.geometry("230x300")

# entryExample = Entry(app, width=10)
# entryExample.pack(side="top", padx=10)

# txt = Text(app, width=30, height=20)
# txt.pack()
# txt.insert(END, "인서트텍스트1","인서트텍스트2") 

# app.mainloop()

# import tkinter as tk

# if __name__ == "__main__":
#     window = tk.Tk()
#     # window.title("tk")
#     # window.geometry("256x256")

#     box1 = tk.Label(window)
#     box1.configure(background="pink", width=10, borderwidth=1, relief="sunken")
#     box1.pack(pady=10, side=tk.TOP)

#     box2 = tk.Label(window)
#     box2.configure(background="orange", width=20, height=10,
#                    borderwidth=1, relief="sunken")
#     box2.configure(text="인서트텍스트1\n인서트텍스트2", anchor=tk.NW)
#     box2.pack(padx=30, side=tk.TOP)

#     window.mainloop()


import tkinter as tk

root=tk.Tk()

label1 = tk.Label(root, width=10, height=1, 
                  bg='pink', relief='sunken', bd=1)

label2 = tk.Label(root, width=20, height=10,
                  bg='orange', relief='sunken', bd=1)

label2.config(text="인서트텍스트1"+'\n'+"인서트텍스트2", anchor='nw')

label1.pack(side="top", pady=10)
label2.pack(side="top", padx=30)

root.mainloop()

# from tkinter import *
# window=Tk()

# window.geometry("200x200")

# label1=Label(window, width=10, bd=1, bg="pink", relief="sunken")
# label2=Label(window, text="인서트텍스트1\n인서트텍스트2", width=20, height=10, bg="orange", anchor=NW)

# label1.pack(side=TOP, pady=10)
# label2.pack(side=TOP)

# window.mainloop()


# from tkinter import *
# window=Tk()

# window.geometry("200x200")

# label1=Label(window, width=10, bd=1, bg="pink", relief="sunken")
# label2=Label(window, text="인서트텍스트1\n인서트텍스트2", width=20, height=10, bg="orange", anchor=NW)

# label1.pack(side=TOP, pady=10)
# label2.pack(side=TOP)

# window.mainloop()