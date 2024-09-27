class Cliente :
    def __init__(self, nome):
        self.nome = nome
        self.contas = []

    def getNome(self):
        return self.nome
    
    def addConta(self, conta):
        self.contas.append(conta)

    def exibirContas(self):
        print(f"As contas de {self.nome} são:")
        for conta in self.contas:
            print(f"Conta: {conta.getNumeroConta()} Saldo: R${ conta.exibirSaldo()}")
           
    