from funcionario import FUncionario

class Departamento:
    def __init__(self, departamento):
        self.departamento = departamento
        self.funcionarios = []

    
    def nomeDep(self):
        return self.departamento
    

    def addFuncionario(self, funcionario):
        self.funcionarios.append(funcionario)
        print(f'O funcionario {funcionario.getNome()} foi adicioando ao departamento {self.departamento}')


    def mostrarFuncionarios(self):
        print(f'os funcionarios do departamento {self.departamento} são:s')
        for funcionario in self.funcionarios:
            return funcionario.getNome()

