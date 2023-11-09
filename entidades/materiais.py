from abc import ABC, abstractmethod

class Material(ABC):
    def __init__(self, nome, codigo, data, quantidade, status):
        self._nome = nome
        self._codigo = codigo
        self._data = data
        self._quantidade = quantidade
        self._status = status
    
    def getNome(self):
        return self._nome
    def setNome(self, valor):
        self._nome = valor

    def getCodigo(self):
        return self._codigo
    def setCodigo(self, valor):
        self._codigo = valor
    
    def getData(self):
        return self._data
    def setData(self, valor):
        self._data = valor

    def getStatus(self):
        return self._status
    def setStatus(self, valor):
        self._status = valor

    def getQuantidade(self):
        return self._quantidade
    def setQuantidade(self, valor):
        self._quantidade = valor

    @abstractmethod
    def exibir(self):
        pass

