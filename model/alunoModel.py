from bd import _executar
from model.usuarioModel import Usuario

class Aluno(Usuario):
    def __init__(self, nome, idade, curso, multa=0, qDeEmprestimos=0, id=None):
        super().__init__(nome, idade, multa, qDeEmprestimos)
        self.__curso = curso
        self.__id = id
    
    #Checar se a tabela Aluno existe.
    query = "CREATE TABLE IF NOT EXISTS alunos(id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT, idade INTEGER, curso TEXT, multa REAL, qDeEmprestimos INTEGER)"
    _executar(query)
    print("Tabela Criada!")

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
        if self.getQDeEmprestimos() < 2:
            return True
        else:
            return False
    
    #inserir
    def cadastrarAluno(self):
        query = f"INSERT INTO alunos(nome, idade, curso, multa, qDeEmprestimos) VALUES ('{self.getNome()}', {int(self.getIdade())}, '{self.getCurso()}', '{float(self.getMulta())}', '{int(self.getQDeEmprestimos())}')"
        _executar(query)
        print("Aluno Cadastrado!")

    #alterar
    def alterarAluno(self):
        query = f"UPDATE alunos SET nome='{self.getNome()}', idade='{int(self.getIdade())}', curso='{self.getCurso()}', multa='{float(self.getMulta())}', qDeEmprestimos='{int(self.getQDeEmprestimos())}' WHERE id={self.getId()}"
        _executar(query)
        print("Aluno Editado!")

    #excluir
    def excluirAluno(self):
        query=f"DELETE FROM alunos WHERE id={self.getId()}"
        _executar(query)
        print("Aluno Deletado!")

    #listar alunos que estão cadastrados.
    @staticmethod
    def listarAlunos():
      query="SELECT * FROM alunos"
      alunos=_executar(query)
      return alunos

    #buscar aluno pelo ID.
    @staticmethod
    def listarAluno(id):
        query=f"SELECT * FROM alunos WHERE id={int(id)}"
        resultado = _executar(query)[0]
        if resultado:
            aluno = Aluno(
                nome=resultado[1],
                idade=resultado[2],
                curso=resultado[3],
                multa=resultado[4],
                qDeEmprestimos=resultado[5],
                id=resultado[0]
            )
            return aluno
        else:
            return None
    
    def __str__(self):
        return f"""
Aluno
ID: {self.__id}
Nome: {self.getNome()}
Idade: {self.getIdade()}
Curso: {self.__curso}
Multa: {self.getMulta()}
Quantidade de Empréstimos: {self.getQDeEmprestimos()}
"""
