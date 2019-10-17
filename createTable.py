import tkinter as tk
import tkinter.ttk as ttk


def createTable(opr):
    root = tk.Tk()

    table = Table(root, headings=('i', 'operators', 'F1i', 'j', 'operands', 'F2j'), operators=tuple(opr))
    table.pack(expand=tk.YES, fill=tk.BOTH)
    root.mainloop()


class Table(tk.Frame):
    def __init__(self, parent=None, headings=tuple(), operators=tuple(), operands=tuple()):
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
                if j > len(operands):
                    while i < len(operators):
                        table.insert(values=createStringForOutput(i, operators[i].name, operators[i].usability, '',
                                                                  '', ''))
                        i += 1
                else:
                    table.insert(values=createStringForOutput(i, operators[i].name, operators[i].amount, j,
                                                              operands[j].name, operands[i].usability))
                    i += 1
                    j += 1
        else:
            while j < len(operands):
                if i > len(operators):
                    while j < len(operands):
                        table.insert(values=createStringForOutput('', '', '', j,
                                                                  operands[j].name, operands[i].usability))
                        j += 1
                else:
                    table.insert(values=createStringForOutput(i, operators[i].name, operators[i].amount, j,
                                                              operands[j].name, operands[i].usability))
                    i += 1
                    j += 1
        scrolltable = tk.Scrollbar(self, command=table.yview)
        table.configure(yscrollcommand=scrolltable.set)
        scrolltable.pack(side=tk.RIGHT, fill=tk.Y)
        table.pack(expand=tk.YES, fill=tk.BOTH)


def createStringForOutput(k1, operator, usability1, k2, operand, usability2):
    value = []
    value[0] = k1
    value[1] = operator
    value[2] = usability1
    value[3] = k2
    value[4] = operand
    value[5] = usability2
    return value
