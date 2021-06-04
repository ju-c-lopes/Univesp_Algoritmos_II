class Queue2(list):
    """Uma classe de fila, subclasse de list"""

    def is_empty(self):
        """Retorna True se fila vazia, False caso contrário"""
        return len(self) == 0

    def dequeue(self):
        """Remove e retorna item na frente da fila"""
        return self.pop(0)

    def enqueue(self, item):
        """Insere item no final da fila"""
        return self.append(item)
