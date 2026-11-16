import tkinter as tk
from tkinter import messagebox

def on_button_click():
    """This function runs whenever the button is clicked."""
    messagebox.showinfo("Success", "You clicked the button!")

# 1. Initialize the main application window
root = tk.Tk()
root.title("GitHub Python Button Example")
root.geometry("400x200")

# 2. Create the button widget
# 'command' binds the click event to our function
button = tk.Button(
    root, 
    text="Click Me!", 
    command=on_button_click,
    fg="white", 
    bg="#24292e",  # GitHub dark gray color
    font=("Arial", 12, "bold"),
    padx=10,
    pady=5
)

# 3. Position the button inside the window
button.pack(expand=True)

# 4. Start the application loop
root.mainloop()
