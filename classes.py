class Item:
    def __init__(self, idItem, titulo):
        self._idItem = idItem
        self._titulo = titulo
        self._disponivel = True

    def alugar(self):
        self._disponivel = False

    def devolver(self):
        self._disponivel = True

    def idItem (self):
        return self._idItem

    def titulo (self):
        return self._titulo

    def estado (self):
        return self._disponivel


class Filme(Item):
    def __init__(self, id, titulo, genero, duracao):
        self._idItem = id
        self._titulo = titulo
        self._disponivel = True
        self._genero = genero
        self._duracao = duracao

    def alugar(self):
        self.__disponivel = False

    def devolver(self):
        self.__disponivel = True

    def idFilme(self):
        return self._idItem

    def titulo(self):
        return self._titulo

    def estado(self):
        return self._disponivel

    def genero(self):
        return self._genero

    def duracao(self):
        return self._duracao
