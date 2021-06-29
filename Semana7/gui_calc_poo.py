from tkinter import Tk, Frame, Button, RAISED, RIDGE, Entry, END


class Calc(Frame):
    def __init__(self, parent=None):
        Frame.__init__(self, parent)
        # rótulos de botão de calculadora em uma lista 2D
        buttons = [['MC', 'M+', 'M-', 'MR'],
                   ['C', '\u221a', 'x\u00b2', '+'],
                   ['7', '8', '9', '-'],
                   ['4', '5', '6', '*'],
                   ['1', '2', '3', '/'],
                   ['0', '.', '+-', '=']]

        # cria e coloca botões na linha e coluna apropriada
        for r in range(6):
            for c in range(4):
                # função cmd() é definida, de modo que quando
                # chamada sem um argumento de entrada, executa
                # self.click(buttons[r][c])
                def cmd(x=buttons[r][c]):
                    self.click(x)

                b = Button(self,            # botão para símbolo buttons[r][c]
                           text=buttons[r][c],
                           width=3, relief=RAISED, command=cmd)
                # cmd é o manipulador
                b.grid(row=r+1, column=c)   # entrada é na linha 0

        # usa o widget Entry para exibição
        self.entry = Entry(self, relief=RIDGE, borderwidth=3,
                           width=20, bg='gray',
                           font=('Helvetica', 18))
        self.entry.grid(row=0, column=0, columnspan=5)
        self.entry.insert(END, '0')
        self.expr = ''
        self.memory = 0
        self.startOfNextOperand = False

    def click(self, key):
        """Manipulador para evento de pressionar tecla rotulada do botão"""
        if key == '=':
            # avalia a expressão, incluindo o valor
            # exibido na entrada e o resultado apresentado
            try:
                result = eval(self.expr + self.entry.get())
                self.entry.delete(0, END)
                if result % 1 == 0:
                    self.entry.insert(END, int(result))
                else:
                    self.entry.insert(END, result)
                self.expr = ''
            except:
                self.entry.delete(0, END)
                self.entry.insert(END, 'Error')
            self.startOfNextOperand = True
        elif key in '+*-/':
            # acrescenta operador exibido na entrada e tecla de
            # operador à expressão e prepara novo operando
            self.expr += self.entry.get()
            self.expr += key
            self.startOfNextOperand = True
        elif key == '+-':
            # troca entrada de positiva para negativa ou vice-versa
            # se não houver valor de entrada, não faz nada
            try:
                if self.entry.get()[0] == '-':
                    self.entry.delete(0)
                else:
                    self.entry.insert(0, '-')
            except IndexError:
                pass
        elif key == 'C':
            self.memory = 0
            self.entry.delete(0, END)
            self.entry.insert(END, '0')
        elif key == 'M+':
            self.memory = eval(self.entry.get())
            self.startOfNextOperand = True
        elif key == 'MR':
            self.entry.delete(0, END)
            self.entry.insert(0, self.memory)
            self.startOfNextOperand = True
        elif key == 'M-':
            if self.entry.get() == '0':
                pass
            else:
                self.memory -= eval(self.entry.get())
                self.startOfNextOperand = True
        elif key == 'MC':
            self.memory = 0
            self.startOfNextOperand = True
        elif key == '\u221a':
            if self.entry.get() == '0':
                pass
            else:
                try:
                    result = eval(self.entry.get()) ** 0.5
                    self.entry.delete(0, END)
                    if result % 1 == 0:
                        self.entry.insert(END, int(result))
                    else:
                        self.entry.insert(END, result)
                    self.startOfNextOperand = True
                except:
                    self.entry.delete(0, END)
                    self.entry.insert(END, 'Error')
                    self.startOfNextOperand = True
        elif key == 'x\u00b2':
            if self.entry.get() == '0':
                pass
            else:
                try:
                    result = eval(self.entry.get()) ** 2
                    self.entry.delete(0, END)
                    self.entry.insert(END, result)
                    self.startOfNextOperand = True
                except:
                    self.entry.delete(0, END)
                    self.entry.insert(END, 'Error')
                    self.startOfNextOperand = True
        else:
            # insere dígito ao final da entrada, ou como primeiro
            # dígito, se início do próximo operando
            if self.startOfNextOperand:
                self.entry.delete(0, END)
                self.startOfNextOperand = False
            if self.entry.get() == '0':
                self.entry.delete(0, END)
            self.entry.insert(END, key)
