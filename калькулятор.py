import tkinter as tk
from tkinter import ttk
from  tkinter import messagebox
import logging

# Настройка логирования
logging.basicConfig(
    filename="калькулятор_лог.txt",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Функция для обработки кнопок
def calculate(операция):
    try:
        число1 = float(entry1.get())
        число2 = float(entry2.get())

        if операция == "+":
            результат = число1 + число2
        elif операция == "-":
            результат = число1 - число2
        elif операция == "*":
            результат = число1 * число2
        elif операция =="/":
            if число2 == 0:
                результат ="Ошибка: деление на ноль!"
                logging.error("Попытка деления на ноль")
            else:
                результат = число1 / число2
        else:
            результат = "Неизвестная операция"

        result_label.config(text=f"Результат: {результат}")
        logging.info(f"Выполнено: {число1} {операция} {число2} = {результат}")

    except ValueError:
        messagebox.showerror("Ошибка", "Введите корректные числа!")
        logging.error("Некорректный ввод: не числовое значение")

 # Создаем окно
root = tk.Tk()
root.title("Калькулятор")
root.geometry("300x400")
root.configure(bg="#f0f0f0")

 # Добавляем иконку
try:
    root.iconbitmap("калькулятор.ico")
except tk.TclError as e:
    print("Ошибка загрузки иконки:", e)

 # Цветовая палитра
BG_COLOR = "#f0f0f0" # Светло-серый фон
BTN_COLOR = "#4CAF50" # Зеленые кнопки
BTN_HOVER_COLOR = "#45a049" #Темнее при наведении
TEXT_COLOR = "#ffffff" # Белый текст
ENTRY_COLOR = "#ffffff" # Белый фон полей ввода

 # Поля ввода
entry1 = tk.Entry(root, font=("Arial", 14), bg=ENTRY_COLOR, justify="center")
entry2 = tk.Entry(root, font=("Arial", 14), bg=ENTRY_COLOR, justify="center")

 # Кнопки
style = ttk.Style()
style.configure("TButton", font=("Arial", 14), padding=10, relief="flat", backgroung=BTN_COLOR)
style.map("TButton", backgrounf=[("active", BTN_HOVER_COLOR)])

btn_add = ttk.Button(root, text="+", command=lambda: calculate("+"))
btn_sub = ttk.Button(root, text="-", command=lambda: calculate("-"))
btn_mul = ttk.Button(root, text="*", command=lambda: calculate("*"))
btn_div = ttk.Button(root, text="/", command=lambda: calculate("/"))

 # Метка для результата
result_label = tk.Label(root, text="Результат: ", font=("Arial", 14), bg=BG_COLOR, fg="#333333")

 # Расположение элементов
entry1.pack(pady=10, padx=20, ipady=5)
entry2.pack(pady=10, padx=20, ipady=5)
btn_add.pack(pady=5)
btn_sub.pack(pady=5)
btn_mul.pack(pady=5)
btn_div.pack(pady=5)
result_label.pack(pady=15)

 # Запуст окна
root.mainloop()
