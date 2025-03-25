import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

class ElectrodePlacementApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Схема подключения к оборудованию")
        self.geometry("800x600")
        self.configure(bg="#f0f0f0")

        # Title Label
        title_label = ttk.Label(self, text="Схема подключения к оборудованию", font=("Helvetica", 20, "bold"))
        title_label.pack(pady=20)

        # Load the image (update the path to your local image file)
        image_path = "images/BioRadio.png"  # Replace with your actual image file path
        image = Image.open(image_path)
        image = image.resize((600, 400), Image.LANCZOS)
        photo = ImageTk.PhotoImage(image)

        # Image Label
        image_label = ttk.Label(self, image=photo)
        image_label.image = photo  # Keep a reference to avoid garbage collection
        image_label.pack(pady=20)

        # Next Button
        next_button = ttk.Button(self, text="Продолжить", width=20)
        next_button.pack(pady=20)

if __name__ == "__main__":
    app = ElectrodePlacementApp()
    app.mainloop()
