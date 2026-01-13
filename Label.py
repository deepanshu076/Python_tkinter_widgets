import tkinter as tk

# ---------------- Main Window ----------------
root = tk.Tk()
root.title("Label Program")
root.geometry("300x100")  # Set window size

# ---------------- Label ----------------
label = tk.Label(
    root,
    text="deepanshu github",
    font=("Arial", 14),       # Set font and size
    fg="blue",                # Text color
    bg="lightyellow",         # Background color
    padx=10, pady=10          # Padding inside the label
)
label.pack(pady=20)           # Pack with vertical spacing

# Run the application
root.mainloop()
