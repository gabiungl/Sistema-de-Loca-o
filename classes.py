class Item:
    def __init__(self, idItem, titulo):
        self._idItem = idItem
        self._titulo = titulo
        self._disponivel = True

    def alugar(self):
        self._disponivel = False

    def devolver(self):
        self._disponivel = True

    def idItem(self):
        return self._idItem

    def titulo(self):
        return self._titulo

    def estado(self):
        return self._disponivel


class Filme(Item):
    def __init__(self, id, titulo, genero, duracao):
        self._idItem = id
        self._titulo = titulo
        self._disponivel = True
        self._genero = genero
        self._duracao = duracao

    def genero(self):
        return self._genero

    def duracao(self):
        return self._duracao


class Jogo(Item):
    def __init__(self, id, titulo, plataforma, faixaEtaria):
        self._idItem = id
        self._titulo = titulo
        self._disponivel = True
        self._plataforma = plataforma
        self._faixaEtaria = faixaEtaria

    def plataforma(self):
        return self._plataforma

    def faixaEtaria(self):
        return self._faixaEtaria


class Cliente:
    def __init__(self, cpf, nome):
        self._cpf = cpf
        self._nome = nome
        self._itens = []

    def alugar(self, item):
        if item.estado():
            item.alugar()
            self._itens.append(item)
            print(f"{self._nome} alugou {item.titulo()}")
        else:
            print(f"{item.titulo()} não está disponível")

    def devolver(self, item):
        if item in self._itens:
            item.devolver()
            self._itens.remove(item)
            print(f"{self._nome} devolveu {item.titulo()}")

    def listarItens(self):
        return [item.titulo() for item in self._itens]


class Locadora:
    def __init__(self):
        self._clientes = []
        self._itens = []

    def cadastrarCliente(self, cliente):
        self._clientes.append(cliente)

    def cadastrarItem(self, item):
        self._itens.append(item)

    def listarItens(self):
        for item in self._itens:
            status = "Disponível" if item.estado() else "Alugado"
            print(f"{item.titulo()} - {status}")
