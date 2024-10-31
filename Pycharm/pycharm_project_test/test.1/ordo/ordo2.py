import tkinter as tk  # 창을 표시하는 모듈
import tkinter.filedialog as fd  # 파일 대화 상자를 사용하는 모듈
import PIL.Image  # 이미지를 다루는 모듈
import PIL.ImageTk  # tkinter로 만든 화면 상에 이미지를 표시하는 모듈

def dispPhoto(path):  # 이미지 파일을 표시하는 함수
    newImage = PIL.Image.open(path).resize((300, 300))  # 이미지를 읽어 들인다.
    # 해당 이미지를 라벨에 표시
    imageData = PIL.ImageTk.PhotoImage(newImage)
    imageLabel.configure(image=imageData)
    imageLabel.image = imageData

def openFile():  # 파일 대화 상자를 열기 위한 함수
    fpath = fd.askopenfilename()  # 파일 대화 상자를 열고, 선택한 파일명을 가져온다.
    if fpath:  # 만약 파일명이 있으면
        dispPhoto(fpath)  # 해당 파일명으로 함수를 호출한다.

# 메인 프로그램 시작
root = tk.Tk()
root.geometry("400x350")

btn = tk.Button(root, text="파일 열기", command=openFile)  # 버튼을 만들고 함수를 설정
imageLabel = tk.Label(root)  # 화면 표시용 라벨을 만든다.
btn.pack()  # 화면에 버튼을 배치
imageLabel.pack()  # 화면에 라벨을 배치
root.mainloop()  # 만든 창을 표시

