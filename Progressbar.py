import tkinter as tk
from tkinter import ttk

# ---------------- Main Window ----------------
root = tk.Tk()
root.title("Progressbar Program")
root.geometry("350x150")

# ---------------- Progressbar ----------------
progress = ttk.Progressbar(root, orient="horizontal", length=300, mode="determinate")
progress.pack(pady=20)

# ---------------- Control Variables ----------------
running = False  # Tracks whether progress is running

# ---------------- Function to update progress ----------------
def update_progress(value=0):
    global running
    if not running:  # Stop if running is False
        return
    if value > 100:  # Stop when progress reaches 100%
        running = False
        return
    progress['value'] = value
    root.update_idletasks()
    # Schedule next increment
    root.after(50, update_progress, value + 1)

# ---------------- Start Progress ----------------
def start_progress():
    global running
    if not running:
        running = True
        update_progress(int(progress['value']))  # Resume from current value

# ---------------- Stop Progress ----------------
def stop_progress():
    global running
    running = False  # Stops the progress

# ---------------- Buttons ----------------
start_button = tk.Button(root, text="Start", command=start_progress)
start_button.pack(side="left", padx=20, pady=10)

stop_button = tk.Button(root, text="Stop", command=stop_progress)
stop_button.pack(side="right", padx=20, pady=10)

# ---------------- Run Application ----------------
root.mainloop()
