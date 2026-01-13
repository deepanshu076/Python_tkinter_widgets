import tkinter as tk

# ---------------- Main Window ----------------
root = tk.Tk()
root.title("Radiobutton Program")
root.geometry("250x150")  # Optional window size

# ---------------- Variable to store selection ----------------
v = tk.IntVar()  # Stores selected value

# ---------------- Radiobuttons ----------------
tk.Radiobutton(root, text="GfG", variable=v, value=1).pack(anchor=tk.W, pady=2)
tk.Radiobutton(root, text="MIT", variable=v, value=2).pack(anchor=tk.W, pady=2)
tk.Radiobutton(root, text="JPG", variable=v, value=3).pack(anchor=tk.W, pady=2)

# ---------------- Run Application ----------------
root.mainloop()
