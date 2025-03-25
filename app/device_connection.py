import tkinter as tk
from tkinter import ttk

class DeviceConnectionApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Подключение устройства")
        self.geometry("600x400")
        self.configure(bg="#f0f0f0")

        # Title Label
        title_label = ttk.Label(self, text="Подключение устройства", font=("Helvetica", 20, "bold"))
        title_label.pack(pady=20)

        # Device Selection Drop-Down
        device_label = ttk.Label(self, text="Выберите устройство:", font=("Helvetica", 14))
        device_label.pack(pady=5)
        self.device_combo = ttk.Combobox(self, font=("Helvetica", 12), state="readonly", width=38)
        self.device_combo['values'] = ("BioRadio")
        self.device_combo.pack(pady=5)

        # Connection Status Indicator
        self.status_label = ttk.Label(self, text="Статус: Отключен", font=("Helvetica", 14), foreground="red")
        self.status_label.pack(pady=10)

        # Connect Button
        connect_button = ttk.Button(self, text="Подключить", width=20, command=self.connect_device)
        connect_button.pack(pady=20)

        # Next Button (Initially Disabled)
        self.next_button = ttk.Button(self, text="Продолжить", width=20, state="disabled")
        self.next_button.pack(pady=10)

    def connect_device(self):
        selected_device = self.device_combo.get()
        if selected_device:
            # Update the status to Connected (Green)
            self.status_label.config(text="Статус: Подключен", foreground="green")
            # Enable the Next button
            self.next_button.config(state="normal")
        else:
            # If no device selected, show Disconnected (Red)
            self.status_label.config(text="Статус: Отключен", foreground="red")
            # Disable the Next button
            self.next_button.config(state="disabled")

if __name__ == "__main__":
    app = DeviceConnectionApp()
    app.mainloop()
