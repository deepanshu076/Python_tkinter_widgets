import tkinter as tk
master = tk.Tk()
master.title('Canvas Program')
w = tk.Canvas(master, width=400, height=600 , bg="white")
w.pack()
canvas_height=400
canvas_width=3300
w.create_rectangle(50, 50, 300, 200, outline="black", fill="blue", width=2)
master.mainloop()

# import tkinter as tk

# # Create main window
# root = tk.Tk()
# root.title("Draw Rectangle")

# # Create canvas
# canvas = tk.Canvas(root, width=400, height=300, bg="white")
# canvas.pack()

# # Draw rectangle (x1, y1, x2, y2)
# canvas.create_rectangle(50, 50, 300, 200, outline="black", fill="lightblue", width=2)

# # Run the application
# root.mainloop()
