import os
from funções import *

while True:
    try:
        os.system("cls")
        print("BEM-VINDO(a) AO SISTEMA DE LOCADORA")
        print("Qual opção você deseja?")
        print("1 - Cadastrar Cliente")
        print("2 - Cadastrar Item")
        print("3 - Listar Clientes")
        print("4 - Listar Itens")
        print("5 - Alugar Item")
        print("6 - Devolver Item")
        print("0 - Sair")
        escolha = int(input(" "))

        match escolha:
            case 1:
                cadastro_cliente()
            case 2:
                cadastro_item()
            case 3:
                
                listar_clientes()
            case 4:
                listar_itens()
            case 5:
                alugar_item()
            case 6:
                devolver_item()
            case 0:
                print("Saindo...")
                os.system("pause")
                break
            case _:
                print("Opção inválida!")
                os.system("pause")

    except Exception as e:
        print(f"Ocorreu um erro, tente novamenet! Erro: {e}")
        os.system("pause")

