class Animal:
    """representa um animal"""
    def __init__(self, especie='animal', linguagem='emitir sons'):
        """Inicializa um animal com sua espécie e forma de emitir sons"""
        self.especie = especie
        self.linguagem = linguagem

    def set_especie(self, especie):
        """define a espécie do animal"""
        self.especie = especie

    def set_linguagem(self, linguagem):
        """define a linguagem do animal"""
        self.linguagem = linguagem

    def fala(self):
        """exibe uma sentença pelo animal"""
        print('Eu sou um {} e sei {}'.format(self.especie, self.linguagem))
