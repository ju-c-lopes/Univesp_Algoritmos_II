"""

# >>> S = "prodA,12,3.8\n"         # string S como virá do arquivo
# >>> S[:-1]                       # remover o"\n" com fatiamento não é a melhor solução
# 'prodA,12,3.8'
# >>> S = "prodA,12,3.8"           # se o "\n" não estiver presente, então
# >>> S[:-1]
# 'prodA,12,3.'                    # o último caractere será removido indevidamente
#
# >>> S = "prodA,12,3.8\n"         # essa solução é melhor
# >>> S.rstrip()                   # o "\n" foi removido
#
# >>> L = S.split(",")             # separa S em uma lista de strings usando "," como delimitador
# >>> L
# ['prodA', '12', '3.8']           # lista produzida
#
# >>> L[1], L[2] = int(L[1]), float(L[2])        # converte L[1] e L[2]
# >>> L                                          # para int e float, respectivamente
# ['prodA', 12, 3.8]

"""