import tkinter as tk
import tkinter.filedialog as fd
import PIL.Image
import PIL.ImageTk
import numpy as np
from sklearn.svm import SVC
import joblib

# 이미지 파일을 수치 리스트로 변환
def imageToData(filename):
    # 이미지를 흑백으로 변환하고 크기를 조정
    realimage = PIL.Image.open(filename)
    grayImage = realimage.convert("L")
    grayImage = grayImage.resize((200, 200))  # 모델 입력 크기에 맞게 조정

    # 원본 이미지 표시
    dispRealImage = PIL.ImageTk.PhotoImage(realimage.resize((300, 300)))
    originalImageLabel.configure(image=dispRealImage)
    originalImageLabel.image = dispRealImage

    # 예측 이미지 표시
    dispGrayImage = PIL.ImageTk.PhotoImage(grayImage.resize((300, 300)))
    imageLabel.configure(image=dispGrayImage)
    imageLabel.image = dispGrayImage

    # 수치 리스트로 변환
    numImage = np.asarray(grayImage, dtype=float).flatten() / 255.0  # 정규화
    return numImage

# 코로나 진단 예측 함수
def predictCovid(data):
    clf = joblib.load('covid_test_model.pkl')  # 미리 학습된 모델 불러오기
    prediction = clf.predict([data])
    result = "양성" if prediction[0] == 1 else "음성"
    textLabel.configure(text="예측 결과: " + result)

# 파일 대화 상자를 열어 이미지 선택
def openFile():
    fpath = fd.askopenfilename()
    if fpath:
        data = imageToData(fpath)
        predictCovid(data)

# 앱의 창을 만든다.
root = tk.Tk()
root.geometry("600x500")

# 버튼 추가
btn = tk.Button(root, text="파일 열기", command=openFile)
btn.pack(pady=10)

# 가로 정렬을 위한 프레임 추가
frame = tk.Frame(root)
frame.pack()

# 원본 이미지 라벨
originalImageLabel = tk.Label(frame)
originalImageLabel.grid(row=0, column=0)

# 전처리 후 이미지 라벨
imageLabel = tk.Label(frame)
imageLabel.grid(row=0, column=1)

# 예측 결과를 표시하는 라벨
textLabel = tk.Label(root, text="코로나 진단 키트를 이미지를 예측합니다.")
textLabel.pack(pady=10)

# 앱 실행
root.mainloop()


