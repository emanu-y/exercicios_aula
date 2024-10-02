from livro import Livro

class Pedido:
    def __init__(self, cliente, quantidade ):
        self.cliente = cliente 
        self.livros = []
        self.quantidade = quantidade


    def getClinete(self):
        return self.cliente
    
    def ADDLIvro(self, livro):
        if livro == livro.getTitulo():
           if self.quantidade <= livro.getEstoque():
             self.livros.append(livro)
             livro.setEstoque(livro.getEstoque - self.quantidade)
           else:
                return f'Temos somente {livro.getEstoque()} disponovel'
        else:
             return 'Livro nao escontrado'


    def somarCompra(self)            
    
    def compra(self, pagamento):
            for livro in self.livros:
                sum(livro.getPeco) 

            if pagamento >= sum(livro.getPreco):
                if pagamento > sum(livro.getPreco):
                    troco = pagamento - sum(livro.getPreco)
                    return f'Seu troco é {troco}'
                return 'Pagamento relizado'
            else:
                return 'Valor insuficiente'
            




if __name__ == "__main__":
    livro1 = Livro('lalal', 'jkdnwd', 87.00, 8)
    pedido1= Pedido('eu', 5)
    pedido1.ADDLIvro(livro1)
    pedido1.compra(100)


