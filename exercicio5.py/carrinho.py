from roupa import Roupa
class Carrinho:
    def __init__(self):
        self.roupas = []

    def addRoupas(self,roupa):
        self.roupas.append(roupa)

    def removerRoupa(self, roupa):
        self.roupas.remove(roupa)

    def mostrarroupasCarrinho(self):
        for roupa in self.roupas:
            print(roupa.getTipo())