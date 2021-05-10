class Point:
    """Representa pontos no plano cartesiano"""
    def __init__(self, coordx=0, coordy=0):
        """Inicializa as coordenadas x e y"""
        self.x = coordx
        self.y = coordy

    def setx(self, coordx):
        """define a coordenada x do ponto"""
        self.x = coordx

    def sety(self, coordy):
        """define a coordenada y do ponto"""
        self.y = coordy

    def get(self):
        """retorna as coordenadas x"""
        return self.x, self.y

    def move(self, dx, dy):
        """adiciona a quantidade informada aos valores x e y já presentes"""
        self.x += dx
        self.y += dy

    def __eq__(self, other):
        """self == outro quando eles têm as mesmas coordenadas"""
        return self.x == other.x and self.y == other.y

    def __repr__(self):
        """Retorna representação de string canônica Ponto(x, y)"""
        return 'Point({}, {})'.format(self.x, self.y)
