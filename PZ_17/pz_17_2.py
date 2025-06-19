import tkinter as tk
from tkinter import messagebox

def process_input():
    num = entry.get()
    while True:
        try:
            num = int(num)
            if 99 < num < 1000:   # проверка на 3-х значное число
                sot = num // 100
                des = (num // 10) % 10
                ed = num % 10
                summ = sot + des + ed
                pr = sot * des * ed
                result_label.config(
                    text=f"{sot}, {des}, {ed}\nСумма чисел: {summ}\nПроизведение чисел: {pr}"
                )
            else:
                messagebox.showwarning("Предупреждение", "Число не трёхзначное.")
            break
        except ValueError:
            messagebox.showerror("Ошибка", "Вы ввели не число.")
            break

root = tk.Tk()
root.title("Обработка трёхзначного числа")
root.geometry("400x300")

tk.Label(root, text="Введите трёхзначное число:").pack(pady=5)
entry = tk.Entry(root)
entry.pack(pady=5)

tk.Button(root, text="Рассчитать", command=process_input).pack(pady=5)

result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack(pady=10)

root.mainloop()