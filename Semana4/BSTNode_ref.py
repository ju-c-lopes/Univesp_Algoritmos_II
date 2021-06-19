class BSTNode(object):
    """
    os parâmetros left e right são as referências a outros nós,
    o campo key guarda a chave utilizada para identificar o nó
    e value representa o valor que desejamos armazenar nele
    """
    def __init__(self, key, value=None, left=None, right=None):
        self.key = key
        self.value = value
        self.left = left
        self.right = right

    def get(self, key):
        """Retorna uma referência ao nó de chave key"""
        if self.key == key:
            return self
        node = self.left if key < self.key else self.right
        if node is not None:
            return node.get(key)

    def add(self, key):
        """Adiciona elemento à subárvore"""
        side = 'left' if key < self.key else 'right'
        node = getattr(self, side, BSTNode(key))
        if node is None:
            setattr(self, side, BSTNode(key))
        else:
            node.add(key)

    def remove(self, key):
        if key < self.key:
            self.left = self.left.remove(key)
        elif key > self.key:
            self.right = self.right.remove(key)
        else:
            # encontramos o elemento, então vamos removê-lo!
            if self.right is None:
                return self.left
            if self.left is None:
                return self.right
            # ao invés de remover o nó, copiamos os valores do nó substituto
            tmp = self.right.find_min()
            self.key, self.value = tmp.key, tmp.value
            self.right.remove_min()
        return self

    def find_min(self):
        """Retorna o menor elemento da subárvore que tem self como raíz."""
        if self.left is None:
            return self
        else:
            return self.left.find_min()

    def remove_min(self):
        """Remove o menor elemento da subárvore que tem self como raíz."""
        if self.left is None:  # encontrou o min, daí pode rearranjar
            return self.right
        self.left = self.left.remove_min()
        return self
