m = dict()  # coleção de dicionário 'm' armazena os valores já calculados do fatorial


def fat(n):
    if n == 0:
        return 1
    elif m.get(n) is not None:  # verifica se fatorial de 'n' já foi calculado e está na coleção 'm'
        return m[n]
    else:                       # caso não esteja, então é feito o cálculo recursivo
        m[n] = n * fat(n-1)
        return m[n]
