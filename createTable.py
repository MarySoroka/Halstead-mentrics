import tkinter as tk


class CreateTable(tk.Tk):
    def __init__(self, operators, operands):
        tk.Tk.__init__(self)
        t = SimpleTable(self, len(operators), 6)
        t.pack(side="top", fill="x")
        t.set(0, 0, "j")
        t.set(0, 1, "operators")
        t.set(0, 2, "F1j")
        t.set(0, 3, "i")
        t.set(0, 4, "operands")
        t.set(0, 5, "F2i")
        k = 1

        while k < 30:
            t.set(k, 0, k)
            t.set(k, 1, k + 1)
            k += 1

        k = 1
        while k < len(operators):
            t.set(k, 0, k + 1)
            t.set(k, 1, operators[k-1])
            k += 1

        k = 1
        while k < len(operands):
            t.set(k, 3, k + 1)
            t.set(k, 4, operands[k-1].name)
            t.set(k, 5, operands[k-1].usability)
            k += 1


class SimpleTable(tk.Frame):
    def __init__(self, parent, rows, columns=6):
        # use black background so it "peeks through" to
        # form grid lines
        tk.Frame.__init__(self, parent, background="black")
        self._widgets = []
        for row in range(rows):
            current_row = []
            for column in range(columns):
                label = tk.Label(self, text=" ", borderwidth=0, width=20)
                label.grid(row=row, column=column, sticky="nsew", padx=1, pady=1)
                current_row.append(label)
            self._widgets.append(current_row)

        for column in range(columns):
            self.grid_columnconfigure(column, weight=1)

    def set(self, row, column, value):
        widget = self._widgets[row][column]
        widget.configure(text=value)


if __name__ == "__main__":
    app = CreateTable()
    app.mainloop()
