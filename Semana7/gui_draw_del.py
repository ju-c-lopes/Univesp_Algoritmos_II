from tkinter import Tk, Canvas


def begin(event):
    """inicializa o início da curva com a posição do mouse"""
    global oldx, oldy, curve
    oldx, oldy = event.x, event.y
    curve = []


def draw(event):
    """Desenha um segmento de linha da posição antiga do mouse à nova"""
    global oldx, oldy, canvas, curve  # x e y são mudados
    newx, newy = event.x, event.y   # nova posição do mouse
    # conecta posição anterior do mouse à atual
    curve.append(canvas.create_line(oldx, oldy, newx, newy))
    oldx, oldy = newx, newy         # nova posição torna-se a anterior


def delete(event):
    """Exclui última curva desenhada"""
    global curve
    for segment in curve:
        canvas.delete(segment)


# manipuladores de evento começam e desenham aqui

raiz = Tk()

oldx, oldy = 0, 0  # coordenadas do mouse (variáveis globais)
curve = list()

# canvas
canvas = Canvas(raiz, height=200, width=250)

# vincula evento de clique do botão esquerdo à função begin()
canvas.bind("<Button-1>", begin)

# vincula evento de movimento do mouse enquanto o botão está pressionado
canvas.bind("<Button1-Motion>", draw)

# vinculo Ctrl com botão esquerdo do mouse a delete()
canvas.bind("<Control-Button-1>", delete)

canvas.pack()
raiz.mainloop()
