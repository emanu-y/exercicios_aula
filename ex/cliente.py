class Cliente :
    def __init__(self, nome, conta):
        self.nome = nome
        self.conta = conta

    def getNome(self):
        return self.nome
    
    def getConta(self):
        return self.contas