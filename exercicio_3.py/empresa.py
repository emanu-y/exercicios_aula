from funcionario import FUncionario
from departamento import Departamento


class Empresa:
    def __init__(self):
        self.departamentos = []

    def addDep(self, departamento):
        self.departamentos.append(departamento)



if __name__ == '__main__':
    pass
