import tkinter as tk
from tkinter import messagebox, simpledialog
from tkinter import PhotoImage
import pygame
import os

# 노래 목록과 이미지 목록을 저장할 리스트
song_list = []
image_list = []

# 노래 추가 함수
def add_song():
    song_name = simpledialog.askstring("노래 추가", "노래 제목을 입력하세요:")
    if song_name:
        image_name = simpledialog.askstring("이미지 추가", "이미지 파일 경로를 입력하세요:")
        if os.path.exists(image_name):  # 이미지 파일이 존재하는지 확인
            song_list.append(song_name)
            image_list.append(image_name)
            update_song_listbox()
        else:
            messagebox.showerror("오류", "유효한 이미지 파일 경로를 입력하세요.")

# 노래 목록 업데이트 함수
def update_song_listbox():
    song_listbox.delete(0, tk.END)  # 기존 목록 지우기
    for song in song_list:
        song_listbox.insert(tk.END, song)  # 새로운 목록 추가
    if song_list:  # 노래가 있는 경우 첫 번째 노래의 이미지를 표시
        display_image(0)

# 노래 이미지 표시 함수
def display_image(index):
    if index < len(image_list):
        img_path = image_list[index]
        try:
            img = PhotoImage(file=img_path)
            image_label.config(image=img)
            image_label.image = img  # 이미지 객체 유지
        except Exception as e:
            messagebox.showerror("오류", f"이미지를 표시할 수 없습니다: {e}")

# 노래 재생 함수
def play_song():
    selected_song_index = song_listbox.curselection()
    if selected_song_index:
        song_name = song_list[selected_song_index[0]]
        try:
            pygame.mixer.init()  # pygame 믹서 초기화
            pygame.mixer.music.load(song_name)  # 노래 로드
            pygame.mixer.music.play()  # 노래 재생
            display_image(selected_song_index[0])  # 선택한 노래의 이미지 표시
        except Exception as e:
            messagebox.showerror("오류", f"노래를 재생할 수 없습니다: {e}")
    else:
        messagebox.showwarning("경고", "재생할 노래를 선택하세요.")

# 앱 초기화
root = tk.Tk()
root.title("노래 목록 플레이어")

# 버튼 추가
add_song_button = tk.Button(root, text="노래 추가", command=add_song)
add_song_button.pack(pady=10)

play_song_button = tk.Button(root, text="재생", command=play_song)
play_song_button.pack(pady=10)

# 노래 목록 박스 추가
song_listbox = tk.Listbox(root, width=50)
song_listbox.pack(pady=10)

# 이미지 표시 레이블 추가
image_label = tk.Label(root)
image_label.pack(pady=10)

# 앱 실행
root.geometry("400x400")
root.mainloop()


