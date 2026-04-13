from    Cliente    import Cliente
#       arquivo.py        o nome da nossa classe
import pandas as pd

caminho_excel = "cliente_banco_tabajara.xlsx"

print("================================================")
print("Digite as seguintes informações: ")
print("1 > Criar conta ")
print("2 > Acessar conta ")
print("================================================\n")
opcao = int(input("R: "))

if opcao == 1:
    print("Opção 1 selecionada")
    nome_cliente = str(input("Digite o seu nome: "))
    cpf = float(input("Digite seu CPF: "))
    tipo_conta = str(input("Digite seu tipo de conta: "))
    numero_conta = 0
    agencia = 400
    extrato_bancario = 0

    # Instancio o cliente
    cliente = Cliente(nome_cliente, cpf, tipo_conta, numero_conta, agencia, extrato_bancario)

    dados = {
            "nome_cliente": [cliente.nome_cliente],
            "cpf": [cliente.cpf],
            "tipo_conta": [cliente.tipo_conta],
            "numero_conta": [cliente.numero_conta],
            "agencia": [cliente.agencia],
            "extrato_bancario": [cliente.extrato_bancario]
        }

    excel = pd.DataFrame(cliente)
    excel.to_excel(caminho_excel, index=False)

elif opcao == 2:
    print("Opção 2 selecionada")