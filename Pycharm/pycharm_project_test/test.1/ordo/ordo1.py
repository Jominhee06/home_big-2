import tkinter as tk
import random


def dispLabel(): # 함수를 추가 한다
    list_unse=["대길","중길","소길","흉"]
    lbl.configure(text=random.choice(list_unse))

root=tk.Tk()  # 화면을 만든다.
root.geometry("200x100")   # 화면의 크기를 정한다(단위는 픽셀)

lbl=tk.Label(text="LABEL")  # 라벨을 만든다.
btn=tk.Button(text="PUSH", command=dispLabel)  # 버튼을 만든다.

lbl.pack()  # 화면에 라벨을 배치 한다.
btn.pack()  # 화면에 버튼을 배치 한다.
tk.mainloop()  # 만든 창을 표시 한다.