import random


def search(lst, target, i, j):
    """
    Tenta achar target na sublista classificada lst[i:j]
    indice de target é retornado se achado, -1 caso contraário
    """

    if i == j:                      # caso básico: lista vazia
        return -1                   # target não pode estar na lista

    mid = (i + j) // 2              # índice da mediana de l[i:j]

    if lst[mid] == target:          # target é a mediana
        return mid
    if target < lst[mid]:           # busca à esquerda da mediana
        return search(lst, target, i, mid)
    else:                           # busca à direita da mediana
        return search(lst, target, mid + 1, j)


def binary(lst):
    """Escolhe item aleatório na lista lst e roda search() sobre ele"""
    target = random.choice(lst)
    return search(lst, target, 0, len(lst))


def linear(lst):
    """Escolhe item aleatório na lista lst e roda index() sobre ele"""
    target = random.choice(lst)
    return lst.index(target)
