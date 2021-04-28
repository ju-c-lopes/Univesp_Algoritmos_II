"""
Ordenar lista em Python é muito simples, usando sort()
fazemos facilmente essa manobra, porém, com este algoritmo
entendemos como funciona a lógica da ordenação de uma lista
aleatória
"""

print("Ordenação Bolha\n")
L = [17, 4, 23, 8, 19, 12]                                         # poderia ter sido gerada uma lista
print("Lista gerada:", L)                                          # com números aaleatórios com randint()

Trocou = 1                                                         # flag que indica se houve troca ou não
while Trocou:                                                      # enquanto trocou é diferente de zero
    Trocou = 0                                                     # faça Trocou = 0
    i = 0
    while i < len(L)-1:                                            # laço que percorre a lista fazendo
        if L[i] > L[i+1]:                                          #   as trocas quando necessário
            L[i], L[i+1] = L[i+1], L[i]                            # faz a troca
            Trocou = 1                                             # se houve troca então Trocou = 1
        i += 1
    print(" estado parcial de L:", L)
print("\nSituação final")
print("Lista ordenada:", L)
print("Fim do Programa")
