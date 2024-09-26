class Livro:
    def __init__(self, titulo, autor, preco, estoque):
        self.titulo = titulo
        self.autor = autor 
        self.__preco = preco
        self.__estoque = estoque

