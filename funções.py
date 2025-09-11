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
