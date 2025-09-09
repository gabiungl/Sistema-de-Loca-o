class Locadora:
    def __init__(self, nome):
        self.__nome = nome
        self.__acervo = {}
        self.__id = 0
    
    def addLivro(self, livro):
        self.__id += 1
        self.__acervo[self.__id] = livro
    
    def listar(self):
        return self.__acervo


class Item:
    def __init__(self, id, titulo, disponibilidade):
        self.__id = id
        self.__titulo = titulo
        self.__disponibilidade = disponibilidade


    def getNome(self):
        return self.__nome
