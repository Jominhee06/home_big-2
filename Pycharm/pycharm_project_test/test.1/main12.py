import tkinter as tk
import tkinter.filedialog as fd
import PIL.Image
import PIL.ImageTk
import sklearn.datasets
import sklearn.svm
import numpy

# 이미지 파일을 수치 리스트로 변환
def imageToData(filename):
    # 이미지를 8*8의 그레이스케일로 변환
    realimage = PIL.Image.open(filename)
    grayImage = realimage.convert("L")
    grayImage = grayImage.resize((8, 8))

    # 원본 이미지 표시
    dispRealImage = PIL.ImageTk.PhotoImage(realimage.resize((200, 200)))
    originalImageLabel.configure(image=dispRealImage)
    originalImageLabel.image = dispRealImage

    # 예측 이미지 표시
    dispGrayImage = PIL.ImageTk.PhotoImage(grayImage.resize((200, 200)))
    imageLabel.configure(image=dispGrayImage)
    imageLabel.image = dispGrayImage

    # 두 번째 예측 이미지 (모든 픽셀을 반전)
    invertedImage = PIL.Image.eval(grayImage, lambda x: 255 - x)
    dispInvertedImage = PIL.ImageTk.PhotoImage(invertedImage.resize((200, 200)))
    invertedImageLabel.configure(image=dispInvertedImage)
    invertedImageLabel.image = dispInvertedImage

    # 수치 리스트로 변환
    numImage = numpy.asarray(grayImage, dtype=float)
    numImage = numpy.floor(16 - 16 * (numImage / 256))  # 색농담을 255~0을 0~16으로 변환
    numImage = numImage.flatten()
    return numImage

# 숫자를 예측 한다.
def predictDigits(data):
    # 학습용 데이터를 읽어 들인다.
    digits = sklearn.datasets.load_digits()
    # 머신 러닝을 한다.
    clf = sklearn.svm.SVC(gamma=0.001)
    clf.fit(digits.data, digits.target)
    # 예측 하고 결과를 표시 한다.
    n = clf.predict([data])
    textLabel.configure(text="이 그림은 " + str(n[0]) + "입니다.")

# 파일 대화 상자를 연다
def openFile():
    fpath = fd.askopenfilename()
    if fpath:
        data = imageToData(fpath)
        predictDigits(data)

# 앱의 창을 만든다.
root = tk.Tk()
root.geometry("700x600")

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

# 반전 이미지 라벨
invertedImageLabel = tk.Label(frame)
invertedImageLabel.grid(row=0, column=2)

# 예측 결과를 표시 하는 라벨
textLabel = tk.Label(root, text="손글씨 숫자를 인식합니다.")
textLabel.pack(pady=10)

# 앱 실행
tk.mainloop()
