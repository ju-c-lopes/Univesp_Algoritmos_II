from tkinter import Tk, Frame, Button, Canvas, LEFT, RIGHT


class Paint(Frame):
    """Gui de desenho por botão"""
    def __init__(self, master):
        Frame.__init__(self, master)
        self.canvas = Canvas(self, height=200, width=200)
        self.canvas.pack(side=LEFT)
        self.x, self.y = 100, 100
        buttons = Frame(self)
        b_up = Button(buttons, text="up", command=self.up)
        b_left = Button(buttons, text="left", command=self.left)
        b_right = Button(buttons, text="right", command=self.right)
        b_down = Button(buttons, text="down", command=self.down)
        b_up.grid(row=0, column=0, columnspan=2)
        b_left.grid(row=1, column=0)
        b_right.grid(row=1, column=1)
        b_down.grid(row=2,column=0, columnspan=2)
        buttons.pack(side=RIGHT)

    def up(self):
        self.canvas.create_line(self.x, self.y, self.x, self.y - 10)
        self.y -= 10

    def left(self):
        self.canvas.create_line(self.x, self.y, self.x - 10, self.y)
        self.x -= 10

    def right(self):
        self.canvas.create_line(self.x, self.y, self.x + 10, self.y)
        self.x += 10

    def down(self):
        self.canvas.create_line(self.x, self.y, self.x, self.y + 10)
        self.y += 10
