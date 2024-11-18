import sys
import tkinter as tk
from tkinter import messagebox

def check_serial_key():
    correct_key = "111"

    def validate_key():
        user_input = entry.get()
        if user_input == correct_key:
            root.destroy()
            success_screen()
        else:
            messagebox.showerror("Результат", "Неправильний ключ. Доступ заборонено.")

    def success_screen():
        success_root = tk.Tk()
        success_root.title("Успіх")
        success_root.geometry("300x50")
        tk.Label(success_root, text="Ключ правильний. Доступ надано.").pack(pady=10)
        tk.Button(success_root, text="Закрити", command=success_root.destroy).pack(pady=5)
        success_root.mainloop()

    root = tk.Tk()
    root.title("Перевірка серійного ключа")
    root.geometry("300x150")

    tk.Label(root, text="Введіть серійний ключ:").pack(pady=10)
    entry = tk.Entry(root)
    entry.pack(pady=5)

    tk.Button(root, text="Перевірити", command=validate_key).pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    check_serial_key()