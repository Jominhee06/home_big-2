import tkinter as tk
from tkinter import messagebox

class ExpenseTracker:
    def __init__(self, root):
        self.root = root
        self.root.title("가계부 앱")
        self.root.geometry("400x300")

        self.balance = 0


        self.income_label = tk.Label(root, text="수입 입력:")
        self.income_label.pack(pady=10)
        self.income_entry = tk.Entry(root)
        self.income_entry.pack(pady=5)


        self.expense_label = tk.Label(root, text="지출 입력:")
        self.expense_label.pack(pady=10)
        self.expense_entry = tk.Entry(root)
        self.expense_entry.pack(pady=5)


        self.add_button = tk.Button(root, text="추가", command=self.add_entry)
        self.add_button.pack(pady=20)


        self.balance_label = tk.Label(root, text=f"현재 잔액: {self.balance} 원")
        self.balance_label.pack(pady=10)

    def add_entry(self):
        income = self.income_entry.get()
        expense = self.expense_entry.get()

        if income:
            self.balance += float(income)
            self.income_entry.delete(0, tk.END)

        if expense:
            self.balance -= float(expense)
            self.expense_entry.delete(0, tk.END)


        self.balance_label.configure(text=f"현재 잔액: {self.balance} 원")
        messagebox.showinfo("정보", "항목이 추가되었습니다!")


if __name__ == "__main__":
    root = tk.Tk()
    app = ExpenseTracker(root)
    root.mainloop()
