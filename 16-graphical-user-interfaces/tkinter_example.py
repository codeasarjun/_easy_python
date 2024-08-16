import tkinter as tk

def on_button_click():
    label.config(text="Button Clicked!")

# create the main window
root = tk.Tk()
root.title("Tkinter Example")

# create a label
label = tk.Label(root, text="Hello, Tkinter!")
label.pack(pady=10)

# create a button
button = tk.Button(root, text="Click Me", command=on_button_click)
button.pack(pady=10)

# start the Tkinter event loop
root.mainloop()
