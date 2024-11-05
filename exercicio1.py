class SaldoInsuficienteError(Exception):
    pass

class LimiteExcedidoError(Exception):
    pass

class ContaDestinoInvalidoError(Exception):
    pass


class Conta:
    def __init__(self, titular, saldo=0.0, limite=1000.0):
        self.titular = titular
        self.saldo = saldo
        self.limite = limite

    def depositar(self, valor):
        self.saldo += valor
        print(f'Depositado R$ {valor:.2f} na conta. Saldo atual: R$ {self.saldo:.2f}')
    
    def sacar(self, valor):
        if valor >= self.saldo:
            raise SaldoInsuficienteError("Erro: Saldo insuficiente para realizar o saque.")
        self.saldo -= valor
        print(f'Valor Sacado: R$ {valor:.2f}. Saldo atual: R$ {self.saldo:.2f}')

    def transferir(self, valor, conta_destino):
        if not isinstance(conta_destino, Conta):
            raise ContaDestinoInvalidoError("Erro: Conta de destino inválida.")
        if valor > self.limite:
            raise LimiteExcedidoError("Erro: Valor excedido da conta.")
        if valor > self.saldo:
            raise SaldoInsuficienteError("Erro: Saldo insuficiente para a transferência.")  
        
        self.saldo -= valor
        conta_destino.saldo += valor
        print(f"Transferência de R${valor:.2f} para {conta_destino.titular} realizada com sucesso.\nSaldo atual: R${self.saldo:.2f}")


conta1 = Conta("João", saldo=850)
conta2 = Conta("Maria", saldo=357)

try:
    conta1.depositar(200)
    conta1.sacar(800)  # Deve lançar SaldoInsuficienteError
except (SaldoInsuficienteError, LimiteExcedidoError, ContaDestinoInvalidoError) as e:
    print(e)

try:
    conta1.transferir(900, conta2)  # Deve lançar LimiteExcedidoError
except (SaldoInsuficienteError, LimiteExcedidoError, ContaDestinoInvalidoError) as e:
    print(e)

try:
    conta1.transferir(100, "Conta Inexistente")  # Deve lançar ContaDestinoInvalidaError
except (SaldoInsuficienteError, LimiteExcedidoError, ContaDestinoInvalidoError) as e:
    print(e)

try:
    conta1.transferir(100, conta2)  # Transferência válida
except (SaldoInsuficienteError, LimiteExcedidoError, ContaDestinoInvalidoError) as e:
    print(e)


