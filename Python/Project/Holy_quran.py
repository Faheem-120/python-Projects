from tkinter import *
from tkinter import ttk

def load_quran():
    with open("quran.txt", "r") as file:
        quran_text.insert(END, file.read())

window = Tk()
window.title("Holy Quran")
window.geometry("800x600")

quran_text = Text(window)
quran_text.pack(fill=BOTH, expand=True)

load_button = ttk.Button(window, text="Load Quran", command=load_quran)
load_button.pack()

window.mainloop()
