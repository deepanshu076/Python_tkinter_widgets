import tkinter as tk

# ---------------- Functions for Events ----------------
def on_key_press(event):
    # Called when any key is pressed
    print(f"Key pressed: {event.keysym}")

def on_left_click(event):
    # Called when left mouse button is clicked
    print(f"Left click at ({event.x}, {event.y})")

def on_right_click(event):
    # Called when right mouse button is clicked
    print(f"Right click at ({event.x}, {event.y})")

def on_mouse_motion(event):
    # Called when mouse is moved over the window
    print(f"Mouse moved to ({event.x}, {event.y})")

# ---------------- Main Window ----------------
root = tk.Tk()
root.title("Event Handling Example")
root.geometry("400x300")  # Set window size for easier testing

# Bind events to the main window
root.bind("<KeyPress>", on_key_press)      # Keyboard key press
root.bind("<Button-1>", on_left_click)     # Left mouse button
root.bind("<Button-3>", on_right_click)    # Right mouse button
root.bind("<Motion>", on_mouse_motion)     # Mouse movement

# Instruction label
tk.Label(root, text="Press keys or click/move the mouse inside the window.",
         wraplength=350, justify="center").pack(pady=20)

# Run the application
root.mainloop()
