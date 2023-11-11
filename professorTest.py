from model.professorModel import Professor
from bd import _executar

if __name__ == '__main__':
    professor1 = Professor("Berg", 82, "DS", 5, 3)
    professor2 = Professor("George", 13, "DS", 5, 1)
    #print(professor1)
    #professor1.cadastrarProfessor()
    #print(Professor.listarProfessores())
    #print(Professor.listarProfessor(3))
    #DELETE
    #index = 2
    #professor2= Professor.listarProfessor(index)
    #professor2.excluirProfessor()
    #print(Professor.listarProfessores())
    #UPDATE
    #index = 3
    #newName = "Regis"
    #newIdade = 43
    #professor3 = Professor.listarProfessor(index)
    #professor3._nome = newName
    #professor3._idade = newIdade
    #professor3.alterarProfessor()
    #print(Professor.listarProfessores())
