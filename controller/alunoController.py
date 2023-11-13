from model.alunoModel import Aluno

class CadastrarAluno:
    @staticmethod
    def post(nome, idade, curso, multa, qDeEmprestimos):
        aluno = Aluno(nome, idade, curso, multa, qDeEmprestimos)
        aluno.cadastrarAluno()

class DeletarAluno:
    @staticmethod
    def get(id):
        aluno = Aluno.listarAluno(id)
        aluno.excluirAluno()

class EditarAluno:
    @staticmethod
    def get(id, nome, idade, curso, multa, qDeEmprestimos):
        aluno = Aluno.listarAluno(id)
        aluno._nome = nome
        aluno.setCurso(curso)
        aluno._idade = idade
        aluno._multa = multa
        aluno._qDeEmprestimos = qDeEmprestimos
        aluno.alterarAluno()

class ListarAlunos:
    @staticmethod
    def get():
        print(Aluno.listarAlunos())

class ListarAluno:
    @staticmethod
    def get(id):
        print(Aluno.listarAluno(id))

class TestarQuantidade:
    @staticmethod
    def get(id):
        aluno = Aluno.listarAluno(id)
        print(aluno.testeQuantidade())
