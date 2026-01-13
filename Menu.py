import tkinter as tk

# ---------------- Main Window ----------------
root = tk.Tk()
root.title("Menu Program")
root.geometry("300x200")  # Optional: set window size

# ---------------- Main Menu ----------------
menu = tk.Menu(root)
root.config(menu=menu)

# ---------------- File Menu ----------------
file_menu = tk.Menu(menu, tearoff=0)  # tearoff=0 removes dashed line
menu.add_cascade(label="File", menu=file_menu)

# Add commands to File menu
file_menu.add_command(label="New")       # New file
file_menu.add_command(label="Copy")      # Copy
file_menu.add_command(label="Paste")     # Paste
file_menu.add_separator()                # Separator line
file_menu.add_command(label="Exit", command=root.quit)  # Exit app

# ---------------- Help Menu ----------------
help_menu = tk.Menu(menu, tearoff=0)
menu.add_cascade(label="Help", menu=help_menu)

# Add commands to Help menu
help_menu.add_command(label="About")     # About info
help_menu.add_command(label="Theme")     # Theme option

# ---------------- Run the Application ----------------
root.mainloop()
