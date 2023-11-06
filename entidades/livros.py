from materiais import Material

class Livro(Material):
    def __init__(self, nome, codigo, data, quantidade, status, codigoTitulo, autor, editora):
        super().__init__(nome, codigo, data, quantidade, status)
        self.__codigoTitulo = codigoTitulo
        self.__autor = autor
        self.__editora = editora

    def getCodigoTitulo (self):
        return self.__codigoTitulo
    def setCodigoTitulo (self, valor):
        self.__codigoTitulo = valor
    
    def getAutor(self):
        return self.__autor
    def setAutor (self, valor):
        self.__autor = valor
    
    def getEditora (self):
        return self.__editora
    def setEditora (self, valor):
        self.__editora = valor
    
    def exibir(self):
        #return super().exibir()
        ...