import random


class MyList(list):  # list é a estensão de list para a classe MyList, ou seja, MyList herda atributos de list

    def choice(self):
        return random.choice(self)
