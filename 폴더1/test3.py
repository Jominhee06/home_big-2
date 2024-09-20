import tkinter as tk
from tkinter import ttk
from sklearn import datasets
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

class IrisVisualizerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("붓꽃 데이터 시각화기")
        self.root.geometry("300x200")

        # 붓꽃 데이터셋 로드
        self.iris = datasets.load_iris()
        self.data = pd.DataFrame(data=self.iris.data, columns=self.iris.feature_names)
        self.data['species'] = self.iris.target

        # 특성 선택을 위한 드롭다운 메뉴
        self.feature_x = ttk.Combobox(root, values=self.iris.feature_names)
        self.feature_x.set("X축 특성 선택")
        self.feature_x.pack(pady=10)

        self.feature_y = ttk.Combobox(root, values=self.iris.feature_names)
        self.feature_y.set("Y축 특성 선택")
        self.feature_y.pack(pady=10)

        # 시각화 버튼
        self.button_plot = tk.Button(root, text="시각화하기", command=self.plot_data)
        self.button_plot.pack(pady=10)

    def plot_data(self):
        x = self.feature_x.get()
        y = self.feature_y.get()

        if x in self.iris.feature_names and y in self.iris.feature_names:
            plt.figure(figsize=(8, 6))
            sns.scatterplot(data=self.data, x=x, y=y, hue='species', palette='viridis')
            plt.title(f"{x} vs {y} 시각화")
            plt.xlabel(x)
            plt.ylabel(y)
            plt.legend(title='Species', loc='upper left', labels=self.iris.target_names)
            plt.show()
        else:
            tk.messagebox.showerror("오류", "올바른 특성을 선택하세요.")

# 앱 실행
if __name__ == "__main__":
    root = tk.Tk()
    app = IrisVisualizerApp(root)
    root.mainloop()


