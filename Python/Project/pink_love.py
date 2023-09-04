import tkinter as tk
from tkinter import messagebox

def calculate_love():
    name1 = entry_name1.get().lower().replace(" ", "")
    name2 = entry_name2.get().lower().replace(" ", "")

    if name1 == "" or name2 == "":
        messagebox.showinfo("Error", "Please enter both names.")
        return

    love_percentage = (len(set(name1 + name2)) / 26) * 100
    messagebox.showinfo("Love Calculator", f"Love Percentage: {love_percentage:.2f}%")

# Create the main window
window = tk.Tk()
window.title("Love Calculator")
window.geometry("300x200")
window.configure(bg="pink")

# Create labels
label_title = tk.Label(window, text="Love Calculator", font=("Arial", 16), bg="pink", fg="white")
label_title.pack(pady=10)

label_name1 = tk.Label(window, text="Name 1:", font=("Arial", 12), bg="pink")
label_name1.pack(pady=5)

# Create entry fields
entry_name1 = tk.Entry(window, font=("Arial", 12))
entry_name1.pack()

label_name2 = tk.Label(window, text="Name 2:", font=("Arial", 12), bg="pink")
label_name2.pack(pady=5)

entry_name2 = tk.Entry(window, font=("Arial", 12))
entry_name2.pack()

# Create calculate button
button_calculate = tk.Button(window, text="Calculate", font=("Arial", 12), command=calculate_love)
button_calculate.pack(pady=10)

# Run the main window's event loop
window.mainloop()
