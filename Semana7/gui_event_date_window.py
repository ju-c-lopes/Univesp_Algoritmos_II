from tkinter import Tk, Button, Label, LEFT, RIGHT, PhotoImage
from tkinter.messagebox import showinfo
from time import strftime, localtime


def clicked():
    time = strftime('Day: %d %b %Y\nTime: %H:%M:%S%p\n', localtime())
    showinfo(title="HORA ATUAL", message=time)


root = Tk()
button = Button(root, text="Click", command=clicked)
button.pack()
root.mainloop()
