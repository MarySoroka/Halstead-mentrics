import tkinter

from tkinter import *
from tkinter import scrolledtext, filedialog, messagebox


# set the value of checkbox and set te visibiality of button to open file
from createTable import ExampleApp


def setChoose():
    var.set(not var.get())
    if var.get():
        openFileBtn.pack_forget()
        chooseInputType.deselect()
    else:
        chooseInputType.select()
        openFileBtn.pack()


# open dialog to find file and after that define variable fileName as path of the file
# read from file by lines and write into text area in the main form
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
        numOfLine = numOfLine + 1


# show result table
def showTable():
   ExampleApp()


# addition of the all components in the main form and set their size

window = tkinter.Tk()
window.title("Hasltead's metrics")
window.geometry("1000x550")
var = BooleanVar()
var.set(0)
f_top = Frame(window)
f_bot = Frame(window)
textForInput = Label(f_top, width=20, height=2, text="Please, enter yor program")
openFileBtn = Button(f_bot, width=20, height=2, text="Open File", command=openFile)
chooseInputType = Checkbutton(f_top, width=20, height=2, text="Read from file", variable=var, command=setChoose)
inputText = scrolledtext.ScrolledText(f_bot, width=700, height=25)
inputText.configure(font="Calibri 10")
analyseBtn = Button(f_bot, width=20, height=2, text="Analyse", command=showTable)

f_top.pack()
f_bot.pack()

textForInput.pack(side=LEFT)
chooseInputType.pack()
inputText.pack(side=TOP, padx=10, pady=10)
analyseBtn.pack(side=BOTTOM, padx=10, pady=10)

window.mainloop()
