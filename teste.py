from model.livrosModel import Livro
from bd import _executar

if __name__ == '__main__':
    l = Livro("Padrões de Projeto", 123, "10/11/2023", 3, 0, 321,  "Erich Gamma", "sla")

    print(l)

    #insiro os objetos na base de dados
    #print("======INSERIR======")
    #l.inserir()
    print(Livro.listar())
    #print(l)