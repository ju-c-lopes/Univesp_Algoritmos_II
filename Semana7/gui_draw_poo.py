from tkinter import Canvas, Frame, BOTH, Tk


class Draw(Frame):
    """Uma aplicação de desenho básica"""
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.pack()

        # coordenadas do mouse são variáveis de instância
        self.oldx, self.oldy = 0, 0

        # cria tela e vincula eventos do mouse aos manipuladores
        self.canvas = Canvas(self, height=200, width=250)
        self.canvas.bind("<Button-1>", self.begin)
        self.canvas.bind("<Button1-Motion>", self.draw)
        self.canvas.pack(expand=True, fill=BOTH)

    def begin(self, event):
        """Trata clique do botão esquerdo registrando posição do mouse"""
        self.oldx, self.oldy = event.x, event.y

    def draw(self, event):
        """Trata movimento do mouse, ao pressionar botão esquerdo,
        conectando posição anterior à nova posição do mouse"""
        newx, newy = event.x, event.y
        self.canvas.create_line(self.oldx, self.oldy, newx, newy)
        self.oldx, self.oldy = newx, newy
