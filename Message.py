import tkinter as tk

# ---------------- Main Window ----------------
root = tk.Tk()
root.title("Message Program")
root.geometry("300x150")  # Optional: set window size

# ---------------- Our Message ----------------
our_message = "This is our Message"
message1 = tk.Message(root, text=our_message, width=250, bg="lightgreen", fg="black")
message1.pack(pady=10)

# ---------------- Your Message ----------------
your_message = "This is your Message"
message2 = tk.Message(root, text=your_message, width=250, bg="lightblue", fg="black")
message2.pack(pady=10)

# ---------------- Run Application ----------------
root.mainloop()
