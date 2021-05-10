class Retangulo:
    """Objeto que representa um retângulo com suas devidas medidas"""

    def setTamanho(self, largura, comprimento):
        """Define a largura e o comprimento do retângulo"""
        self.largura = largura
        self.comprimento = comprimento

    def perimetro(self):
        """Retorna o valor do perímetro de um dado retângulo"""
        return 2 * (self.largura + self.comprimento)

    def area(self):
        """Retorna a área de um dado retângulo"""
        return self.largura * self.comprimento
