import tkinter as tk

root = tk.Tk()
root.title("코딩코딩")
root.geometry("480x360")

frame = tk.Frame(root)
frame.pack()

scrollbar = tk.Scrollbar(frame)
scrollbar.pack(side="right", fill="y")

# set이 없으면 스크롤을 내려도 다시 올라옴
listbox = tk.Listbox(frame, selectmode="extended", height=10, yscrollcommand=scrollbar.set)

for i in range(1, 32): # 1 ~31일
    listbox.insert(tk.END, str(i) + "일") # 1일, 2일, ..
listbox.pack(side="left")

scrollbar.config(command=listbox.yview)

root.mainloop()