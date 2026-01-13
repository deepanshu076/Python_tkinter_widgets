import tkinter as tk

# ---------------- Main Window ----------------
root = tk.Tk()
root.title("Text Widget Program")
root.geometry("350x150")  # Optional window size

# ---------------- Text Widget ----------------
text_widget = tk.Text(root, height=4, width=40)  # Bigger area to see text clearly
text_widget.pack(pady=20)

# Insert text into the Text widget
text_widget.insert(tk.END, "deepanshu\nBEST GITHUB\n")

# ---------------- Run Application ----------------
root.mainloop()
