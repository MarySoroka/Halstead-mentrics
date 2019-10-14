import tkinter
from tkinter import *



window = tkinter.Tk()
window.title("Hasltead's metrics")
window.geometry('800x500')
lbl = Label(window, text="Your program")
lbl.grid(column=0, row=0)
btn = Button(window, text="Analyse")
btn.grid(column=1, row=0)
TextArea = tkinter.Text(window)

window.mainloop()

