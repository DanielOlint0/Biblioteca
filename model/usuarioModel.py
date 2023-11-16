from bd import _executar

class Usuario:
    def __init__(self, nome, idade, tipoDoUsuario, multa=0, id=None):
        self.__id = id
        self.__nome = nome
        self.__idade = idade
        self.__multa = multa
        self.__tipoDoUsuario=tipoDoUsuario #0 = p e 1=aluno
        if tipoDoUsuario == 1:
            self.__qDeEmprestimos = 2
        else:
            self.__qDeEmprestimos = 3

    query = "CREATE TABLE IF NOT EXISTS usuarios(id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT, idade INTEGER, multa REAL, qDeEmprestimos INTEGER, tipoDoUsuario INTEGER)"
    _executar(query)
    print("Tabela Criada!")

    def getId(self):
        return self.__id
    def setId(self, value):
        self.__id = value
    def getNome(self):
        return self.__nome
    def setNome(self, valor):
        self.__nome = valor
    def getIdade(self):
        return self.__idade
    def setIdade(self, valor):
        self.__idade = valor
    def getMulta(self):
        return self.__multa
    def setMulta(self, valor):
        self.__multa = valor
    def getTipoUsuario(self):
        return self.__tipoDoUsuario
    def setTipoUsuario(self, valor):
        self.__tipoDoUsuario = valor
    def getQDeEmprestimo(self):
        return self.__qDeEmprestimos
    def setQDeEmprestimo(self, valor):
        self.__qDeEmprestimos = valor

    def testeQuantidade(self):
        if self.getQDeEmprestimo == 0:
            return False
        else:
            return True

    # Inserir
    def cadastrarProfessor(self):
        query = f"INSERT INTO usuarios(nome, idade, turma, multa, qDeEmprestimos, tipoDoUsuario) VALUES ('{self.getNome()}', {int(self.getIdade())}, '{self.getTurma()}', '{float(self.getMulta())}', '{int(self.getQDeEmprestimo())}')"
        _executar(query)
        print("Professor Cadastrado!")

    # Alterar
    def alterarProfessor(self):
        query = f"UPDATE usuarios SET nome='{self.getNome()}', idade='{int(self.getIdade())}', multa='{float(self.getMulta())}', qDeEmprestimos='{int(self.getQDeEmprestimo())}'tipoDoUsuario='{int(self.getTipoUsuario())} , ' WHERE id={int(self.getId())}"
        _executar(query)

    # Excluir
    def excluirProfessor(self):
        query = f"DELETE FROM usuarios WHERE id={int(self.getId())}"
        _executar(query)

    # Listar professores cadastrados.
    @staticmethod
    def listarProfessores():
        query = "SELECT * FROM usuarios"
        professores = _executar(query)
        return professores

    # Buscar professor pelo ID.
    @staticmethod
    def listarProfessor(id):
        query = f"SELECT * FROM usuarios WHERE id={int(id)}"
        resultado = _executar(query)[0]
        if resultado:
            usuario = Usuario(
                nome=resultado[1],
                idade=resultado[2],
                turma=resultado[3],
                multa=resultado[4],
                qDeEmprestimos=resultado[5],
                tipoDoUsuario=resultado[6],
                id=resultado[0]
            )
            return usuario
        else:
            return None

    def __str__(self):
        return f"""
Usuario
ID: {self.__id}
Nome: {self.getNome()}
Idade: {self.getIdade()}
Multa: {self.getMulta()}
Quantidade de Empréstimos: {self.getQDeEmprestimo()}
Tipo do usuario: {self.getTipoUsuario()}
"""

    #to string
    def __str__(self):
        return f"'{self._nome}', '{self._idade}'"