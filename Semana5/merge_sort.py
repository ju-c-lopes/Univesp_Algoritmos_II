"""
Também chamado de ordenação por intercalação

idéia básica: "dividir para conquistar"

O vetor a ser ordenado é divido recursivamente
ordenando as partes separadamente e posteriormente juntando-as
em um só vetor

É utilizado um vetor auxiliar para intercalar as partes
"""

# IMPLEMENTAÇÃO         vetor de exemplo: [5, 2, 4, 7, 1, 3, 2, 6]

# Fazemos a função recursiva para dividir a lista a ser ordenada


def merge_sort(v, ini, fim):
    if ini < fim:
        meio = (ini + fim) // 2             # Fazemos a divisão inteira (índices).
        merge_sort(v, ini, meio)            # Chamará a função recursivamente,
                                            # com a primeira metade do vetor
        # -------------------------------------------------------------------------
        merge_sort(v, meio+1, fim)          # Chamará a função recursivamente,
                                            # com a outra metade do vetor
        intercalar(v, ini, meio, fim)
    return v


# Função que unirá tudo de forma ordenada ("CONQUISTAR")


def intercalar(v, ini, meio, fim):
    """
    Será usado dois vetores auxiliares, LEFT e RIGHT
    cada um recebendo sublistas para ir juntando em uma só lista
    """
    left = v[ini:meio+1]                    # o meio + 1 não será incluido
    right = v[meio+1:fim+1]                 # começará do meio + 1 até fim + 1 (último índice)
    """
    A seguir, adicionaremos um valor de 'SENTINELA' para cada
    vetor auxiliar, sendo estes valores mais alto, de forma que nenhum valor
    nos vetores seja maior que ele, afim de evitar que os iteradores sejam
    incrementados além do que precisam
    """
    left.append(999)                        # SENTINELA
    right.append(999)                       # SENTINELA
    i, j = 0, 0
    for k in range(ini, fim+1):
        if left[i] <= right[j]:
            v[k] = left[i]
            i += 1
        else:
            v[k] = right[j]
            j += 1
