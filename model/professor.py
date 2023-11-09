from bd import _executar
from usuario import Usuario

class Professor(Usuario):
    def __init__(self, nome, idade, multa, qDeEmprestimos, turma, id=None):
        super().__init__(nome, idade, multa, qDeEmprestimos)
        self.__turma = turma

    def getTurma(self):
        return self.__turma
    def setTurma(self, value):
        self.__turma = value

    def getId(self):
        return self.__id
    def setId(self, value):
        self.__id = value

    def testeQuantidade(self):
        ...
    
    query = "CREATE TABLE IF NOT EXISTS professores(id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT, idade INTEGER, multa REAL, qDeEmprestimos INTEGER, turma TEXT)"
    _executar(query)

    # Inserir
    def cadastrarProfessor(self):
        query = f"INSERT INTO professores(nome, idade, multa, qDeEmprestimos, turma) VALUES ('{self.__nome}', {int(self.__idade)}, {float(self.__multa)}, {int(self.__qDeEmprestimos)}, '{self.__turma}')"
        _executar(query)

    # Alterar
    def alterarProfessor(self):
        query = f"UPDATE professores SET nome='{self.__nome}', idade={int(self.__idade)}, multa={float(self.__multa)}, qDeEmprestimos={int(self.__qDeEmprestimos)}, turma='{self.__turma}' WHERE id={int(self.__id)}"
        _executar(query)

    # Excluir
    def excluirProfessor(self):
        query = f"DELETE FROM professores WHERE id={int(self.__id)}"
        _executar(query)

    # Listar professores cadastrados.
    @staticmethod
    def get_professores():
        query = "SELECT * FROM professores"
        professores = _executar(query)
        return professores

    # Buscar professor pelo ID.
    @staticmethod
    def get_professor_by_id(self):
        query = f"SELECT * FROM professores WHERE id={int(self.__id)}"
        professor = _executar(query)[0]
        return professor
