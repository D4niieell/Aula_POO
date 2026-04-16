from Cliente import Cliente
#    arquivo.py    o nome da nossa classe
from Criar_conta import Criar_conta
from adicionar_conta import adicionar_conta
import pandas as pd
import os

caminho_excel = "cliente_banco_Tabajara.xlsx"

print("================================================")
print("                 BANCO TABAJARA")
print("                                 ")
print("                 Escolha uma opção")
print("                 1 - Criar conta")
print("                 2 - Acessar conta")
print("================================================\n")
opcao = int(input("R: "))

if opcao == 1:
    print("Opcao 1 selecionada")
    nome_cliente = str(input("Nome completo: "))
    cpf = int(input("CPF: "))
    tipo_conta  = str(input("Tipo da conta que deseja criar:  "))

    df = pd.DataFrame()
    
    if os.path.exists(caminho_excel): # true
        print("Arquivo ja existe")
        df = pd.read_excel(caminho_excel)

        # Instanciando o adicionar Conta
        adicionar = adicionar_conta(nome_cliente, cpf, tipo_conta)

        # Chamando função adicionar que está dentro da classe Adicionar_conta
        novo_dado = adicionar.adiconar(df)

    else: # false
        print("Arquivo nao existe")


        # Instancio para manipular os dados adicionados pelo cliente
        conta = Criar_conta(nome_cliente, cpf, tipo_conta)

        # Identifico o caminho do excel e chamo a funcao salvar_excel
        novo_dado = conta.salvar_excel(caminho_excel)

    #Concat para inserir uma nova linha no excel com os dados digitados pelo usuario
    df = pd.concat([df, novo_dado], ignore_index=True)

    df.to_excel(caminho_excel, index=False)

    print()
    

elif opcao == 2:
    print("Opcao 2 selecionada")