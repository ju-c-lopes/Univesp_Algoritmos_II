from pessoa import Pessoa
from fila import Fila
import time
agora = time.localtime()


class Cliente(Pessoa):
    def __init__(self, nome, idade, senha=0):
        super().__init__(nome, idade)
        self.senha = senha


class Caixa:
    def __init__(self):
        self.fila_prioritario = Fila()
        self.fila_normal = Fila()
        self.aberto = False
        self.prio = 0

    def abrir_caixa(self):
        if 9 < agora.tm_hour < 21:
            self.aberto = True
        else:
            self.aberto = False

    def pegar_senha(self):
        if self.aberto:
            pessoa = Cliente(input('Nome: '), int(input('Idade: ')))
            if pessoa.idade > 60:
                pessoa.senha = self.fila_prioritario.data[-1].senha + 1\
                    if not self.fila_prioritario.empty() else 1
                self.fila_prioritario.inserir(pessoa)
                for i in range(len(self.fila_prioritario.data)):
                    print(f'Senha Prioritária n° {self.fila_prioritario.data[i].senha}: '
                          f'{self.fila_prioritario.data[i].nome}')
                    print('=' * 50)
                    print('PARA ENTRAR NA FILA DIGITE: caixa.pegar_senha()')
            else:
                pessoa.senha = self.fila_normal.data[-1].senha + 1\
                    if not self.fila_normal.empty() else 1
                self.fila_normal.inserir(pessoa)
                for i in range(len(self.fila_normal.data)):
                    print(f'Senha Normal n° {self.fila_normal.data[i].senha}: '
                          f'{self.fila_normal.data[i].nome}')
                    print('=' * 50)
                    print('PARA ENTRAR NA FILA DIGITE: caixa.pegar_senha()')

    def atender(self):
        if self.prio < 2 and not self.fila_prioritario.empty():
            self.prio += 1
            sua_vez = self.fila_prioritario.remover()
            print(f'\n====SENHA PRIO {sua_vez.senha}=====\n\n{sua_vez.nome}\n')
            print('=' * 50)
            print('PARA ENTRAR NA FILA DIGITE: caixa.pegar_senha()')
        elif not self.fila_normal.empty():
            if self.prio == 2:
                self.prio = 0
            sua_vez = self.fila_normal.remover()
            print(f'\n====SENHA NORMAL {sua_vez.senha}=====\n\n{sua_vez.nome}\n')
            print('=' * 50)
            print('PARA ENTRAR NA FILA DIGITE: caixa.pegar_senha()')
        else:
            print('AGUARDANDO CLIENTES...')


caixa = Caixa()
caixa.abrir_caixa()

print('=' * 50)
print('PARA ENTRAR NA FILA DIGITE: caixa.pegar_senha()')
