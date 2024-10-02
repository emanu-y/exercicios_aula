from funcionario import FUncionario

class Departamento:
    def __init__(self, departamento):
        self.departamento = departamento
        self.funcionarios = []

    
    def nomeDep(self):
        return self.departamento
    

    def addFuncionario(self, funcionario):
        self.funcionarios.append(funcionario)
        print(f'O funcionario {funcionario} foi adicioando ao departamento {self.nome}')


    def mostrarFuncionarios(self):
        print(f'os funcionarios do departamento {self.departamento} são:s')
        for funcionario in self.funcionarios:
            return funcionario

