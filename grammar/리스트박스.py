import tkinter as tk

root = tk.Tk()
root.title("코딩코딩")
root.geometry("480x360")

label1 = tk.Label(root, text="메뉴를 선택하셈").pack()

burger_var = tk.IntVar()
btn_burger1 = tk.Radiobutton(root, text="햄버거", value=1, variable=burger_var)
btn_burger2 = tk.Radiobutton(root, text="치킨버거", value=2, variable=burger_var)
btn_burger3 = tk.Radiobutton(root, text="치즈버거", value=3, variable=burger_var)

btn_burger1.pack()
btn_burger2.pack()
btn_burger3.pack()

drink_var = tk.StringVar()

btn_drink1 = tk.Radiobutton(root, text="콜라", value="콜라", variable=drink_var)
btn_drink1.select()
btn_drink2 = tk.Radiobutton(root, text="사이다", value="사이다", variable=drink_var)

btn_drink1.pack()
btn_drink2.pack()

def btncmd():
    print(burger_var.get())
    print(drink_var.get())

btn = tk.Button(root, text="클릭", command=btncmd)
btn.pack()

root.mainloop()