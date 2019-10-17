import tkinter
import  math
import sourses
import ourclass
from tkinter import *
from tkinter import scrolledtext, filedialog, messagebox

from createTable import CreateTable
from workWithOperators import findingOperators, findDot, deleteRepeatObj

#удаляю строки с импортами и пэкеджами
def delitingOfImport(redString):
    if redString[0] == "import" or redString[0] == "package":
        returnString = ' '
        return returnString
    else:
        return redString


#удаляю всякие распечатки строк
def delitingOfStrings(redString):
    finding = """"""
    if redString.find(finding) != -1:
        start = redString.find(finding)
        ending = redString.rfind(finding)
        i = 0
        newLine = ""
        while i < start:
            newLine += redString[i]
            i += 1
        i = ending+1
        while i < len(redString):
            newLine += redString[i]
            i += 1
    return newLine

#создание листа с операторами и их подсчётом
def editingOperatorsList(listOfOperators):
    i = 0
    while i < len(listOfOperators):
        j = 0
        while j < len(listOfOperators):
            if listOfOperators[i].name == listOfOperators[j].name and j != i:
                listOfOperators[i].amount = listOfOperators[i].amount + listOfOperators[j].amount
                del listOfOperators[j]
            j += 1
        i += 1
    return listOfOperators



#delete oop words
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
        list1, list2 = readFromTextbox()
        list2 = deleteRepeatObj(list2)


        # считаю метрики
        programmDictionary = len(list1)+len(list2)
        programmLength = 0
        i=0
        while i<len(list1):
            programmLength += list1[i].amount
            i += 1
        i = 0
        while i < len(list2):
            programmLength += list2[i].initialization + list2[i].usability
            i += 1
        programPower = programmLength * math.log2(programmDictionary)


        CreateTable(list1, list2)


def readFromTextbox():
    resultListOfOperators = []
    resultOfOperands = []
    text = inputText.get('1.0', END).splitlines()
    for line in text:
        lineWithDot = delitingOfOOP(line.split())
        operators, operands = findingOperators(findDot(lineWithDot))
        resultListOfOperators.extend(operators)
        resultOfOperands.extend(operands)
    finalListOfOperators = editingOperatorsList(resultListOfOperators)
    return finalListOfOperators, resultOfOperands



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
