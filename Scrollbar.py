import tkinter as tk

# ---------------- Main Window ----------------
root = tk.Tk()
root.title("Scrollbar Program")
root.geometry("300x300")  # Optional window size

# ---------------- Scrollbar ----------------
scrollbar = tk.Scrollbar(root)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)  # Place scrollbar on right, fill vertically

# ---------------- Listbox ----------------
mylist = tk.Listbox(root, yscrollcommand=scrollbar.set)  # Connect scrollbar to Listbox

# Add items to the Listbox
for i in range(100):
    mylist.insert(tk.END, f"This is line number {i}")

mylist.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)  # Listbox fills the space

# Connect scrollbar command to Listbox scrolling
scrollbar.config(command=mylist.yview)

# ---------------- Run Application ----------------
root.mainloop()
