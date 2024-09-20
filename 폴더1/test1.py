import tkinter as tk
from tkinter import messagebox

# 퀴즈 질문과 답변 데이터
questions = [
    {
        "question": "파이썬의 창시자는 누구인가요?",
        "options": ["Guido van Rossum", "Elon Musk", "Bill Gates", "Mark Zuckerberg"],
        "answer": "Guido van Rossum"
    },
    {
        "question": "파이썬의 주요 용도는 무엇인가요?",
        "options": ["웹 개발", "데이터 분석", "인공지능", "모두 포함"],
        "answer": "모두 포함"
    },
    {
        "question": "파이썬의 확장자는 무엇인가요?",
        "options": [".py", ".java", ".cpp", ".html"],
        "answer": ".py"
    }
]


# 퀴즈 앱 클래스
class QuizApp:
    def __init__(self, master):
        self.master = master
        self.master.title("퀴즈 앱")
        self.score = 0
        self.question_index = 0

        self.question_label = tk.Label(master, text="", wraplength=400)
        self.question_label.pack(pady=20)

        self.options_var = tk.StringVar(value="")
        self.options_frame = tk.Frame(master)
        self.options_frame.pack()

        self.option_buttons = []
        for i in range(4):
            btn = tk.Radiobutton(self.options_frame, text="", variable=self.options_var, value="")
            btn.pack(anchor="w")
            self.option_buttons.append(btn)

        self.submit_button = tk.Button(master, text="제출", command=self.submit_answer)
        self.submit_button.pack(pady=10)

        self.next_button = tk.Button(master, text="다음 질문", command=self.next_question)
        self.next_button.pack(pady=10)
        self.next_button.config(state=tk.DISABLED)

        self.show_question()

    def show_question(self):
        question = questions[self.question_index]
        self.question_label.config(text=question["question"])
        for i, option in enumerate(question["options"]):
            self.option_buttons[i].config(text=option, value=option)
        self.options_var.set("")

    def submit_answer(self):
        selected_option = self.options_var.get()
        if selected_option == questions[self.question_index]["answer"]:
            self.score += 1
            messagebox.showinfo("정답!", "정답입니다!")
        else:
            messagebox.showinfo("오답", f"틀렸습니다! 정답은 '{questions[self.question_index]['answer']}'입니다.")

        self.submit_button.config(state=tk.DISABLED)
        self.next_button.config(state=tk.NORMAL)

    def next_question(self):
        self.question_index += 1
        if self.question_index < len(questions):
            self.show_question()
            self.submit_button.config(state=tk.NORMAL)
            self.next_button.config(state=tk.DISABLED)
        else:
            messagebox.showinfo("퀴즈 종료", f"퀴즈가 종료되었습니다! 점수: {self.score}/{len(questions)}")
            self.master.quit()


# 앱 실행
if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
    root.geometry("500x300")
    root.mainloop()
