import tkinter as tk

def button_clicked():
    label.configure(text="Button Clicked!")

# Create the main window
window = tk.Tk()
window.title("Mobile GUI")
window.geometry("300x500")

# Create a label
label = tk.Label(window, text="Mobile GUI", font=("Arial", 16))
label.pack(pady=20)

# Create buttons
button1 = tk.Button(window, text="Button 1", font=("Arial", 12), command=button_clicked)
button1.pack(pady=10)

button2 = tk.Button(window, text="Button 2", font=("Arial", 12), command=button_clicked)
button2.pack(pady=10)

button3 = tk.Button(window, text="Button 3", font=("Arial", 12), command=button_clicked)
button3.pack(pady=10)

# Run the main window's event loop
window.mainloop()
