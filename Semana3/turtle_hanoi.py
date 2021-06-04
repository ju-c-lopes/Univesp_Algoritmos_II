from turtle import Turtle, Screen
from hanoi import hanoi


class Disk(Turtle):
    """
    Uma classe de disco de Torre de Hanói
    _____________________________________

    Métodos definidos aqui:

    __init__(self, n)
        Inicializa disco n
    """

    def __init__(self, n):
        """Inicializa disco n"""
        Turtle.__init__(self, shape='square', visible=False)
        self.penup()                        # movimentos não devem ser traçados
        self.sety(300)                      # movimentos são acima dos pinos
        self.shapesize(1, 1.5 * n, 2)       # define diâmetro do disco
        self.fillcolor(1, 1, 1)             # disco é branco
        self.showturtle()                   # disco se torna visível


class Peg(Turtle, list):
    """
    Classe de pino da torre de Hanói, herda de Turtle e list
    ________________________________________________________

    __init__(self, n)
        Inicializa um pino para n discos

    pop(self)
        Remove o disco de cima do pino e o retorna

    push(self, disk)
        coloca o disco no pino
    """
    pos = -200                              # coordenada x do próximo pino

    def __init__(self, n):
        """Inicializa um pino para n discos"""

        Turtle.__init__(self, shape='square', visible=False)
        self.penup()                        # movimentos de pino não devem ser traçados
        self.shapesize(n * 1.25, .75, 1)    # altura do pino é função do número de discos
        self.sety(12.5 * n)                 # fundo do pino é y = 0
        self.x = Peg.pos                    # coordenada x do pino
        self.setx(self.x)                   # pino movido para sua coord. x
        self.showturtle()                   # pino se torna visível
        Peg.pos += 200                      # posição do próximo pino

    def push(self, disk):
        """Coloca disco em torno do pino"""

        disk.setx(self.x)                   # move disco para coord. x do pino
        disk.sety(10 + len(self) * 25)      # move disco verticalmente para logo acima do disco mais no topo do pino
        self.append(disk)                   # acrescenta disco ao pino

    def pop_disk(self):
        """Remove disco do topo do pino e o retorna"""

        disk = self.pop()                   # remove disco do pino
        disk.sety(300)                      # levanta disco para acima do pino
        return disk


def play(n):
    """Mostra a solução do problema da TOrre de Hanói com n discos"""
    screen = Screen()
    Peg.pos = -200
    p1 = Peg(n)
    p2 = Peg(n)
    p3 = Peg(n)

    for i in range(n):                      # discos são colocados em torno do pino 1
        p1.push(Disk(n-i))                  # em ordem decrescente de diâmetro

    hanoi(n, p1, p2, p3)

    screen.bye()
