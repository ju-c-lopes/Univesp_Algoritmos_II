class Queue:
    """representa uma fila, onde quem chega vai pro fim da fila e quem tá no início sai primeiro"""
    def __init__(self, queue=None):
        """Instancia uma lista vazia que conterá os itens da fila"""
        if queue is None:
            self.q = []
        else:
            self.q = queue

    def is_empty(self):
        """Retorna True se a fila estiver vazia, False caso contrário"""
        return len(self.q) == 0

    def enqueue(self, item):
        """Insere item no final da fila"""
        return self.q.append(item)

    def dequeue(self):
        """Remove e retorna item na frente da fila"""
        return self.q.pop(0)

    def get(self):
        return self.q

    def __repr__(self):
        """Representação de string canônica de fila"""
        return '{}'.format(self.q)

    def __eq__(self, other):
        """Retorna True se as filas self e outro tiverem os mesmos itens na mesma ordem"""
        return self.q == other.q

    def __len__(self):
        """Retorna o número de itens da fila"""
        return len(self.q)
