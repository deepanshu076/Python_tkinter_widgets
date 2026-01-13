import tkinter as tk

# Create main window
root = tk.Tk()
root.title("Pack Program")
root.geometry("250x200")

# Create buttons
button1 = tk.Button(root, text="Button 1", width=15)
button2 = tk.Button(root, text="Button 2", width=15)
button3 = tk.Button(root, text="Button 3", width=15)

# Pack the buttons vertically (top to bottom)
button1.pack(pady=5)
button2.pack(pady=5)
button3.pack(pady=5)

# Run the application
root.mainloop()
