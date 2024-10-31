import tkinter as tk
import tkinter.filedialog as fd
import tkinter.messagebox as mb
import os
import pygame
from PIL import Image, ImageTk
import numpy as np

# 초기화
pygame.mixer.init()

# 노래 목록을 관리할 리스트
song_list = []

# 이미지 파일을 보여 주는 함수
def showImage(filename):
    image = Image.open(filename)
    image = image.resize((300, 300))  # 이미지를 300x300으로 크기 변경

    # 이미지 표시
    dispImage = ImageTk.PhotoImage(image)
    imageLabel.configure(image=dispImage)
    imageLabel.image = dispImage

    # 앨범 커버 이미지 에서 장르 예측
    genre = predictGenre(image)
    genreLabel.configure(text=f"예측된 장르: {genre}")

# 파일 대화 상자를 열어 이미지를 선택 하고 표시 하는 함수
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
        mb.showwarning("경고", "재생할 노래를 선택 하세요.")
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