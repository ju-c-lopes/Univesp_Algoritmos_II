from class_Animal import Animal


class Ave(Animal):
    """Representa uma ave"""

    def fala(self):
        """Exibe sons de ave"""
        print('{}! '.format(self.linguagem) * 3)
