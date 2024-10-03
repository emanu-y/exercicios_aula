from carro import Carro
from cliente import Cliente

class Agencia:
    def __init__(self):
        self.carros = []


    def addCarros(self, carro):
        self.carros.append(carro)
        print('carro adicionado')

    def alugarCArro(self, carro):
        if carro in self.carros:
            if carro.getStatus() == True:
                carro.setStatus(False)
                print(f'aligou carro')
            else: 
               print('carro nao disponivel')
        else: 
            print('Carro nao encontrado')


    def devolverCarro(self, carro):
        carro.setStatus(True)
        print('carro devolvido')



if __name__ == '__main__':
    agencia = Agencia()
    c1 = Carro('conversivel', 'fiat', 8494894)
    agencia.addCarros(c1)




