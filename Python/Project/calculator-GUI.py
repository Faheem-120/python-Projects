import tkinter as tk

def button_click(event):
    # Get the text from the clicked button
    text = event.widget.cget("text")
    
    if text == "=":
        try:
            # Evaluate the expression
            expression = entry.get()
            result = eval(expression)
            entry.delete(0, tk.END)
            entry.insert(tk.END, result)
        except Exception as e:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif text == "C":
        # Clear the entry
        entry.delete(0, tk.END)
    else:
        # Append the clicked button's text to the entry
        entry.insert(tk.END, text)

# Create the main window
window = tk.Tk()
window.title("Calculator")

# Create an entry widget to display the expression and results
entry = tk.Entry(window, width=50)
entry.grid(row=0, column=0, columnspan=7)

# Define the button labels
buttons = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "0", ".", "=", "+",
    "C"
]

# Create and position the buttons
row = 1
col = 0
for button in buttons:
    btn = tk.Button(window, text=button, width=9)
    btn.grid(row=row, column=col)
    btn.bind("<Button-1>", button_click)  # Bind the click event
    col += 1
    if col > 3:
        col = 0
        row += 1

# Start the GUI event loop
window.mainloop()
