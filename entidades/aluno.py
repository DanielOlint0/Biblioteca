from usuario import Usuario
class Aluno(Usuario):
    def __init__(self, nome, idade, multa, qDeEmprestimos):
        super().__init__(nome, idade, multa, qDeEmprestimos)
        self.__curso = []
    def getTurma(self):
        return self.__curso

    def testeQuantidade(self):
        ...