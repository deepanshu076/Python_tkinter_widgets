import tkinter as tk

# ---------------- Main Window ----------------
root = tk.Tk()
root.title("Listbox Program")
root.geometry("250x200")  # Set window size

# ---------------- Listbox ----------------
listbox = tk.Listbox(root, height=6, width=20, bg="lightyellow", fg="blue")
listbox.pack(pady=20)

# Insert items individually without a loop
listbox.insert(1, "Python")
listbox.insert(2, "Java")
listbox.insert(3, "C++")
listbox.insert(4, "Ruby")
listbox.insert(5, "Any other")

# Run the application
root.mainloop()
