import tkinter as tk

# ---------- Function ----------
# This function runs when the user selects an option
def show_selection(*args):
    label_result.config(
        text="Selected Item: " + selected_value.get()
    )

# ---------- Main Window ----------
root = tk.Tk()
root.title("Dropdown Example")
root.geometry("300x180")

# ---------- Label ----------
label_info = tk.Label(root, text="Choose an option:")
label_info.pack(pady=5)

# ---------- Variable ----------
# This variable stores the selected option
selected_value = tk.StringVar()
selected_value.set("Select an option")

# ---------- Dropdown Options ----------
options = ["Option 1", "Option 2", "Option 3", "Option 4"]

# ---------- OptionMenu ----------
dropdown = tk.OptionMenu(root, selected_value, *options)
dropdown.pack(pady=5)

# ---------- Result Label ----------
label_result = tk.Label(root, text="Selected Item: None", fg="blue")
label_result.pack(pady=10)

# ---------- Track Selection Change ----------
selected_value.trace("w", show_selection)

# ---------- Run Program ----------
root.mainloop()
