import tkinter as tk

master = tk.Tk()
master.title('CheckButton program')

# Label
label = tk.Label(master, text='Gender')
label.grid(row=0, column=0, sticky=tk.W)

# Variables
var1 = tk.IntVar()
var2 = tk.IntVar()
var3 = tk.IntVar()

# Checkbuttons
tk.Checkbutton(master, text='Male', variable=var1).grid(row=1, column=0, sticky=tk.W)
tk.Checkbutton(master, text='Female', variable=var2).grid(row=2, column=0, sticky=tk.W)
tk.Checkbutton(master, text='Other', variable=var3).grid(row=3, column=0, sticky=tk.W)

master.mainloop()
