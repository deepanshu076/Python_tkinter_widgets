import tkinter as tk

# Create main window
root = tk.Tk()
root.title("Place Program")
root.geometry("250x200")  # Set window size

# Create a label
label = tk.Label(root, text="Label", bg="lightblue", width=10)

# Place the label at specific coordinates (x, y)
label.place(x=80, y=85)

# Run the application
root.mainloop()
