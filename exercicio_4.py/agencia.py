
from carro import Carro
class Agencia:
    def __init__(self):
        self.carros = []


    def addCarros(self, carro):
        self.carros.append(carro)
        print('carro adicionado')

    def getCarros(self):
        return self.carros
    


    # def alugarCArro(self, carro):
    #     if carro in self.carros:
    #         if carro.getStatus() == True:
    #             carro.setStatus(False)
    #             print(f'aligou carro')
    #         else: 
    #            print('carro nao disponivel')
    #     else: 
    #         print('Carro nao encontrado')


    # def devolverCarro(self, carro):
    #     carro.setStatus(True)
    #     print('carro devolvido')







