

class Cliente:
    def __init__(self, nome):
        self.nome = nome
       

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

  
