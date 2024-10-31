import tkinter as tk
import tkinter.filedialog as fd
import tkinter.messagebox as mb
import os
import pygame
from PIL import Image, ImageTk
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
import joblib

# 초기화
pygame.mixer.init()

# 노래 목록을 관리할 리스트
song_list = []

# KNN 모델 생성 또는 불러 오기
try:
    knn_model = joblib.load("knn_genre_model.pkl")  # 기존 모델 로드
except FileNotFoundError:
    knn_model = KNeighborsClassifier(n_neighbors=5)  # 새로운 KNN 모델 생성

# 이미지 파일을 보여 주는 함수
def showImage(filename):
    image = Image.open(filename)
    image = image.resize((300, 300))  # 이미지를 300x300으로 크기 변경

    # 이미지 표시
    dispImage = ImageTk.PhotoImage(image)
    imageLabel.configure(image=dispImage)
    imageLabel.image = dispImage

    # 앨범 커버 이미지에서 장르 예측
    genre = predictGenre(image)
    genreLabel.configure(text=f"예측된 장르: {genre}")

# 파일 대화 상자를 열어 이미지를 선택하고 표시하는 함수
def openImageFile():
    fpath = fd.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.bmp")])
    if fpath:
        showImage(fpath)

# 간단한 색상 기반 장르 예측 함수
def predictGenre(image):
    # 이미지를 numpy 배열로 변환
    image_array = np.array(image)

    # 이미지 평균 색상 계산
    mean_color = np.mean(image_array, axis=(0, 1))

    # 특정 색상 범위에 따라 장르를 예측 (규칙 기반)
    if mean_color[0] > 150 and mean_color[1] > 150:  # 노란색 계열
        return "jazz"
    elif mean_color[0] > 150:  # 빨간색 계열
        return "ballade"
    elif mean_color[2] > 150:  # 파란색 계열
        return "pop"
    elif mean_color[1] > 150:  # 초록색 계열
        return "Rock"
    else:
        return "Classical"  # 고전

# 이미지에서 색상 히스토그램을 추출하는 함수 (RGB 각 채널별 히스토그램)
def extract_color_histogram(image):
    image = image.resize((50, 50))  # 이미지 크기 축소
    image_array = np.array(image)

    # RGB 히스토그램 계산 (각 채널별 히스토그램을 이어 붙임)
    hist_r = np.histogram(image_array[:, :, 0], bins=32, range=(0, 256))[0]
    hist_g = np.histogram(image_array[:, :, 1], bins=32, range=(0, 256))[0]
    hist_b = np.histogram(image_array[:, :, 2], bins=32, range=(0, 256))[0]

    # 각 히스토그램을 하나의 벡터로 결합
    hist = np.concatenate([hist_r, hist_g, hist_b])
    return hist

# 새로운 학습 데이터 추가 및 KNN 모델 재학습
def trainKNNModel():
    # 학습 데이터를 입력 받음
    train_data = []
    train_labels = []

    # 여러 파일 선택 가능
    files = fd.askopenfilenames(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.bmp")])
    if files:
        for file in files:
            image = Image.open(file)
            color_histogram = extract_color_histogram(image)

    if train_data and train_labels:  # 데이터가 존재할 때만 진행
        # 학습 및 테스트 데이터로 분할
        X_train, X_test, y_train, y_test = train_test_split(train_data, train_labels, test_size=0.2, random_state=42)

        # KNN 모델 학습
        global knn_model
        knn_model.fit(X_train, y_train)

        # 학습된 KNN 모델을 파일로 저장
        joblib.dump(knn_model, "knn_genre_model.pkl")
        mb.showinfo("학습 완료", "KNN 모델이 성공적으로 학습되었습니다!")

        # 테스트 데이터로 정확도 출력
        accuracy = knn_model.score(X_test, y_test)
        mb.showinfo("모델 성능", f"KNN 모델의 정확도: {accuracy * 100:.2f}%")

    else:
        mb.showwarning("경고", "학습 데이터가 부족합니다.")

# 노래 파일 추가
def addSongs():
    files = fd.askopenfilenames(filetypes=[("Audio Files", "*.mp3;*.wav")])
    for file in files:
        song_list.append(file)
        songBox.insert(tk.END, os.path.basename(file))

# 노래 재생
def playSong():
    try:
        selected_song = songBox.get(tk.ACTIVE)
        song_index = songBox.curselection()[0]
        song_path = song_list[song_index]

        pygame.mixer.music.load(song_path)
        pygame.mixer.music.play()
        songLabel.configure(text=f"재생 중: {selected_song}")
    except IndexError:
        mb.showwarning("경고", "재생할 노래를 선택하세요.")
    except Exception as e:
        mb.showerror("에러", str(e))

# 앱의 창을 만든다.
root = tk.Tk()
root.geometry("800x800")
root.title("노래 목록 플레이 및 이미지 예측")

# 이미지 파일 열기 버튼
imageBtn = tk.Button(root, text="이미지 파일 열기", command=openImageFile)
imageBtn.pack(pady=10)

# 이미지 표시 레이블
imageLabel = tk.Label()
imageLabel.pack(pady=10)

# 예측된 장르 레이블
genreLabel = tk.Label(root, text="예측된 장르: 없음")
genreLabel.pack(pady=10)

# KNN 모델 학습 버튼 (새 데이터를 추가하여 모델을 학습)
trainBtn = tk.Button(root, text="KNN 모델 학습", command=trainKNNModel)
trainBtn.pack(pady=10)

# 노래 플레이어 관련 UI
songFrame = tk.Frame(root)
songFrame.pack(pady=10)

songBox = tk.Listbox(songFrame, width=50)
songBox.pack(side=tk.LEFT)

songScroll = tk.Scrollbar(songFrame)
songScroll.pack(side=tk.RIGHT, fill=tk.Y)

songBox.config(yscrollcommand=songScroll.set)
songScroll.config(command=songBox.yview)

# 노래 추가 버튼
addSongBtn = tk.Button(root, text="노래 추가", command=addSongs)
addSongBtn.pack(pady=5)

# 노래 재생 버튼
playSongBtn = tk.Button(root, text="노래 재생", command=playSong)
playSongBtn.pack(pady=5)

# 현재 재생 중인 노래 레이블
songLabel = tk.Label(root, text="재생 중: 없음")
songLabel.pack(pady=5)

# tkinter 메인 루프 실행
tk.mainloop()







