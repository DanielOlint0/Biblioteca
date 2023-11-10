from bd import _executar
from usuarioModel import Usuario

class Aluno(Usuario):
    def __init__(self, nome, idade, multa, qDeEmprestimos, curso, id=None):
        super().__init__(nome, idade, multa, qDeEmprestimos)
        self.__curso = curso
        self.__id = id

    def getCurso(self):
        return self.__curso
    def setCurso(self, value):
        self.__curso = value

    def getId(self):
        return self.__id
    def setId(self, value):
        self.__id = value

    #Checar quantidade máxima de dois livros em registro.
    def testeQuantidade(self):
        ...
    
    #Checar se a tabela Aluno existe.
    query = "CREATE TABLE IF NOT EXISTS alunos(id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT, idade INTEGER, multa REAL, qDeEmprestimos INTEGER, curso TEXT)"
    _executar(query)
    
    #inserir
    def cadastrarAluno(self):
        query=f"INSERT INTO alunos(nome, idade, multa, qtEmprestimos, curso) VALUES ({self.__nome}, {int(self.__idade)}, {float(self.__multa)}, {int(self.__qDeEmprestimos)}, {self.__curso})"
        _executar(query)

    #alterar
    def alterarAluno(self):
        query = f"UPDATE alunos SET nome='{self.__nome}', idade={int(self.__idade)}, multa={float(self.__multa)}, qDeEmprestimos={int(self.__qDeEmprestimos)}, curso='{self.__curso}' WHERE id={int(self.__id)}"
        _executar(query)

    #excluir
    def excluirAluno(self):
        query=f"DELETE FROM alunos WHERE id={int(self.__id)}"
        _executar(query)

    #listar alunos que estão cadastrados.
    @staticmethod
    def get_alunos():
      query="SELECT * FROM alunos"
      alunos=_executar(query)
      return alunos

    #buscar aluno pelo ID.
    @staticmethod
    def get_aluno(self):
        query=f"SELECT * FROM produtos WHERE id={int(self.__id)}"
        produto = _executar(query)[0]
        return produto
