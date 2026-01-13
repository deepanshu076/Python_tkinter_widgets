import tkinter as tk

# ---------------- Main Window ----------------
root = tk.Tk()
root.title("Scale Program")
root.geometry("300x200")  # Optional window size

# ---------------- Vertical Scale ----------------
vertical_scale = tk.Scale(root, from_=0, to=100)
vertical_scale.pack(pady=10)

# ---------------- Horizontal Scale ----------------
horizontal_scale = tk.Scale(root, from_=0, to=200, orient=tk.HORIZONTAL)
horizontal_scale.pack(pady=10)

# ---------------- Run Application ----------------
root.mainloop()
