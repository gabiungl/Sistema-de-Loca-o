import os
from classes import *

locadora = Locadora()

def cadastro_cliente():
    os.system("cls")
    print(" Cadastro de Cliente")
    try:
        nome = input("Nome: ")
        cpf = input("CPF: ")
    except Exception:
        print("Erro na entrada de dados!")
        os.system("pause")
        return

    cliente = Cliente(nome, cpf)   
    locadora.cadastrarCliente(cliente)
    print(f"Cliente [{cliente.idCliente()}] cadastrado com sucesso!")
    os.system("pause")

def cadastro_item():
    os.system("cls")
    print("Cadastro de Item")
    print("1 - Filme")
    print("2 - Jogo")
    try:
        escolha = int(input("--> "))
        match escolha:
            case 1:
                titulo = input("Título: ")
                genero = input("Gênero: ")
                duracao = int(input("Duração (min): "))
                filme = Filme(titulo, genero, duracao)
                locadora.cadastrarItem(filme)
                print("Filme cadastrado com sucesso!")
            case 2:
                titulo = input("Título: ")
                plataforma = input("Plataforma: ")
                faixa = input("Faixa etária: ")
                jogo = Jogo(titulo, plataforma, faixa)
                locadora.cadastrarItem(jogo)
                print("Jogo cadastrado com sucesso!")
            case _:
                print("Opção inválida!")
    except Exception as e:
        print(f"Erro: {e}")
    os.system("pause")


def listar_clientes():
    os.system("cls")
    print(" Clientes Cadastrados")
    for clie in locadora.listarClientes():
        print(f"[{clie.idCliente()}] Nome: {clie.nome()}")
    os.system("pause")
import os

def listar_itens():
    os.system("cls")
    print(" Itens Cadastrados ")
    for itens in locadora.listarItens():
        match itens.estado():
            case True:
                status = "Disponível"
            case False:
                status = "Indisponível"
        print(f"[{itens.idItem()}] {itens.titulo()} - {status}")
    os.system("pause")

def alugar_item():
    while True:
        try:
            print("-Alugar-")
            print("\nClientes cadastrados:")
            count = 1
            for cliente in locadora.listarClientes():
                print(f"ID:{count} \nNome: {cliente.nome()} \nCPF: {cliente.cpf()}")
                count += 1

            print("\nItens disponíveis:")
            count = 1
            for item in locadora.listarItens():
                status = "Disponível" if item.estado() else "Alugado"
                print(f"ID:{count} \nTítulo: {item.titulo()} \nStatus: {status}")
                count += 1

            cliente_id = int(input("\nDigite o ID do cliente: "))
            item_id = int(input("Digite o ID do item: "))

            cliente = locadora.listarClientes()[cliente_id - 1]
            item = locadora.listarItens()[item_id - 1]

            match item.estado():
                case True:
                    cliente.alugar(item)
                    print(f"{cliente.nome()} alugou {item.titulo()}")
                case False:
                    print("Esse item já está alugado")


            os.system("pause")
            break

        except Exception as e:
            print(f"Ocorreu um erro inesperado: {e}")
            os.system("pause")
  

def devolver_item():
    while True:
        try:
            print("-Devolver-")
            print("Clientes cadastrados:")
            count = 1
            for cliente in locadora.listarClientes():
                print(f"ID:{count} \nNome: {cliente.nome()}")
                count += 1

            print("\nItens:")
            count = 1
            for item in locadora.listarItens():
                status = "Disponível" if item.estado() else "Alugado"
                print(f"ID:{count} \nTítulo: {item.titulo()} \nStatus: {status}")
                count += 1

            cliente_id = int(input("\nDigite o ID do cliente: "))
            item_id = int(input("Digite o ID do item: "))

            cliente = locadora.listarClientes()[cliente_id - 1]
            item = locadora.listarItens()[item_id - 1]

            match item in cliente._itens:
                case True:
                    cliente.devolver(item)  
                case False:
                    print(f"O cliente {cliente.nome()} não tem esse item alugado.")

            os.system("pause")
            break

        except Exception as e:
            print(f"Ocorreu um erro inesperado: {e}")
            os.system("pause")
