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
