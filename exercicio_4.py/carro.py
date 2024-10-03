class Carro:
    def __init__(self, modelo, marca, quilometragem):
        self.modelo = modelo
        self.marca = marca 
        self.__quilometragem = quilometragem
        self.__disponivel = True



    def get_quilometragem(self):
        return self.__quilometragem
    

    def getStatus(self):
        return self.__disponivel
    
    
    def setStatus(self, status):
        self.__disponivel = status
        
    
    def disponivel(self):
        if self.__disponivel == True:
            print(f"O carro {self.modelo} esta disponivel")
        else:
            print(f'O carro {self.modelo} nao esta disponivel')