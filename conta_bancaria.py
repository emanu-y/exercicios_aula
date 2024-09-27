from clienteBanco.cliente import Cliente

class ContaBancaria:
    def __init__(self, saldo_inicial, numeroConta):
        self.__saldo = saldo_inicial
        self.__numeroConta = numeroConta

    def getNumeroConta(self):
        return self.__numeroConta


    def depositar(self, valor):
        self.__saldo += valor
        print(f"depositou {valor}")

    def sacar(self, valor):
        if valor <= self.__saldo:
         self.__saldo -= valor
         print(f'{valor} sacaado.')
        else:
            print('Saldo insuficiente.')


    def exibirSaldo(self):
        return self.__saldo
    
if __name__ == "__main__":
    
    # c2 = Cliente('huidh')
    # conta1 = ContaBancaria(0, '82978397')
    # conta1.depositar(100)
    # conta1.exibirSaldo()
    # conta1.
    
    #  c1 =Cliente("Emanuelly")
    #  conta1 = ContaBancaria(55, '7834678')
    # # c1.addConta(conta1)
    # # conta1.depositar(20)
    # # c1.exibirContas()
    # # conta1.sacar(100)
    # # conta1.exibirSaldo()
    # # c1.exibirContas()

    for i in range(0,7):
        print(f"ola {i}")


    
   




   

    

