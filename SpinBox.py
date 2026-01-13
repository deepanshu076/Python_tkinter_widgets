import tkinter as tk

# ---------------- Main Window ----------------
root = tk.Tk()
root.title("Spinbox Program")
root.geometry("200x100")  # Optional window size

# ---------------- Spinbox ----------------
spinbox = tk.Spinbox(root, from_=0, to=100)  # Numbers from 0 to 100
spinbox.pack(pady=20)

# ---------------- Run Application ----------------
root.mainloop()
