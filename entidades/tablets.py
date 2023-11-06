from materiais import Material

class Tablet(Material):
    def __init__(self, nome, codigo, data, quantidade, status, marca, codigoModelo):
        super().__init__(nome, codigo, data, quantidade, status)
        self.__marca = marca
        self.__codigoModelo = codigoModelo
    
    def getMarca (self):
        return self.__marca
    def setMarca (self, valor):
        self.__marca = valor
    
    def getCodigoModelo(self):
        return self.__codigoModelo
    def setCodigoModelo(self, valor):
        self.__codigoModelo = valor

    def exibir(self):
        #return super().exibir()
        ...