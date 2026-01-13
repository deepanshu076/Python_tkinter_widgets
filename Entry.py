import tkinter as tk

# Create main window
master = tk.Tk()
master.title("Entry Program")
master.geometry("300x150")

# Labels
tk.Label(master, text="First Name:").grid(row=0, column=0, padx=10, pady=10, sticky=tk.W)
tk.Label(master, text="Last Name:").grid(row=1, column=0, padx=10, pady=10, sticky=tk.W)

# Entry fields
e1 = tk.Entry(master, width=25)
e2 = tk.Entry(master, width=25)

e1.grid(row=0, column=1, padx=10, pady=10)
e2.grid(row=1, column=1, padx=10, pady=10)

# Run the application
master.mainloop()
