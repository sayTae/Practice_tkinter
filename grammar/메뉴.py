import tkinter as tk

root = tk.Tk()
root.title("코딩코딩")
root.geometry("480x360")

menu = tk.Menu(root)

def creat_new_file():
    print("새 파일을 만듭니다.")
    
def creat_new_window():
    print("새 윈도우를 만듭니다.")

#file 메뉴
menu_file = tk.Menu(menu, tearoff=0)
menu_file.add_command(label="New file", command=creat_new_file)
menu_file.add_command(label="New window", command=creat_new_window)
menu_file.add_separator()
menu_file.add_command(label="Open file...")
menu_file.add_separator()
menu_file.add_command(label="Save All", state="disable")
menu_file.add_separator()
# menu_file.insert_separator(1)
menu_file.add_command(label="Exit", command=root.quit)
menu.add_cascade(label="File", menu=menu_file)

#edit 메뉴
menu.add_cascade(label="Edit")

# Language 메뉴 추가
menu_lang = tk.Menu(menu, tearoff=0)
menu_lang.add_radiobutton(label="Python")
menu_lang.add_radiobutton(label="Java")
menu_lang.add_radiobutton(label="C++")
menu.add_cascade(label="Laguage",menu=menu_lang)

# View 메뉴
menu_view = tk.Menu(menu, tearoff=0)
menu_view.add_checkbutton(label="Show minimap")
menu.add_cascade(label="View", menu=menu_view)

root.config(menu=menu)
root.mainloop()