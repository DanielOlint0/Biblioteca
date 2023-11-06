from abc import ABC, abstractmethod

class Material(ABC):
    def __init__(self, nome, codigo, data, quantidade, status):
        self.__nome = nome
        self.__codigo = codigo
        self.__data = data
        self.__quantidade = quantidade
        self.__status = status
    
    def getNome(self):
        return self.__nome
    def setNome(self, valor):
        self.__nome = valor

    def getCodigo(self):
        return self.__codigo
    def setCodigo(self, valor):
        self.__codigo = valor
    
    def getData(self):
        return self.__data
    def setData(self, valor):
        self.__data = valor

    def getStatus(self):
        return self.__status
    def setStatus(self, valor):
        self.__status = valor

    def getQuantidade(self):
        return self.__quantidade
    def setQuantidade(self, valor):
        self.__quantidade = valor

    @abstractmethod
    def exibir(self):
        pass


