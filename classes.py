class Locadora:
    def __init__(self):
        self.__clientes = []
        self.__itens = []
    
    def cadastrarCliente(self, cliente):
        self.__clientes.append(cliente)

    def cadastrarItem(self, item):
        self.__itens.append(item)
    
    def listarClientes(self):
        return self.__clientes

    def listarItens(self):
        return self.__itens

loc = Locadora()

class Item:
    _contador_id = 0  

    def __init__(self, titulo):
        Item._contador_id += 1
        self.__codigo = Item._contador_id
        self.__titulo = titulo
        self.__disponivel = True
    
    def alugar(self):
        self.__disponivel = False

    def devolver(self):
        self.__disponivel = True

    def getCodigo(self):
        return self.__codigo
    
    def getTitulo(self):
        return self.__titulo
    
    def getDisponivel(self):
        return self.__disponivel


class Jogo(Item):
    def __init__(self, titulo, plataforma, faixa_etaria):
        super().__init__(titulo=titulo)
        self.__plataforma = plataforma
        self.__faixa_etaria = faixa_etaria

    def getPlataforma(self):
        return self.__plataforma
    
    def getFaixa(self):
        return self.__faixa_etaria
    
    
class Filme(Item):
    def __init__(self, titulo, genero, duracao):
        super().__init__(titulo=titulo)
        self.__genero = genero
        self.__duracao = duracao
    
    def getGenero(self):
        return self.__genero
    
    def getDuracao(self):
        return self.__duracao


class Cliente:
    _contador_id = 0 

    def __init__(self, nome, cpf):
        Cliente._contador_id += 1
        self.__id = Cliente._contador_id
        self.__nome = nome
        self.__cpf = cpf
        self.__itens_locados = []

    def locar(self, item):
        if item.getDisponivel():
            item.alugar()
            self.__itens_locados.append(item)
            print(f"{self.__nome} alugou {item.getTitulo()}")
        else:
            print(f"{item.getTitulo()} não está disponível.")

    def devolver(self, item):
        if item in self.__itens_locados:
            item.devolver()
            self.__itens_locados.remove(item)
            print(f"{self.__nome} devolveu {item.getTitulo()}")
        else:
            print(f"{self.__nome} não possui {item.getTitulo()} para devolver.")

    def listarItens(self):
        return [item.getTitulo() for item in self.__itens_locados]

    def getId(self):
        return self.__id

    def getNome(self):
        return self.__nome
    
    def getCpf(self):
        return self.__cpf
