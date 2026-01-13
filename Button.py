import tkinter as tk
r = tk.Tk()
r.title('Button program')
button = tk.Button(r, text='End', width=25, command=r.destroy)
button.pack()
r.mainloop()