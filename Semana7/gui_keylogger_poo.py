from tkinter import Text, Frame, BOTH, Tk


class KeyLogger(Frame):
    """Um editor básico que registra as teclas pressionadas"""
    def __init__(self,  master=None):
        Frame.__init__(self, master)
        self.pack()
        text = Text(width=20, height=5)
        text.bind("<KeyPress>", self.record)
        text.pack(expand=True, fill=BOTH)

    def record(self, event):
        """Trata dos eventos de toque de tecla exibindo
        caracteres associados à tecla"""
        print('char={}'.format(event.keysym))
