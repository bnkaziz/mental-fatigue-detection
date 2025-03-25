import tkinter as tk
from tkinter import ttk

class FatigueDetectionApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Приложение для определения утомления")
        self.geometry("800x600")
        self.configure(bg="#f0f0f0")

        # Title Label
        title_label = ttk.Label(self, text="Приложение для определения утомления", font=("Helvetica", 24, "bold"))
        title_label.pack(pady=50)

        # Button Frame
        button_frame = ttk.Frame(self)
        button_frame.pack(pady=20)

        # Buttons
        new_experiment_button = ttk.Button(button_frame, text="Новый эксперимент")
        new_experiment_button.pack(pady=10, fill=tk.X)

        load_experiment_button = ttk.Button(button_frame, text="Загрузить эксперимент")
        load_experiment_button.pack(pady=10, fill=tk.X)

        settings_button = ttk.Button(button_frame, text="Настройки")
        settings_button.pack(pady=10, fill=tk.X)

        help_button = ttk.Button(button_frame, text="Справка")
        help_button.pack(pady=10, fill=tk.X)

        # Footer Label
        footer_label = ttk.Label(self, text="Версия 1.0 | Разработана Бенхалди", font=("Helvetica", 10))
        footer_label.pack(side=tk.BOTTOM, pady=20)

if __name__ == "__main__":
    app = FatigueDetectionApp()
    app.mainloop()
