import json

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

def salvar_contas(contas):
    with open("contas.json", "w") as arquivo:
        json.dump([conta.__dict__ for conta in contas], arquivo, indent=4)

def carregar_contas():
    try:
        with open("contas.json", "r") as arquivo:
            contas_dados = json.load(arquivo)
            return [ContaBancaria(**conta) for conta in contas_dados]
    except FileNotFoundError:
        return []
    
contas = carregar_contas()

nova_conta = ContaBancaria("Thiago", 100)
contas.append(nova_conta)
salvar_contas(contas)



