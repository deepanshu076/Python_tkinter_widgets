import tkinter as tk

# ---------------- Main Window ----------------
root = tk.Tk()
root.title("PanedWindow Program")
root.geometry("400x200")  # Optional: set window size

# ---------------- Main PanedWindow (horizontal) ----------------
paned1 = tk.PanedWindow(root, bd=4, relief="sunken")
paned1.pack(fill=tk.BOTH, expand=1)

# ---------------- Left Pane: Entry ----------------
entry_left = tk.Entry(paned1, bd=5)
paned1.add(entry_left)

# ---------------- Right Pane: Nested Vertical PanedWindow ----------------
paned2 = tk.PanedWindow(paned1, orient=tk.VERTICAL, bd=4, relief="sunken")
paned1.add(paned2)

# ---------------- Top Pane: Scale ----------------
scale_top = tk.Scale(paned2, orient=tk.HORIZONTAL, from_=0, to=100, label="Adjust Value")
paned2.add(scale_top)

# ---------------- Run Application ----------------
root.mainloop()
