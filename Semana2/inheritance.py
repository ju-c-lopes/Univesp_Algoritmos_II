import random


class MyList(list):
    """Uma subclasse de list que implementa o método escolha(choice)"""
    def choice(self):
        """Retorna item da lista escolhida uniformemente de modo aleatório"""
        return random.choice(self)
