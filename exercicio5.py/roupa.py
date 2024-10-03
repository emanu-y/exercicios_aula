class Roupa:
    def __init__(self, tipo, cor, tamanho, preco):
        self.tipo = tipo
        self.color = cor 
        self.__tamanho = tamanho 
        self.__preco = preco

    def getTipo(self):
      return self.tipo
    #   print(self.tipo) *forma errada de se fazer, porque aparece o none abaixo do nome
2
        