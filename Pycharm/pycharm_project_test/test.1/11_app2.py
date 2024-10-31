import tkinter as tk

def dispLable():  # 함수를 추가
    lbl.configure(text="안녕하세요")
    
rook=tk.Tk() # 화면을 만든다
rook.geometry("200x200")    # 화면의 크리를 정한다(단위는 픽셀)

lbl = tk.Label(text="LABEL")  # 라벨을 만든다
btn= tk.Button(text="PUSH",command=dispLable) # 버튼을 만든다. 함수를 실행 하도록 버튼을 수정

lbl.pack()  # 화면에 라벨을 배치
btn.pack()  # 화면에 버튼을 배치
tk.mainloop() #만든 창 표시
