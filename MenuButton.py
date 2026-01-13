import tkinter as tk

# ---------------- Main Window ----------------
root = tk.Tk()
root.title("Menubutton Program")
root.geometry("250x150")  # Optional: window size

# ---------------- Menubutton 1 ----------------
mb1 = tk.Menubutton(root, text="GfG", relief="raised")
mb1.menu = tk.Menu(mb1, tearoff=0)
mb1["menu"] = mb1.menu

# Variables for checkbuttons
contact_var = tk.IntVar()
about_var = tk.IntVar()

# Add checkbuttons to Menubutton 1
mb1.menu.add_checkbutton(label="Contact", variable=contact_var)
mb1.menu.add_checkbutton(label="About", variable=about_var)

# Pack Menubutton 1
mb1.pack(pady=10)

# ---------------- Menubutton 2 ----------------
mb2 = tk.Menubutton(root, text="Python", relief="raised")
mb2.menu = tk.Menu(mb2, tearoff=0)
mb2["menu"] = mb2.menu

# Variables for checkbuttons
copy_var = tk.IntVar()
paste_var = tk.IntVar()

# Add checkbuttons to Menubutton 2
mb2.menu.add_checkbutton(label="Copy", variable=copy_var)
mb2.menu.add_checkbutton(label="Paste", variable=paste_var)

# Pack Menubutton 2
mb2.pack(pady=10)

# ---------------- Run Application ----------------
root.mainloop()
