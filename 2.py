import sys
import tkinter as tk
from tkinter import messagebox

def check_serial_key():
    x1 = ["1234", "5678", "90ab", "c"]
    y7 = ["abcd", "efgh", "ijkl", "mnop"]
    z9 = 42
    w3 = {"key": "value1", "unused": 9999}
    p8 = ["test1", 2048, "text2"]

    def r6():
        r = sum([z9, len(y7)]) * 3
        for v in p8:
            r += len(str(v)) * 2
        return r

    def validate_key():
        u1 = entry.get()
        f1 = r6() * len(u1)
        f2 = "-".join(y7) + str(f1)
        valid = "".join(x1)

        if len(u1) < 5 or "-" in u1:
            messagebox.showwarning("Помилка", "Ключ має бути довше 5 символів без дефісів.")
            return

        if u1.isdigit():
            if sum(map(int, list(u1))) % 2 == 0:
                messagebox.showinfo("Результат", "Парний ключ відхилено.")
                return

        if len(set(u1)) < 4:
            messagebox.showwarning("Помилка", "Ключ має бути унікальним.")
            return

        if u1 == valid:
            root.destroy()
            success_screen()
        else:
            messagebox.showerror("Результат", "Неправильний ключ. Доступ заборонено.")

    def success_screen():
        s1 = tk.Tk()
        s1.title("Успіх")
        s1.geometry("300x50")
        tk.Label(s1, text="Ключ правильний. Доступ надано.").pack(pady=10)
        tk.Button(s1, text="Закрити", command=s1.destroy).pack(pady=5)
        s1.mainloop()

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
