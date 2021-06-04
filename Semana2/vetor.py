from class_Point import Point


class Vetor(Point):
    """representa um vetor usando atributos e métodos da classe Point"""

    def __add__(self, other):
        self.x += other.x
        self.y += other.y
        return Vetor(self.x, self.y)

    def __mul__(self, other):
        self.x *= other.x
        self.y *= other.y
        produto = self.x + self.y
        return produto

    def __repr__(self):
        """apresentará o obejto vetor como um vetor e não como um ponto"""
        return 'Vetor({}, {})'.format(self.x, self.y)
