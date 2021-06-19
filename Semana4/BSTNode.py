# Classe para uma árvore binária de busca
# Obs: ver pfd sobre árvores

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
        if key < self.key:
            return self.left.get(key) if self.left else None
        elif key > self.key:
            return self.right.get(key) if self.right else None
        else:
            return self

    def add(self, node):
        """Adiciona elemento à subárvore"""
        if node.value < self.value:
            if self.left is None:
                self.left = node
            else:
                self.left.add(node)
        else:
            if self.right is None:
                self.right = node
            else:
                self.right.add(node)

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


# a construção de um nó, com chave 42, sem valor armazenado se sem filhos
no_raiz = BSTNode(42)

"""
                                ______
                                | 42 |
                                ------

"""

# Adicionando filhos ao nó 42
no_raiz.left = BSTNode(10)
no_raiz.right = BSTNode(90)

"""
                                ______
                                | 42 |
                                ------
                                /     \
                              /         \
                            /             \
                         ______          ______
                         | 10 |          | 90 |
                         ------          ------

"""

# adicionando um filho esquerdo ao nó recém-criado 10
no_raiz.left.left = BSTNode(2)
"""
                                ______
                                | 42 |
                                ------
                                /     \
                              /         \
                            /             \
                         ______          ______
                         | 10 |          | 90 |
                         ------          ------
                        /
                      /
                    /
                 _____
                 | 2 |
                 -----

OBS: Implementação para didática
"""
