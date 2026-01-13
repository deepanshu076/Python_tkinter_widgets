import tkinter as tk

# Create main window
root = tk.Tk()
root.title("Grid Program")
root.geometry("300x200")

# Create labels
label1 = tk.Label(root, text="Label 1", bg="lightblue", width=10)
label2 = tk.Label(root, text="Label 2", bg="lightgreen", width=10)
label3 = tk.Label(root, text="Label 3", bg="lightyellow", width=22)
label4 = tk.Label(root, text="Label 4", bg="lightpink", width=22)

# Place labels using grid
label1.grid(row=0, column=0, padx=5, pady=5)
label2.grid(row=0, column=1, padx=5, pady=5)

# columnspan makes the label cover 2 columns
label3.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

# Label 4 placed below label 3
label4.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

# Run the application
root.mainloop()
