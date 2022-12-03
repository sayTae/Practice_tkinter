import tkinter as tk
import tkinter.messagebox as msgbox

root = tk.Tk()
root.title("코딩코딩")
root.geometry("480x360")

# 기차 예매 시스템
def info():
    msgbox.showinfo("알림", "정상적으로 예매 완료되었습니다.")
    
def warn():
    msgbox.showwarning("경고", "해당 좌석은 매진되었습니다.")
    
def error():
    msgbox.showerror("에러", "결제 오류가 발생했습니다.")
    
def okcancel():
    msgbox.askokcancel("확인 / 취소", "해당 좌석은 유아 동반석 입니다.")
    
def retrycancel():
    msgbox.askretrycancel("재시도 / 취소", "일시적인 오류입니다. 다시 시도하시겠습니까?")
    
def yesno():
    msgbox.askyesno("예 / 아니오", "해당 죄석은 역방향입니다. 예매 하시겠습니까?")
    
def yesnocancel():
    response = msgbox.askyesnocancel(title=None, message="예매 내역이 저장되지 않았습니다.\n저장 후 종료 하시겠습니까?")
    # 네 : 저장 후 종료
    # 아니오 : 저장 하지 않고 종료
    # 취소 : 프로그램 종료 취소 (현재 화면에서 계속 작업)
    print("응답:", response) # True, False, None -> 예 1, 아니오 0, 그 외
    if response == 1: # 네, ok
        print("예")
    elif response == 0: # 아니오, no
        print("아니오")
    else:
        print("취소")
    
tk.Button(root, command=info, text="알림").pack()
tk.Button(root, command=warn, text="경고").pack()
tk.Button(root, command=error, text="에러").pack()

tk.Button(root, command=okcancel, text="확인 취소").pack()
tk.Button(root, command=retrycancel, text="재시도 취소").pack()
tk.Button(root, command=yesno, text="예 아니오").pack()
tk.Button(root, command=yesnocancel, text="예 아니오 취소").pack()

root.mainloop()