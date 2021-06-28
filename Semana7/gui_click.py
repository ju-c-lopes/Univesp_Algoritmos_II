from tkinter import Tk, Button
from time import strftime, localtime


def clicked():
    """exibe informação de dia e hora"""
    hora = strftime("Dia: %d %b %Y\nHora: %H:%M:%S %p\n", localtime())
    print(hora)


raiz = Tk()
# Cria botão rotulado com 'Clique aqui' e manipulaldor de evento clicked()
button = Button(raiz, text='Click it', command=clicked)
button.pack()
raiz.mainloop()
