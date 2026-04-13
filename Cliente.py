# A evolução de um dicionario ecriação de uma classe
# __init__ Construtor -> Cria um molde dos dados do cliente, o objetivo e conseguir transferir dados por todos os arquivos python
class Cliente: 
    def __init__(self, nome_cliente, cpf, tipo_conta, numero_conta, agencia, extrato_bancario):
        # Atributos 
        self.nome_cliente = nome_cliente
        self.cpf = cpf
        self.tipo_conta = tipo_conta
        self.numero_conta = numero_conta
        self.agencia = agencia
        self.extrato_bancario = extrato_bancario

    def __str__(self):
        return f"Nome: {self.nome_cliente} | CPF: {self.cpf} | Tipo conta: {self.tipo_conta} | Numero conta: {self.numero_conta} | Agencia: {self.agencia} | Extrato Bancario: {self.extrato_bancario} " 
