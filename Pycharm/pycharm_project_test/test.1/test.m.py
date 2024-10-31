import os
import tkinter as tk
import tkinter.filedialog as fd
import tkinter.messagebox as mb
import cv2
import librosa
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image, ImageTk
from playsound import playsound

# 색상 설정
themes = {
    "Light": {
        "bg_color": "#f0f0f0",
        "button_bg_color": "#FFDD57",
        "text_color": "#000000",
    },
    "Dark": {
        "bg_color": "#333333",
        "button_bg_color": "#555555",
        "text_color": "#FFFFFF",
    }
}

current_theme = "Light"

# 음악 파일 경로 설정 (장르별)
music_directories = {
    "Jazz": "path/to/your/jazz/music/files",
    "Ballade": "path/to/your/ballade/music/files",
    "Rock": "path/to/your/rock/music/files",
    "Pop": "path/to/your/pop/music/files"
}

# 추천 앨범 및 플레이리스트
album_data = {
    "Jazz": (["Album 1 - Jazz", "Album 2 - Jazz"], ["Playlist 1 - Jazz", "Playlist 2 - Jazz"]),
    "Ballade": (["Album 1 - Ballade", "Album 2 - Ballade"], ["Playlist 1 - Ballade", "Playlist 2 - Ballade"]),
    "Rock": (["Album 1 - Rock", "Album 2 - Rock"], ["Playlist 1 - Rock", "Playlist 2 - Rock"]),
    "Pop": (["Album 1 - Pop", "Album 2 - Pop"], ["Playlist 1 - Pop", "Playlist 2 - Pop"])
}

# 미리 정의된 노래 데이터
preset_songs = {
    "Jazz": [{"title": "fly me to the moon", "artist": "xiao", "lyrics": "Fly me to the moon..."}],
    "Ballade": [
        {"title": "오르트구름", "artist": "윤하", "lyrics": "오르트구름은..."},
        {"title": "오늘따라비가와서그런가봐", "artist": "솔지", "lyrics": "오늘따라 비가..."}
    ],
    "Rock": [{"title": "dream official", "artist": "keshi", "lyrics": "I have a dream..."}],
    "Pop": [{"title": "badguy", "artist": "billie eilish", "lyrics": "I'm the bad guy..."}]
}

# 앨범 커버 이미지 경로
album_cover_paths = {
    "Jazz": "path/to/jazz_cover.jpg",
    "Ballade": "path/to/ballade_cover.jpg",
    "Rock": "path/to/rock_cover.jpg",
    "Pop": "path/to/pop_cover.jpg"
}

# 노래 데이터 저장소
song_data = {
    "Jazz": [],
    "Ballade": [],
    "Rock": [],
    "Pop": []
}

# 비주얼라이저를 위한 데이터
audio_data = None
fs = None  # 샘플링 주파수
volume_level = 1.0  # 기본 볼륨
play_speed = 1.0  # 기본 재생 속도
visualizer_style = "Waveform"  # 기본 비주얼라이저 스타일
repeat_mode = False  # 반복 재생 모드
favorites = []  # 즐겨찾기 리스트


# 테마 변경 함수
def change_theme(theme):
    global current_theme
    current_theme = theme
    colors = themes[theme]

    # 배경색 및 글자색 변경
    root.config(bg=colors["bg_color"])
    for label in [genreLabel, recommendationLabel, playlistLabel]:
        label.config(bg=colors["bg_color"], fg=colors["text_color"])
    for widget in [lyricsText, songsListbox, volumeSlider, speedSlider]:
        widget.config(bg=colors["button_bg_color"], fg=colors["text_color"])


# 버튼 생성 함수
def create_button(text, command):
    return tk.Button(root, text=text, command=command,
                     bg=themes[current_theme]["button_bg_color"],
                     fg=themes[current_theme]["text_color"])


# 이미지 파일을 보여 주는 함수
def showImage(filename):
    image = Image.open(filename)
    image = image.resize((300, 300))

    dispImage = ImageTk.PhotoImage(image)
    imageLabel.config(image=dispImage)
    imageLabel.image = dispImage

    genre = predictGenre(image)
    genreLabel.configure(text=f"예측된 장르: {genre}")
    recommendAlbums(genre)


# 파일 대화 상자를 열어 이미지를 선택하고 표시하는 함수
def openImageFile():
    fpath = fd.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.bmp")])
    if fpath:
        showImage(fpath)


