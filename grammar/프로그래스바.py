from tkinter import *
from tkinter.ttk import *
import time

root = Tk()
root.title("코딩코딩")
root.geometry("480x360")

# # progressbar = ttk.Progressbar(root, maximum=100, mode="indeterminate")
# progressbar = ttk.Progressbar(root, maximum=100, mode="determinate")
# progressbar.start(10)
# progressbar.pack()

# def btncmd():
#     progressbar.stop()
    
# btn = Button(root, text="중지", command=btncmd).pack()

p_var2 = DoubleVar()
progressbar2 = Progressbar(root, maximum=100, length=150, variable=p_var2)
progressbar2.pack()

def btncmd2():
    for i in range(101): # 1 ~ 101
        time.sleep(0.01) # 0.01초 대기
        
        p_var2.set(i) # progressbar 값 설정
        progressbar2.update() # ui 업데이트
        print(p_var2.get())
        
btn = Button(root, text="시작", command=btncmd2).pack()

root.mainloop()