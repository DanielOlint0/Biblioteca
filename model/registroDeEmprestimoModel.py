from bd import _executar

class RegistroDeEmprestimo:
    def __init__(self, dataInicio, dataFinal, codigoUsuario=None, codigoMaterial=None, id=None):
        self.__dataInicio = dataInicio
        self.__dataFinal = dataFinal
        self.__codigoUsuario = codigoUsuario
        self.__codigoMaterial = codigoMaterial
        self.__id = id
        self.__ativo = 1

        query = "CREATE TABLE IF NOT EXISTS RegistroDeEmprestimo(id INTEGER AUTOINCREMENT PRIMARY KEY, nome TEXT, preco REAL, status NUMERIC)"
        _executar(query)
   
    def getDataInicio(self):
        return self.__dataInicio
    def setDataInicio(self, valor):
        self.__dataInicio = valor
    
    def getDataFinal(self):
        return self.__dataFinal
    def setDataFinal(self, valor):
        self.__dataFinal = valor

    def getCodigoUsuario(self):
        return self.__codigoUsuario
    def setCodigoUsuario(self, valor):
        self.__codigoUsuario = valor
    
    def getCodigoMaterial(self):
        return self.__codigoMaterial
    def setCodigoMaterial(self, valor):
        self.__codigoMaterial = valor

    def getAtivo(self):
        return self.__ativo
    def setAtivo(self, valor):
        self.__ativo = valor

    def salvar(self):
        query = f"INSERT INTO RegistroDeEmprestimo(dataInicio, dataFinal, codigoMateria, codigoUsuario) VALUES ({self.__dataInicio}, {self.__dataFinal}, {int(self.__codigoMaterial)}, {int(self.__codigoUsuario)})"
        _executar(query)
    def alterar(self):
        query = f"UPDATE RegistroDeEmprestimo SET status = {int(self.__status)} WHERE id = {int(self.__id)}"
        _executar(query)
    def excluir(self):
            query = f"DELETE FROM RegistroDeEmprestimo WHERE id = {int(self.__id)}"
            _executar(query)
    
    @staticmethod
    def get_registros():
        query = "SELECT * FROM RegistroDeEmprestimo"
        registros = _executar(query)
        return registros
    @staticmethod
    def get_produto():
        query = f"SELECT * FROM RegistroDeEmprestimo WHERE id ={int(id)}"
        _executar(query)[0]
        registro = RegistroDeEmprestimo(id=registro[0]),
        registro = RegistroDeEmprestimo(nome=registro[1]),
        registro = RegistroDeEmprestimo(preco=registro[2])
        return registro
