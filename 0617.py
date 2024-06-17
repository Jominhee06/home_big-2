import requests
import tkinter as tk
from tkinter import messagebox

def get_exchange_rate():
    base_currency = 'USD'  # 기준 통화 (미국 달러)
    target_currency = 'KRW'  # 대상 통화 (대한민국 원)
    api_url = f"https://api.exchangeratesapi.io/latest?base={base_currency}&symbols={target_currency}"

    # API 요청
    response = requests.get(api_url)

    if response.status_code == 200:
        data = response.json()
        rate = data['rates'][target_currency]
        date = data['date']

        exchange_info = f"오늘의 환율 (기준: {base_currency} → 대상: {target_currency})\n1 {base_currency} = {rate} {target_currency}\n(기준일: {date})"
        messagebox.showinfo("환율 정보", exchange_info)
    else:
        error_message = response.json().get('error', 'Unknown error')
        messagebox.showerror("에러", f"에러 발생: {error_message}")

# GUI 설정
root = tk.Tk()
root.title("환율 정보 앱")

info_label = tk.Label(root, text="미국 달러(USD) → 대한민국 원(KRW) 환율 정보")
info_label.pack()

get_info_button = tk.Button(root, text="환율 정보 가져오기", command=get_exchange_rate)
get_info_button.pack()

root.mainloop()
