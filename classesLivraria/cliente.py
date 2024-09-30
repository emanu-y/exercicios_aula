from livro import Livro
from pedidos import Pedido


class Cliente:
    def __init__(self, nome):
        self.nome = nome 
        self.pedidos = []

    def addPedido(self, pedido):         
        self.pedidos.append(pedido)

    def exibirPedidos(self):
        for pedido in self.pedidos:
            print(f"{pedido.infoPedido()}")
