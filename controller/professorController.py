from model.professorModel import Professor

class Adicionar:
    @staticmethod
    def post(nome, idade, turma, multa, qDeEmprestimos):
        professor = Professor(nome, idade, turma, multa, qDeEmprestimos)
        professor.cadastrarProfessor()

class Atualizar:
    @staticmethod
    def get(id, nome, idade):
        professor = Professor.listarProfessor(id)
        professor._nome = nome
        professor._idade = idade
        professor.alterarProfessor()

class Apagar:
    @staticmethod
    def get(id):
        professor = Professor.listarProfessor(id)
        professor.excluirProfessor()

class Listar:
    @staticmethod
    def get():
        print(Professor.listarProfessores())

class Buscar:
    @staticmethod
    def get(id):
        print(Professor.listarProfessor(id))