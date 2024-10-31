import tkinter as tk
import tkinter.filedialog as fd
import PIL.Image
import PIL.ImageTk
import pytesseract
import sklearn.datasets
import sklearn.svm
import numpy
from PIL import ImageFilter

# 이미지 파일을 수치 리스트로 변환
def imageToData(filename):
    realimage = PIL.Image.open(filename)

    # 원본 이미지를 그레이스케일로 변환하고 회전
    grayImage = realimage.convert("L").rotate(180)

    # 필터 적용
    grayImage = grayImage.filter(ImageFilter.EDGE_ENHANCE)

    # 이미지를 8x8로 리사이즈
    grayImage = grayImage.resize((8, 8))

    # 원본 이미지 표시
    dispRealImage = PIL.ImageTk.PhotoImage(realimage.resize((200, 200)))
    originalImageLabel.configure(image=dispRealImage)
    originalImageLabel.image = dispRealImage

    # 예측 이미지 표시
    dispGrayImage = PIL.ImageTk.PhotoImage(grayImage.resize((200, 200)))
    imageLabel.configure(image=dispGrayImage)
    imageLabel.image = dispGrayImage

    # 수치 리스트로 변환
    numImage = numpy.asarray(grayImage, dtype=float)
    numImage = numpy.floor(16 - 16 * (numImage / 256))  # 색농담을 255~0을 0~16으로 변환
    numImage = numImage.flatten()
    return numImage, dispRealImage, dispGrayImage  # 두 이미지를 반환

# 숫자를 예측 한다.
def predictDigits(data):
    digits = sklearn.datasets.load_digits()
    clf = sklearn.svm.SVC(gamma=0.001)
    clf.fit(digits.data, digits.target)
    n = clf.predict([data])
    textLabel.configure(text="이 그림은 " + str(n[0]) + "입니다.")

# 이미지에서 텍스트를 추출한다
def extractText(image):
    text = pytesseract.image_to_string(image, lang='eng')
    return text.strip()

# 파일 대화 상자를 연다
def openFile():
    fpath = fd.askopenfilename()
    if fpath:
        data, dispRealImage, dispGrayImage = imageToData(fpath)
        predictDigits(data)

        # 원본 이미지에서 텍스트 추출
        originalText = extractText(PIL.Image.open(fpath))
        originalTextLabel.configure(text="원본 텍스트: " + originalText)

        # 전처리 이미지에서 텍스트 추출
        processed_image = PIL.Image.open(fpath).convert("L").rotate(180).filter(ImageFilter.EDGE_ENHANCE).resize((8, 8))
        grayText = extractText(processed_image)
        grayTextLabel.configure(text="전처리 텍스트: " + grayText)

        # 네 가지 이미지 표시 업데이트
        originalImageDisp.configure(image=dispRealImage)
        originalImageDisp.image = dispRealImage

        processedImageDisp.configure(image=dispGrayImage)
        processedImageDisp.image = dispGrayImage

# 앱의 창을 만든다.
root = tk.Tk()
root.geometry("600x600")  # 창 크기 조정

# 버튼 추가
btn = tk.Button(root, text="파일 열기", command=openFile)
btn.pack()

# 가로 정렬을 위한 프레임 추가
frame = tk.Frame(root)
frame.pack()

# 원본 이미지 라벨
originalImageLabel = tk.Label(frame)
originalImageLabel.grid(row=0, column=0)

# 원본 이미지 아래 텍스트
originalTextLabel = tk.Label(frame, text="전처리 전")
originalTextLabel.grid(row=1, column=0)

# 전처리 후 이미지 라벨
imageLabel = tk.Label(frame)
imageLabel.grid(row=0, column=1)

# 전처리 후 이미지 아래 텍스트
grayTextLabel = tk.Label(frame, text="전처리 후")
grayTextLabel.grid(row=1, column=1)

# 예측 결과를 표시하는 라벨
textLabel = tk.Label(root, text="손글씨 숫자를 인식합니다.")
textLabel.pack()

# 네 가지 이미지 라벨 추가
fourImagesFrame = tk.Frame(root)
fourImagesFrame.pack(pady=10)

# 네 개의 이미지를 표시할 라벨
image1Label = tk.Label(fourImagesFrame, text="원본 이미지")
image1Label.grid(row=0, column=0)

image2Label = tk.Label(fourImagesFrame, text="전처리 이미지")
image2Label.grid(row=0, column=1)

# 이미지를 표시할 라벨 (원본 이미지와 전처리 된 이미지를 여기에 추가)
originalImageDisp = tk.Label(fourImagesFrame)
originalImageDisp.grid(row=1, column=0)

processedImageDisp = tk.Label(fourImagesFrame)
processedImageDisp.grid(row=1, column=1)

tk.mainloop()



