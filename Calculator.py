
import tkinter as tk

# Create the main application window
root = tk.Tk()
root.title("My Calculator")
root.geometry("320x450")
root.resizable(False, False)
root.configure(bg="#9db0e4")

# Calculator display
display = tk.Entry(
    root,
    font=("Arial", 24),
    justify="right",
    bg="#F9F9F9",
    fg="black",
    insertbackground="black",
    relief="flat"
)
display.pack(fill="x", padx=15, pady=20, ipady=15)
display.insert(0, "0")

# Button layout
buttons = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["C", "0", "=", "+"]
]

# Button container
button_frame = tk.Frame(root, bg="#F6F7F7")
button_frame.pack(expand=True, fill="both", padx=10, pady=5)

def button_click(value):
    
    if value == "C":
        display.delete(0, tk.END)
        display.insert(0, "0")
        
    elif value == "=":
        try:
            result = eval(display.get())
            display.delete(0, tk.END)
            display.insert(0, str(result))
        except Exception:
            display.delete(0, tk.END)
            display.insert(0, "Error")
    else:
        current = display.get()
        if current == "Error" or current == "0":
            display.delete(0, tk.END)
        display.insert(tk.END, value)

def keyboard_input(event):
        current = display.get()

        if event.char.isdigit():
            if current == "0" or current == "Error":
                display.delete(0, tk.END)
            return None

# Create calculator buttons
for row_index, row in enumerate(buttons):
    for col_index, value in enumerate(row):
        color = "#42d7eb" if value in ["/", "*", "-", "+", "="] else "#0c0909"

        button = tk.Button(
            button_frame,
            text=value,
            font=("Arial", 18, "bold"),
            bg=color,
            fg="white",
            activebackground="#f8fafd",
            activeforeground="black",
            relief="flat",
            command=lambda v=value: button_click(v)
        )
        button.grid(
            row=row_index,
            column=col_index,
            sticky="nsew",
            padx=4,
            pady=4
        )

for i in range(4):
    button_frame.columnconfigure(i, weight=1)
    button_frame.rowconfigure(i, weight=1)

# Press Enter to calculate the result
root.bind("<Return>", lambda event: button_click("="))
root.bind("<Delete>", lambda event: button_click("C"))
display.bind("<KeyPress>", keyboard_input)


# Start the application
root.mainloop()
