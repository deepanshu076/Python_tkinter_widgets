import tkinter as tk

# ---------------- Main Window ----------------
root = tk.Tk()
root.title("Toplevel Program")
root.geometry("300x150")  # Optional window size

# ---------------- Toplevel Windows ----------------
top_window = tk.Toplevel(root)
top_window.title("Python")
top_window.geometry("200x100")

bottom_window = tk.Toplevel(root)
bottom_window.title("Java")
bottom_window.geometry("200x100")

# ---------------- Run Application ----------------
root.mainloop()
