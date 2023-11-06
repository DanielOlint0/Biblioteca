from usuario import Usuario
class Professor(Usuario):
    def __init__(self, nome, idade, multa, qDeEmprestimos):
        super().__init__(nome, idade, multa, qDeEmprestimos)
        self.__turma = []
    def getTurma(self):
        return self.__turma

    def testeQuantidade(self):
        ...