class ContaBancaria:
    """Simula uma conta de banco"""

    def __init__(self, deposito=0):
        """A abertura da conta com o valor do depósito ou 0"""
        self.saldo = deposito

    def saque(self, saque):
        """Simula o saque de dinheiro"""
        self.saldo -= saque
        return f"Saque de ${saque} realizado com sucesso, seu saldo está em ${self.saldo}"

    def deposito(self, deposito):
        """Simula o depósito na conta"""
        self.saldo += deposito
        return f"Depósito de ${deposito} feito com sucesso, seu novo saldo é de ${self.saldo}"

    def consultar_saldo(self):
        """Retorna o saldo da conta"""
        return f"${self.saldo}"
