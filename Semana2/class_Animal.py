class Animal:
    """representa um animal"""
    def __init__(self, especie='animal', linguagem='emitir sons', idade=0):
        """Inicializa um animal com sua espécie e forma de emitir sons"""
        self.especie = especie
        self.linguagem = linguagem
        self.idade = idade

    def set_especie(self, especie):
        """define a espécie do animal"""
        self.especie = especie

    def set_linguagem(self, linguagem):
        """define a linguagem do animal"""
        self.linguagem = linguagem

    def set_idade(self, idade):
        """Define a idade do animal"""
        self.idade = idade

    def get_idade(self):
        return self.idade

    def fala(self):
        """exibe uma sentença pelo animal"""
        print('Eu sou um {} e sei {}'.format(self.especie, self.linguagem))
