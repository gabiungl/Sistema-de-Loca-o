import os
from classes import *

locadora = Locadora("Locadora Senai")
codigo_item = 0


def cadastro_cliente():
    os.system("cls")
    print(" Cadastro de Cliente")
    nome = input("Nome: ")
    cpf = input("CPF: ")
    match nome, cpf:
        case _:
            print("Opção inválida!")
            os.system("pause")

    cliente = Cliente(nome, cpf)
    locadora.cadastrarCliente(cliente)
    print("Cliente cadastrado com sucesso!")
    os.system("pause")