# 장르 예측 함수
def predictGenre(image, threshold=0.5):
    hist = cv2.calcHist([np.array(image)], [0, 1, 2], None, [8, 8, 8], [0, 256, 0, 256, 0, 256])
    hist = cv2.normalize(hist, hist).flatten()

    genre_features = {
        "Jazz": np.array([0.2, 0.3, 0.5]),
        "Ballade": np.array([0.3, 0.3, 0.4]),
        "Rock": np.array([0.5, 0.2, 0.3]),
        "Pop": np.array([0.4, 0.4, 0.2])
    }

    probabilities = {genre: np.sum(hist * feature) for genre, feature in genre_features.items()}

    max_prob = max(probabilities.values())
    if max_prob >= threshold:
        return max(probabilities, key=probabilities.get)
    return "Unknown"


# 장르 기반 앨범 추천 함수
def recommendAlbums(genre):
    recommended_albums, playlists = album_data.get(genre, ([], []))
    if recommended_albums:
        recommendationLabel.configure(text=f"추천 앨범: {', '.join(recommended_albums)}")
        playlistLabel.configure(text=f"재생목록: {', '.join(playlists)}")
        updateSongList(genre)
        addPresetSongs(genre)
        showAlbumCovers(genre)
    else:
        recommendationLabel.configure(text="추천할 앨범이 없습니다.")
        playlistLabel.configure(text="재생목록: 없음")


# 미리 정의된 노래 추가 함수
def addPresetSongs(genre):
    for song in preset_songs.get(genre, []):
        song_data[genre].append(song)
    updateSongList(genre)


# 노래 리스트 업데이트 함수
def updateSongList(genre):
    song_list = song_data.get(genre, [])
    songsListbox.delete(0, tk.END)
    for song in song_list:
        songsListbox.insert(tk.END, f"{song['title']} - {song['artist']}")


# 앨범 커버 이미지 표시 함수
def showAlbumCovers(genre):
    recommended_albums, _ = album_data.get(genre, ([], []))

    if len(recommended_albums) > 0:
        cover_path1 = album_cover_paths.get(recommended_albums[0].split(" - ")[0])
        if cover_path1 and os.path.exists(cover_path1):
            cover_image1 = Image.open(cover_path1)
            cover_image1 = cover_image1.resize((150, 150))
            dispImage1 = ImageTk.PhotoImage(cover_image1)
            albumCoverLabel1.configure(image=dispImage1)
            albumCoverLabel1.image = dispImage1
        else:
            albumCoverLabel1.configure(image=None)

    if len(recommended_albums) > 1:
        cover_path2 = album_cover_paths.get(recommended_albums[1].split(" - ")[0])
        if cover_path2 and os.path.exists(cover_path2):
            cover_image2 = Image.open(cover_path2)
            cover_image2 = cover_image2.resize((150, 150))
            dispImage2 = ImageTk.PhotoImage(cover_image2)
            albumCoverLabel2.configure(image=dispImage2)
            albumCoverLabel2.image = dispImage2
        else:
            albumCoverLabel2.configure(image=None)
    else:
        albumCoverLabel2.configure(image=None)


# 선택된 노래 재생 함수
def playSelectedSong():
    selected_song_index = songsListbox.curselection()
    if not selected_song_index:
        mb.showwarning("경고", "노래를 선택해주세요.")
        return

    selected_song = song_data[selected_genre][selected_song_index[0]]
    play_and_visualize(selected_song['title'], selected_song['artist'])


# 플레이리스트 실행 함수
def play_and_visualize(title, artist):
    global audio_data, fs, volume_level, play_speed
    try:
        song_path = os.path.join(music_directories[artist], f"{title}.mp3")
        if not os.path.exists(song_path):
            raise FileNotFoundError(f"{title} 파일이 없습니다.")

        while True:
            playsound(song_path)

            # 오디오 데이터 로딩
            audio_data, fs = librosa.load(song_path, sr=None)
            display_visualizer(audio_data, fs)

            if not repeat_mode:
                break

    except Exception as e:
        mb.showerror("오류", str(e))


# 비주얼라이저 표시 함수
def display_visualizer(audio_data, fs):
    plt.figure(figsize=(10, 4))
    if visualizer_style == "Waveform":
        plt.plot(audio_data)
        plt.title("Waveform")
    elif visualizer_style == "Spectrogram":
        plt.specgram(audio_data, Fs=fs)
        plt.title("Spectrogram")
    else:
        # FFT
        N = len(audio_data)
        fft_data = np.fft.fft(audio_data)
        freqs = np.fft.fftfreq(N, 1 / fs)
        plt.plot(freqs, np.abs(fft_data))
        plt.title("FFT")

    plt.xlabel("시간 (s)")
    plt.ylabel("진폭")
    plt.show()


