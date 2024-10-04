from carrinho import Carrinho
from roupa import Roupa

class Cliente:
    def __init__(self, nome, carrinho):
        self.nome = nome
        carrinho = carrinho


    def addRoupaCarrinho(self, carrinho, roupa):
        carrinho.addRoupas(roupa)
        print('dnkjwnkwj')

    def removerRoupaCarrinho(self, roupa, carrinho):
        carrinho.removerRoupa(roupa)
    
    def mostrarCarinho(self, carrinho):
        #print(f'o carrinho de {self.nome} tem as seguintes roupas:')
        carrinho.mostrarroupasCarrinho()


if __name__ == '__main__':
    carrinho1 = Carrinho()
    vestido = Roupa('vestido', 'lilas', 33, 45.55)
    blusa = Roupa('blusa', 'blue', 22, 22)
    c1 = Cliente('emanuelly', carrinho1)
    c1.addRoupaCarrinho(carrinho1, vestido)
    c1.addRoupaCarrinho(carrinho1, blusa)
    c1.mostrarCarinho(carrinho1)
    maria= Cliente()




        


        