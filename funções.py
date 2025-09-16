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
    print(f"Cliente [{cliente.getId()}] cadastrado com sucesso!")  
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
        print(f"[{clie.getId()}] Nome: {clie.getNome()}")  # getId() e getNome() corrigidos
    os.system("pause")

def listar_itens():
    os.system("cls")
    print(" Itens Cadastrados ")
    for itens in locadora.listarItens():
        status = "Disponível" if itens.getDisponivel() else "Indisponível"  # getDisponivel()
        print(f"[{itens.getCodigo()}] {itens.getTitulo()} - {status}")  # getCodigo() e getTitulo()
    os.system("pause")

def alugar_item():
    while True:
        try:
            print("-Alugar-")
            print("\nClientes cadastrados:")
            count = 1
            for cliente in locadora.listarClientes():
                print(f"ID:{count} \nNome: {cliente.getNome()} \nCPF: {cliente.getCpf()}") 
                count += 1

            print("\nItens disponíveis:")
            count = 1
            for item in locadora.listarItens():
                status = "Disponível" if item.getDisponivel() else "Alugado"
                print(f"ID:{count} \nTítulo: {item.getTitulo()} \nStatus: {status}")
                count += 1

            cliente_id = int(input("\nDigite o ID do cliente: "))
            item_id = int(input("Digite o ID do item: "))

            cliente = locadora.listarClientes()[cliente_id - 1]
            item = locadora.listarItens()[item_id - 1]

            if item.getDisponivel():
                cliente.locar(item) 
            else:
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
                print(f"ID:{count} \nNome: {cliente.getNome()}") 
                count += 1

            print("\nItens:")
            count = 1
            for item in locadora.listarItens():
                status = "Disponível" if item.getDisponivel() else "Alugado"  
                print(f"ID:{count} \nTítulo: {item.getTitulo()} \nStatus: {status}")
                count += 1

            cliente_id = int(input("\nDigite o ID do cliente: "))
            item_id = int(input("Digite o ID do item: "))

            cliente = locadora.listarClientes()[cliente_id - 1]
            item = locadora.listarItens()[item_id - 1]

            if item in cliente._Cliente__itens_locados:  
                cliente.devolver(item)
            else:
                print(f"O cliente {cliente.getNome()} não tem esse item alugado.")
            os.system("pause")
            break
        except Exception as e:
            print(f"Ocorreu um erro inesperado: {e}")
            os.system("pause")