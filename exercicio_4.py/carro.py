class Carro:
    def __init__(self, modelo, marca, quilometragem):
        self.modelo = modelo
        self.marca = marca 
        self.__quilometragem = quilometragem
        self.__disponivel = True


    def getStatus(self):
        return self.__disponivel
    
    def setStatus(self, status):
        self.__disponivel = status