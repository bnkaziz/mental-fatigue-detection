import tkinter as tk
from tkinter import ttk

class SubjectInformationApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Информация об испытуемом")
        self.geometry("600x400")
        self.configure(bg="#f0f0f0")

        # Title Label
        title_label = ttk.Label(self, text="Информация об испытуемом", font=("Helvetica", 20, "bold"))
        title_label.pack(pady=20)

        # Name/ID Entry
        name_label = ttk.Label(self, text="Имя/ID:", font=("Helvetica", 14))
        name_label.pack(pady=5)
        name_entry = ttk.Entry(self, font=("Helvetica", 12), width=40)
        name_entry.pack(pady=5)

        # Age Entry
        age_label = ttk.Label(self, text="Возраст:", font=("Helvetica", 14))
        age_label.pack(pady=5)
        age_entry = ttk.Entry(self, font=("Helvetica", 12), width=40)
        age_entry.pack(pady=5)

        # Gender Drop-Down
        gender_label = ttk.Label(self, text="Пол:", font=("Helvetica", 14))
        gender_label.pack(pady=5)
        gender_combo = ttk.Combobox(self, font=("Helvetica", 12), state="readonly", width=38)
        gender_combo['values'] = ("Мужчина", "Женщина")
        gender_combo.pack(pady=5)

        # Experiment Type Drop-Down
        experiment_type_label = ttk.Label(self, text="Тип эксперимента:", font=("Helvetica", 14))
        experiment_type_label.pack(pady=5)
        experiment_type_combo = ttk.Combobox(self, font=("Helvetica", 12), state="readonly", width=38)
        experiment_type_combo['values'] = ("Покой", "Напряжение", "Испытание на утомление")
        experiment_type_combo.pack(pady=5)

        # Notes (Multiline Text)
        notes_label = ttk.Label(self, text="Примечания:", font=("Helvetica", 14))
        notes_label.pack(pady=5)
        notes_text = tk.Text(self, font=("Helvetica", 12), height=5, width=40)
        notes_text.pack(pady=5)

        # Save and Continue Button
        save_button = ttk.Button(self, text="Сохранить и продолжить", width=20)
        save_button.pack(pady=20)

if __name__ == "__main__":
    app = SubjectInformationApp()
    app.mainloop()
