import tkinter
from tkinter import *
from tkinter import scrolledtext, filedialog


def openFile():
    fileName = filedialog.askopenfilename(filetypes=(("TXT files", "*.txt"),))
    inputText.delete('1.0', END)
    f = open(fileName, 'r')
    numOfLine = 0

    for line in f:
        if numOfLine == 0:
            line = line[1:]
            line = line[:0] + ' ' + line[1:]
        inputText.insert(END, line)
        numOfLine = numOfLine+1


window = tkinter.Tk()
window.title("Hasltead's metrics")
window.geometry("700x550")
f_top = Frame(window)
f_bot = Frame(window)
textForInput = Label(f_top, width=20, height=2, text="Please, enter yor program")
openFileBtn = Button(f_bot, width=20, height=2, text="Open File", command=openFile)
chooseInputType = Radiobutton(f_top, width=20, height=2, text="Read from file")
inputText = scrolledtext.ScrolledText(f_bot, width=100, height=25)
analyseBtn = Button(f_bot, width=20, height=2, text="Analyse")

f_top.pack()
f_bot.pack()

textForInput.pack(side=LEFT)
chooseInputType.pack()
openFileBtn.pack()
inputText.pack(side=TOP, padx=10, pady=10)
analyseBtn.pack(side=BOTTOM, padx=10)

window.mainloop()
