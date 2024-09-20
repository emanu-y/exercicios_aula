from ex.cliente import Cliente

class ContaBancaria:
    def __init__(self, conta, saldo_inicial, numeroConta):
        self.conta = conta
        self.saldo = saldo_inicial
        self.numeroConta = numeroConta



    def depositar(self, valor, cliente):
        self.saldo += valor
        print(f"{cliente.getNome} depositou {valor}")

    

