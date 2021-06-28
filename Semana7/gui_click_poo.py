from tkinter import Tk, Button, Frame
from tkinter.messagebox import showinfo
from time import strftime, localtime


class ClickIt(Frame):
    """GUI que apresenta a hora atual"""
    def __init__(self, master):
        Frame.__init__(self, master)
        self.pack()
        button = Button(self, text="Click it", command=self.clicked)
        button.pack()

    def clicked(self):
        """apresenta informações de dia e hora"""
        time = strftime("Dia: %d %b %Y\nHora: %H:%M:%S %p\n", localtime())
        showinfo(message=time)


raiz = Tk()
app = ClickIt(raiz)
app.pack()
raiz.mainloop()
