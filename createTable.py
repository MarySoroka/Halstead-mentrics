import tkinter as tk
import tkinter.ttk as ttk


def createList(opr, opd):
    list1 = []
    list2 = []
    list3 = []
    list4 = []
    i = 0
    while i < len(opr):
        list1.append(opr[i].name)
        list2.append(opr[i].amount)
        i += 1
    j = 0
    while j < len(opd):
        list3.append(opd[j].name)
        list4.append(opd[j].usability)
        j += 1
    return list1, list2, list3, list4


def createTable(opr, oprd):
    root = tk.Tk()
    oprName, oprAmount, oprdName, oprdUse = createList(opr, oprd)
    table = Table(root, headings=('i', 'operators', 'F1i', 'j', 'operands', 'F2j'), operators=tuple(oprName),
                  operatorsAm=tuple(oprAmount), operands=tuple(oprdName), operandsUse=tuple(oprdUse))
    table.pack(expand=tk.YES, fill=tk.BOTH)
    root.mainloop()


class Table(tk.Frame):
    def __init__(self, parent=None, headings=tuple(), operators=tuple(), operatorsAm=tuple(), operands=tuple(),
                 operandsUse=tuple()):
        super().__init__(parent)

        table = ttk.Treeview(self, show="headings", selectmode="browse")
        table["columns"] = headings
        table["displaycolumns"] = headings

        for head in headings:
            table.heading(head, text=head, anchor=tk.CENTER)
            table.column(head, anchor=tk.CENTER)
        i = 0
        j = 0
        if len(operators) >= len(operands):
            while i < len(operators):
                if j > len(operands)-1:
                    table.insert('', tk.END, values=createStringForOutput(i+1, operators[i], operatorsAm[i], '',
                                                                          '', ''))
                    i += 1
                else:
                    table.insert('', tk.END, values=createStringForOutput(i+1, operators[i], operatorsAm[i], j+1,
                                                                          operands[j], operandsUse[j]))
                    i += 1
                    j += 1
        else:
            while j < len(operands):
                if i > len(operators) -1:
                    while j < len(operands):
                        table.insert('', tk.END, values=createStringForOutput('', '', '', j+1,
                                                                              operands[j], operandsUse[i]))
                        j += 1
                else:
                    table.insert('', tk.END, values=createStringForOutput(i+1, operators[i], operatorsAm[i], j+1,
                                                                          operands[j], operandsUse[j]))
                    i += 1
                    j += 1
        scrolltable = tk.Scrollbar(self, command=table.yview)
        table.configure(yscrollcommand=scrolltable.set)
        scrolltable.pack(side=tk.RIGHT, fill=tk.Y)
        table.pack(expand=tk.YES, fill=tk.BOTH)


def createStringForOutput(k1, operator, usability1, k2, operand, usability2):
    value = [k1, operator, usability1, k2, operand, usability2]
    return value
