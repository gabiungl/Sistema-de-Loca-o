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

    cliente = Cliente(nome, cpf)   # CORRIGIDO
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


def listar_itens():
    os.system("cls")
    print(" Itens Cadastrados ")
    for itens in locadora.listarItens():
        status = "Disponível" if itens.estado() else "Indisponível"
        print(f"[{itens.idItem()}] {itens.titulo()} - {status}")
    os.system("pause")

def alugar_item():
    os.system("cls")
    print(" Alugar Item ")

    id_cliente = int(input("ID do Cliente: "))
    id_item = int(input("ID do Item: "))

    cliente = None
    item = None

    for clie in locadora.listarClientes():
        if clie.idCliente() == id_cliente:
            cliente = clie
            break

    for ite in locadora.listarItens():
        if ite.idItem() == id_item:
            item = ite
            break

    match (cliente, item, item.estado() if item else None):
        case (None, _, _):
            print("Cliente não encontrado!")
        case (_, None, _):
            print("Item não encontrado!")
        case (_, _, False):
            print(f"{item.titulo()} já está alugado!")
        case (_, _, True):
            cliente.alugar(item)

    os.system("pause")

def devolver_item():    
    os.system("cls")
    print(" Devolver Item ")

    id_cliente = int(input("ID do Cliente: "))
    id_item = int(input("ID do Item: "))

    cliente = None
    item = None

    for clie in locadora.listarClientes():
        if clie.idCliente() == id_cliente:
            cliente = clie
            break

    for ite in locadora.listarItens():
        if ite.idItem() == id_item:
            item = ite
            break

    match (cliente, item):
        case (None, _):
            print("Cliente não encontrado!")
        case (_, None):
            print("Item não encontrado!")
        case _:
            cliente.devolver(item)

    os.system("pause")