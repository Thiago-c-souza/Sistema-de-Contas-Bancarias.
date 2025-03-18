

class ContaBancaria:
    def __init__(self, titular, saldo = 0):
        self.titular = titular
        self.saldo = saldo if saldo >= 0 else 0

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f"✅ Depósito de R$ {valor:.2f} realizado com sucesso!")
        else:
            print("⚠ O valor do depósito deve ser maior que zero.")
    
    def sacar(self, valor):
        if 0 < valor <= self.saldo:
            self.saldo -= valor
            print(f"✅ Saque de R$ {valor:.2f} realizado com sucesso!")
        else:
            print("⚠ Saldo insuficiente ou valor inválido para saque.")
    
    def exibir_saldo(self):
        print(f"💰 Saldo atual: R$ {self.saldo:.2f}")

Teste = ContaBancaria('Thiago')

Teste.exibir_saldo()
        


