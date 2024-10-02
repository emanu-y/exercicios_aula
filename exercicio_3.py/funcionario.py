class FUncionario:
    def __init__(self, nome, cargo, salario):
        self.nome = nome 
        self.cargo = cargo 
        self.__salario = salario 

    def informacoesFuncionario(self):
        print(f'Nome: {self.nome}. Cargo: {self.cargo}')

    def getNome(self):
        return self.nome

    def Salario(self):
       print(f'A {self.nome} recebe {self.__salario}')
    
    def setSalario(self, salarioAtualizado):
        print(f'O salario da funcionaria(o) {self.nome} foi modificado de {self.__salario} para {salarioAtualizado}')
        self.__salario = salarioAtualizado