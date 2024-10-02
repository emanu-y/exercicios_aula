from funcionario import FUncionario
from departamento import Departamento


class Empresa:
    def __init__(self):
        self.departamentos = []

    def addDep(self, departamento):
        self.departamentos.append(departamento)
        print('dEPARTAMETNO CADASTRADO ')



if __name__ == '__main__':
    empresa = Empresa()
    departamento1 = Departamento('Pesquisa') 
    empresa.addDep(departamento1)

    f1 = FUncionario('emanu', 'pesquisadora', 5000)
    departamento1.addFuncionario(f1)
    f1.informacoesFuncionario()
    
    f1.Salario()
    f1.setSalario(6000)
    
