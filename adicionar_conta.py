from Cliente import Cliente 
import pandas as pd

class adicionar_conta:
    def __init__(self, nome_cliente, cpf, tipo_conta):

        numero_conta = 0
        agencia = 400
        extrato_bancario = 0

        # Criando molde da classe cliente para manipular dados digitados pelo usuario
        self.cliente = Cliente(nome_cliente, cpf, tipo_conta, numero_conta, agencia, extrato_bancario)

    def adiconar(self, caminho_excel):
        nova_linha = len(caminho_excel) # <- visão da nova linha do excel
        ultima_linha = caminho_excel.iloc[-1]

        dados_cliente = {
            "nome_cliente": [self.cliente.nome_cliente],
            "cpf": [self.cliente.cpf],
            "tipo_conta": [self.cliente.tipo_conta],
            "numero_conta": ultima_linha["numero_conta"] + 1,
            "agencia": ultima_linha["agencia"] + 1,
            "extrato_bancario": [self.cliente.extrato_bancario],
            }

        novo_dado = pd.DataFrame(dados_cliente)
        return novo_dado 