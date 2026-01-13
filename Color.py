import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("Color Options in Tkinter")
root.geometry("300x200")

# ---------------- Button ----------------
# activebackground → color when button is clicked
# activeforeground → text color when button is clicked
button = tk.Button(
    root,
    text="Don't Click Me",
    activebackground="red",
    activeforeground="white"
)
button.pack(pady=10)

# ---------------- Label ----------------
# bg → background color
# fg → text color
label = tk.Label(
    root,
    text="Hello, deepanshu!",
    bg="white",
    fg="blue",
    width=20
)
label.pack(pady=10)

# ---------------- Entry ----------------
# selectbackground → color of selected text
# selectforeground → text color when selected
entry = tk.Entry(
    root,
    selectbackground="blue",
    selectforeground="lightblue",
    width=25
)
entry.pack(pady=10)

# Run the application
root.mainloop()
