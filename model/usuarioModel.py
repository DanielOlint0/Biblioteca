from abc import ABC, abstractmethod

class Usuario(ABC):
    def __init__(self, nome, idade, multa, qDeEmprestimos):
        self._nome = nome
        self._idade = idade
        self._multa = multa
        self._qDeEmprestimos = qDeEmprestimos
    def getNome(self):
        return self._nome
    def setNome(self, valor):
        self._nome = valor
    def getIdade(self):
        return self._idade
    def setIdade(self, valor):
        self._idade = valor
    def getMulta(self):
        return self._multa
    def setMulta(self, valor):
        self._multa = valor
    def getQDeEmprestimo(self):
        return self._qDeEmprestimos
    def setQDeEmprestimo(self, valor):
        self._qDeEmprestimos = valor
    
    @abstractmethod
    def testeQuantidade(self):
        pass
