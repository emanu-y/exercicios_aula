class Livro:
    def __init__(self, titulo, autor, preco, estoque):
        self.titulo = titulo
        self.autor = autor 
        self.__preco = preco
        self.__estoque = estoque


    def getTitulo(self):
        return self.titulo
    
    def getAutor(self):
         return self.titulo
   
    def verificarPreço(self):
         print(f'Livro: {self.titulo} Preço: R${self.__preco} Em estoque: {self.__estoque}')
         
        

