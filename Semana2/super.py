class Super:
    """Classe genérica como um método"""
    def metodo(self):  # o método Super
        print('em Super.metodo')


class Herdeiro(Super):
    """classe que herda método"""
    pass


class Substituto(Super):
    """Classe que redefine método"""
    def metodo(self):
        print('em Substituto.metodo')


class Extensor(Super):
    """Classe que estende método"""
    def metodo(self):
        print('iniciando Extensor.metodo')
        Super.metodo(self)
        print('encerrando Extensor.metodo')
