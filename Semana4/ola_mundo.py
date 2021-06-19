"""
Exemplo de funcionamento de pilha:

Onde a função olamundo() chama a função ola() que fica no topo da pilha
printa a string 'olá, ' e chama a próxima função mundo() que, por fim,
imprime a string 'mundo!', completando a frase 'olá mundo'
"""


def ola():
    print('olá, ', end='')
    mundo()


def mundo():
    print('mundo!')


def olamundo():
    ola()


olamundo()
