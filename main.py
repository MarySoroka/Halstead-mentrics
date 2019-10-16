import tkinter
import sourses
from tkinter import *
from tkinter import scrolledtext, filedialog, messagebox



from createTable import ExampleApp
from workWithOperators import findingOperators, findDot


def delitingImports(redString):
    if redString[0] == "import":
        redString = " "
    return redString


def delitingOfOOP(redString):
    i = 0
    while i < len(redString):
        if sourses.oop_delete.get(redString[i], 0) != 0:
            del redString[i]
        i += 1
    return redString


# set the value of checkbox and set te visibiality of button to open file
def setChoose():
    var.set(not var.get())
    if var.get():
        openFileBtn.pack_forget()
        chooseInputType.deselect()
    else:
        chooseInputType.select()
        openFileBtn.pack()


# show result table
def showTable():
    if inputText.get('0.1') == '\n':
        messagebox.showerror('Error', 'Please, choose your file or inter your text')
    else:
        ExampleApp()
        readFromTextbox()



def readFromTextbox():
    resultListOfOperators = []
    resultOfOperands = []
    text = inputText.get('1.0', END).splitlines()
    for line in text:
        clearLine = delitingImports(line.split())
        if clearLine != " ":
             lineWithDot = delitingOfOOP(clearLine)
             operators, operands = findingOperators(findDot(lineWithDot))
             resultListOfOperators.extend(operators)
             resultOfOperands.extend(operands)
    return resultListOfOperators, resultOfOperands


# open dialog to find file and after that define variable fileName as path of the file
# read from file by lines and write into text area in the main form
def openFile():
    fileName = filedialog.askopenfilename(filetypes=(("TXT files", "*.txt"),))
    inputText.delete('1.0', END)
    name = fileName
    try:
        f = open(name, 'r')
        numOfLine = 0
        for line in f:
            if numOfLine == 0:
                line = line[1:]
                line = line[:0] + ' ' + line[1:]
            inputText.insert(END, line)
            numOfLine = numOfLine + 1
    except (OSError, IOError) as e:
        messagebox.showerror('Error', 'Please, choose your file or inter your text')


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
