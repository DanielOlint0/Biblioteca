from bd import _executar
from model.usuarioModel import Usuario

class Professor(Usuario):
    def __init__(self, nome, idade, turma, multa=0, qDeEmprestimos=0, id=None):
        super().__init__(nome, idade, multa, qDeEmprestimos)
        self.__turma = turma
        self.__id = id

    query = "CREATE TABLE IF NOT EXISTS professores(id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT, idade INTEGER, turma TEXT, multa REAL, qDeEmprestimos INTEGER)"
    _executar(query)
    print("Tabela Criada!")

    def getTurma(self):
        return self.__turma
    def setTurma(self, value):
        self.__turma = value

    def getId(self):
        return self.__id
    def setId(self, value):
        self.__id = value

    def testeQuantidade(self):
        if self.getQDeEmprestimos() < 3:
            return True
        else:
            return False

    # Inserir
    def cadastrarProfessor(self):
        query = f"INSERT INTO professores(nome, idade, turma, multa, qDeEmprestimos) VALUES ('{self.getNome()}', {int(self.getIdade())}, '{self.getTurma()}', '{float(self.getMulta())}', '{int(self.getQDeEmprestimos())}')"
        _executar(query)
        print("Professor Cadastrado!")

    # Alterar
    def alterarProfessor(self):
        query = f"UPDATE professores SET nome='{self.getNome()}', idade='{int(self.getIdade())}', turma='{self.getTurma()}', multa='{float(self.getMulta())}', qDeEmprestimos='{int(self.getQDeEmprestimos())}' WHERE id={int(self.getId())}"
        _executar(query)

    # Excluir
    def excluirProfessor(self):
        query = f"DELETE FROM professores WHERE id={int(self.getId())}"
        _executar(query)

    # Listar professores cadastrados.
    @staticmethod
    def listarProfessores():
        query = "SELECT * FROM professores"
        professores = _executar(query)
        return professores

    # Buscar professor pelo ID.
    @staticmethod
    def listarProfessor(id):
        query = f"SELECT * FROM professores WHERE id={int(id)}"
        resultado = _executar(query)[0]
        if resultado:
            professor = Professor(
                nome=resultado[1],
                idade=resultado[2],
                turma=resultado[3],
                multa=resultado[4],
                qDeEmprestimos=resultado[5],
                id=resultado[0]
            )
            return professor
        else:
            return None

    def __str__(self):
        return f"""
Professor
ID: {self.__id}
Nome: {self.getNome()}
Idade: {self.getIdade()}
Turma: {self.__turma}
Multa: {self.getMulta()}
Quantidade de Empréstimos: {self.getQDeEmprestimos()}
"""
