from tkinter import Tk, Button, Label, Entry, END
from tkinter.messagebox import showinfo
from time import strftime, strptime


def clear():
    global entry
    entry.delete(0, END)


def clicked():
    global entry
    date = entry.get()
    entry.delete(0, END)
    weekday = strftime("%A", strptime(date, "%b, %d, %Y"))
    entry.insert(0, weekday)


root = Tk()
label = Label(root, text="Digite uma data:")
label.grid(row=0, column=0)
entry = Entry(root)
entry.grid(row=0, column=1)
button_click = Button(root, text="Click", command=clicked)
button_click.grid(row=1, column=0)
button_clear = Button(root, text="clear", command=clear)
button_clear.grid(row=1, column=1)

root.mainloop()
