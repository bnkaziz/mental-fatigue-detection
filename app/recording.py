import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from PIL import Image, ImageTk
import time

class RecordingApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Запись и визуализация данных")
        self.geometry("800x600")
        self.configure(bg="#f0f0f0")

        # Control Frame (for buttons and indicators)
        control_frame = ttk.Frame(self)
        control_frame.pack(side=tk.TOP, pady=10)

        # Load button icons (using placeholder colors and simple shapes)
        pause_icon = Image.open("images/icons/pause.png").resize((30, 30))
        play_icon = Image.open("images/icons/play.png").resize((30, 30))
        stop_icon = Image.open("images/icons/stop.png").resize((30, 30))
        record_icon = Image.open("images/icons/record.png").resize((30, 30))

        pause_img = ImageTk.PhotoImage(pause_icon)
        play_img = ImageTk.PhotoImage(play_icon)
        stop_img = ImageTk.PhotoImage(stop_icon)
        record_img = ImageTk.PhotoImage(record_icon)

        # Buttons with icons
        pause_button = ttk.Button(control_frame, image=pause_img, command=self.pause)
        pause_button.image = pause_img
        pause_button.pack(side=tk.LEFT, padx=5)

        play_button = ttk.Button(control_frame, image=play_img, command=self.play)
        play_button.image = play_img
        play_button.pack(side=tk.LEFT, padx=5)

        stop_button = ttk.Button(control_frame, image=stop_img, command=self.stop)
        stop_button.image = stop_img
        stop_button.pack(side=tk.LEFT, padx=5)

        record_button = ttk.Button(control_frame, image=record_img, command=self.record)
        record_button.image = record_img
        record_button.pack(side=tk.LEFT, padx=5)

        # Save Button
        save_button = ttk.Button(control_frame, text="Сохранить файл", command=self.save_file)
        save_button.pack(side=tk.LEFT, padx=10)

        # Timer Label
        self.timer_label = ttk.Label(control_frame, text="00:33:49", font=("Helvetica", 16))
        self.timer_label.pack(side=tk.LEFT, padx=20)

        # Fatigue Indicator (Gray by default)
        self.indicator = tk.Canvas(control_frame, width=20, height=20)
        self.indicator.create_oval(2, 2, 18, 18, fill="gray", outline="", tags="oval")
        self.indicator.pack(side=tk.LEFT, padx=10)

        # Recording Status
        self.is_recording = False
        self.start_time = None

        # Empty Data Visualization Frame
        self.data_frame = ttk.Frame(self, relief=tk.SUNKEN)
        self.data_frame.pack(fill=tk.BOTH, expand=True, pady=20, padx=20)

        # Timer Thread
        self.running = False

    def toggle_fatigue(self):
        current_color = self.indicator.itemcget("oval", "fill")
        new_color = "green" if current_color == "red" else "red"
        self.indicator.itemconfig("oval", fill=new_color)

    def start_timer(self):
        self.start_time = time.time()
        self.running = True
        self.update_timer()

    def update_timer(self):
        if self.running:
            elapsed = int(time.time() - self.start_time)
            formatted_time = time.strftime("%H:%M:%S", time.gmtime(elapsed))
            self.timer_label.config(text=formatted_time)
            self.after(1000, self.update_timer)

    def stop_timer(self):
        self.running = False

    def pause(self):
        print("Pause clicked")
        self.stop_timer()

    def play(self):
        print("Play clicked")
        if not self.running:
            self.start_timer()

    def stop(self):
        print("Stop clicked")
        self.stop_timer()
        self.timer_label.config(text="00:00:00")

    def record(self):
        print("Record clicked")
        self.start_timer()
        self.indicator.itemconfig("oval", fill="green")

    def save_file(self):
        print("Save clicked")
        file_path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV files", "*.csv"), ("All files", "*.*")])
        if file_path:
            # Placeholder for saving data, for now just print the path
            print(f"File saved at: {file_path}")

if __name__ == "__main__":
    app = RecordingApp()
    app.mainloop()
