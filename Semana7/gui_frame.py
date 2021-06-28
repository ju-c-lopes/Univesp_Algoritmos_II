from tkinter import Tk, Canvas, Frame, Button, SUNKEN, LEFT, RIGHT


def up():
    """move caneta 10 pixels para cima"""
    global y, canvas                # y é modificado
    canvas.create_line(x, y, x, y - 10)
    y -= 10


def left():
    """move caneta 10 pixels para esquerda"""
    global x, canvas                # x é modificado
    canvas.create_line(x, y, x - 10, y)
    x -= 10


def right():
    """move caneta 10 pixels para direita"""
    global x, canvas                # x é modificado
    canvas.create_line(x, y, x + 10, y)
    x += 10


def down():
    """move caneta 10 pixels para baixo"""
    global y, canvas                # y é modificado
    canvas.create_line(x, y, x, y + 10)
    y += 10


# manipuladores de evento up(), down(), left(), e right()

raiz = Tk()

# tela com borda de tamanho 100 x 500
canvas = Canvas(raiz, height=100, width=150,
                relief=SUNKEN, borderwidth=3)
canvas.pack(side=LEFT)

# frame para manter os 4 botões
box = Frame(raiz)
box.pack(side=RIGHT)

# os 4 widgets de botão tem a caixa do widget Frame como seu master
button_up = Button(box, text="up", command=up)
button_up.grid(row=0, column=0, columnspan=2)
button_left = Button(box, text="left", command=left)
button_left.grid(row=1, column=0)
button_right = Button(box, text="right", command=right)
button_right.grid(row=1, column=1)
button_down = Button(box, text="down", command=down)
button_down.grid(row=2, column=0, columnspan=2)

x, y = 50, 75  # posição da caneta, inicialmente no meio
raiz.mainloop()
