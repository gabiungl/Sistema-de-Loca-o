import os
from classes import *

locadora = Locadora("Locadora Senai")
codigo_item = 0
codigo_cliente = 0

def cadastro_cliente():
    os.system("cls")
    print(" Cadastro de Cliente")
    nome = input("Nome: ")
    cpf = input("CPF: ")
    codigo_cliente += 1
    match nome, cpf:
        case _:
            print("Opção inválida!")
            os.system("pause")

    cliente = Cliente(nome, cpf)
    locadora.adicionarCliente(cliente)
    print("Cliente cadastrado com sucesso!")
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
                codigo_item += 1
                titulo = input("Título: ")
                genero = input("Gênero: ")
                duracao = int(input("Duração (min): "))
                filme = Filme(codigo_item, titulo, genero, duracao)
                locadora.adicionarItem(filme)
                print("Filme cadastrado com sucesso!")
            case 2:
                codigo_item += 1
                titulo = input("Título: ")
                plataforma = input("Plataforma: ")
                faixa = input("Faixa etária: ")
                jogo = Jogo(codigo_item, titulo, plataforma, faixa)
                locadora.adicionarItem(jogo)
                print("Jogo cadastrado com sucesso!")
            case _:
                print("Opção inválida!")
    except Exception:
        print(f"Opção inválida, tente novamente!")
        os.system("pause")
        return


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
