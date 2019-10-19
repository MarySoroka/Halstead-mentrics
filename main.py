import tkinter
import sourses
import math
from tkinter import *
from tkinter import scrolledtext, filedialog, messagebox

from createTable import createTable
from ourclass import RecordOperators
from workWithOperators import findingOperators, findDot, deleteRepeatObj, editFunc


def delitingMultiComments(redString):
    i = 0
    while i < len(redString):
        if redString[i] == "/**" or redString[i] == "*" or redString[i] == "*/" or redString[i] == "/*":
            retStr = " "
            return retStr
        else:
            i += 1
    return redString


def delitingMultigovno(redString):
    i = 0
    while i < len(redString):
        if redString[i] == "/*":
            return 1
        else:
            i += 1
    return 0


# удаляю строки с импортами и пэкеджами
def delitingOfImport(redString):
    i = 0
    while i < len(redString):
        if redString[i] == "import" or redString[i] == "package" or redString[i] == "//" or redString[i] == "class" or redString[i] == "static":
            returnString = ' '
            return returnString
        i += 1
    return redString


def returningOfnames(redString):
    i = 0
    newLine = " "
    while i < len(redString):
        if redString[i] == "$" and len(redString[i + 1]) <= len(redString) and redString[i + 1] == "{":
            end = redString.find("}")
            j = i
            while j <= end:
                newLine += redString[j]
                j += 1
            return newLine
        else:
            i += 1
    redString = " "
    return redString


# удаляю всякие распечатки строк
def delitingOfStrings(redString):
    finding = '"'
    newLine = " "
    if redString.find(finding) != -1:
        start = redString.find(finding)
        ending = redString.rfind(finding)
        i = 0
        while i <= start:
            newLine += redString[i]
            i += 1
        i = ending
        while i < len(redString):
            newLine += redString[i]
            i += 1

        smLine = " "
        i = start + 1
        while i < ending:
            smLine += redString[i]
            i += 1
        workString = returningOfnames(redString)
        newLine = newLine + " " + workString
    else:
        newLine = redString
    return newLine


# создание листа с операторами и их подсчётом
def editingOperatorsList(listOfOperators):
    i = 0
    h = 0
    length = len(listOfOperators)
    while i < length:
        j = i + 1
        while j < length:
            if listOfOperators[i].name == listOfOperators[j].name:
                listOfOperators[i].amount = listOfOperators[i].amount + listOfOperators[j].amount
                del listOfOperators[j]
                h += 1
                length = len(listOfOperators)
            else:
                j += 1
        i += 1
    return listOfOperators


# delete oop words
def delitingOfOOP(redString):
    i = 0
    while i < len(redString):
        if sourses.oop_delete.get(redString[i], 0) != 0:
            del redString[i]
        else:
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


def editFuncList(operators, operands, func):
    i = 0
    while i < len(func):
        j = 0
        while j < len(operands):
            if operands[j].name == func[i].name:
                funcOpr = RecordOperators(func[i].name, 1)
                operators.append(funcOpr)
                operators.extend(func[i].operators)
                operands.extend(func[i].operands)
                del operands[j]
            else:
                j += 1
        i += 1
    return operators, operands


# show result table
def showTable():
    if inputText.get('0.1') == '\n':
        messagebox.showerror('Error', 'Please, choose your file or inter your text')
    else:
        list1, list2, list3 = readFromTextbox()
        list2 = deleteRepeatObj(list2)
        list1, list2 = editFuncList(list1, list2, list3)
        list2 = deleteRepeatObj(list2)
        list1 = editingOperatorsList(list1)
        # считаю метрики
        programmDictionary = len(list1) + len(list2)
        programmLength = 0
        i = 0
        while i < len(list1):
            programmLength += list1[i].amount
            i += 1
        i = 0
        while i < len(list2):
            programmLength += list2[i].initialization + list2[i].usability
            i += 1

        programPower = programmLength * math.log2(programmDictionary)
        createTable(list1, list2, str(int(programPower)))


def convert(list):
    # Converting integer list to string list
    i = 0
    res = ''
    while i < len(list):
        res = res + ' ' + list[i]
        i += 1
    return (res)


def readFromTextbox():
    resultListOfOperators = []
    resultOfOperands = []
    funcList = []
    text = inputText.get('1.0', END).splitlines()
    i = 0
    while i < len(text):
        line = text[i]
        if line != '':
            line = text[i].split()
            str = text[i]
            if line[0] == 'def':
                ind1 = ind2 = 0
                funcStr = ''
                while ind1 != ind2 or ind1 == ind2 == 0:
                    j = 0
                    line = text[i].split()
                    while j < len(line):
                        if line[j] == '{':
                            ind1 += 1
                        elif line[j] == '}':
                            ind2 += 1
                        j += 1
                    delStringLine = delitingOfStrings(text[i])
                    anotherDel = delitingMultiComments(delStringLine.split())
                    lineWithDot = convert(delitingOfOOP(anotherDel))
                    funcStr = funcStr + ' ' + lineWithDot
                    i += 1
                funcList.append(editFunc(funcStr.split()))
            else:
                delStringLine = delitingOfStrings(str)
                anotherDel = delitingMultiComments(delStringLine.split())
                if anotherDel != " ":
                    lineWithoutImport = delitingOfImport(anotherDel)
                    if lineWithoutImport != " ":
                        lineWithDot = delitingOfOOP(lineWithoutImport)
                        operators, operands = findingOperators(findDot(lineWithDot))
                        resultListOfOperators.extend(operators)
                        resultOfOperands.extend(operands)
                i += 1
        else:
            i += 1
    finalOperatorsList = editingOperatorsList(resultListOfOperators)
    return finalOperatorsList, resultOfOperands, funcList


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
                line = line[:0] + ' ' + line[2:]
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