# 반복 재생 모드 토글
def toggleRepeatMode():
    global repeat_mode
    repeat_mode = not repeat_mode
    repeatButton.config(text="반복 재생 해제" if repeat_mode else "반복 재생")


# 즐겨찾기 추가 함수
def toggleFavorite():
    selected_song_index = songsListbox.curselection()
    if not selected_song_index:
        mb.showwarning("경고", "노래를 선택해주세요.")
        return

    selected_song = song_data[selected_genre][selected_song_index[0]]
    if selected_song not in favorites:
        favorites.append(selected_song)
        favoriteButton.config(text="즐겨찾기 해제")
        mb.showinfo("정보", f"{selected_song['title']} - {selected_song['artist']}이(가) 즐겨찾기에 추가되었습니다.")
    else:
        favorites.remove(selected_song)
        favoriteButton.config(text="즐겨찾기 추가")
        mb.showinfo("정보", f"{selected_song['title']} - {selected_song['artist']}이(가) 즐겨찾기에서 제거되었습니다.")


# 볼륨 조절 함수
def adjustVolume(value):
    global volume_level
    volume_level = float(value)
    # 볼륨 조절 로직 추가


# 재생 속도 조절 함수
def adjustSpeed(value):
    global play_speed
    play_speed = float(value)
    # 재생 속도 조절 로직 추가


# UI 초기화 및 설정
root = tk.Tk()
root.title("스마트 음악 플레이어")
root.geometry("800x600")

# 장르 선택 UI
genreLabel = tk.Label(root, text="장르 선택:", bg=themes[current_theme]["bg_color"], fg=themes[current_theme]["text_color"])
genreLabel.pack(pady=10)

# 버튼 생성
buttons = [
    ("이미지 열기", openImageFile),
    ("선택된 노래 재생", playSelectedSong),
    ("반복 재생", toggleRepeatMode),
    ("즐겨찾기 추가", toggleFavorite),
    ("검색", None)  # 검색 기능을 나중에 구현
]

for text, command in buttons:
    button = create_button(text, command)
    button.pack(pady=5)

# 볼륨 조절 슬라이더
volumeSlider = tk.Scale(root, from_=0, to=1, resolution=0.1, label="볼륨", orient=tk.HORIZONTAL, command=adjustVolume)
volumeSlider.set(volume_level)
volumeSlider.pack(pady=10)

# 재생 속도 조절 슬라이더
speedSlider = tk.Scale(root, from_=0.5, to=2.0, resolution=0.1, label="재생 속도", orient=tk.HORIZONTAL,
                       command=adjustSpeed)
speedSlider.set(play_speed)
speedSlider.pack(pady=10)

# 비주얼라이저 스타일 버튼
visualizer_styles = ["파형 비주얼라이저", "스펙트로그램 비주얼라이저", "FFT 비주얼라이저"]
for style in visualizer_styles:
    button = create_button(style, lambda s=style: setVisualizerStyle(s))
    button.pack(pady=5)

# 노래 목록 표시
songsListbox = tk.Listbox(root, width=50, height=10)
songsListbox.pack(pady=10)

# 앨범 커버 이미지 표시
albumCoverLabel1 = tk.Label(root)
albumCoverLabel1.pack(pady=5)

albumCoverLabel2 = tk.Label(root)
albumCoverLabel2.pack(pady=5)

# 이미지 표시
imageLabel = tk.Label(root)
imageLabel.pack(pady=10)

# 예측된 장르 및 추천 결과 표시
recommendationLabel = tk.Label(root, text="추천 앨범:", bg=themes[current_theme]["bg_color"],
                               fg=themes[current_theme]["text_color"])
recommendationLabel.pack(pady=10)

playlistLabel = tk.Label(root, text="재생목록:", bg=themes[current_theme]["bg_color"],
                         fg=themes[current_theme]["text_color"])
playlistLabel.pack(pady=10)

# 테마 변경 버튼
theme_buttons = [("라이트 테마", "Light"), ("다크 테마", "Dark")]
for text, theme in theme_buttons:
    button = create_button(text, lambda t=theme: change_theme(t))
    button.pack(pady=5)

root.mainloop()