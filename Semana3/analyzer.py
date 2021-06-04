import random
import time


def timing(func, n):
    """Roda func sobre entrada retornada por build_input"""
    func_input = build_input(n)  # obtém entrada para func

    start = time.time()         # toma hora inicial
    func(func_input)            # roda func sobre func_input
    end = time.time()           # toma hora final
    return end - start          # retorna tempo de execução

"""
função utilizada para testar a função Fibonacci

def build_input(entry):
    "Retorna entrada para funções de Fibonacci"
    return entry
"""

"""
função utilizada para testar a função power

def build_input(n):
    "Retorna uma amostra aleatória de n números no intervalo [0, 2n]"
    lst = random.sample(range(2 * n), n)
    lst.sort()
    return lst
"""


def build_input(n):
    """Retorna um alista de inteiros aleatórios no intervalo [0, n**2]"""
    res = []
    for i in range(n):
        res.append(random.choice(range(n**2)))
    return res


def timing_analysis(func, start, stop, inc, runs):
    """
    Exibe tempos de execução médios da função sobre entradas
    de tamanho start, start+inc, start+2*inc, ... até stop
    """
    for n in range(start, stop, inc):       # para cada tamanho de entrada de tamanho n

        acc = 0.0   # inicializa acumulador
        for i in range(runs):   # repete runs vezes
            acc += timing(func, n)  # roda func sobre entradas de tamanho n e acumula tempos de execução

        # exibe tempos de execução médios para tamanho de entrada n
        format_str = 'Tempo de execução de {}({}) é {:.7f} segundos.'
        print(format_str.format(func.__name__, n, acc/runs))
