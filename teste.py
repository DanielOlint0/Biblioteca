from model.livrosModel import Livro
from model.tabletsModel import Tablet
from bd import _executar

if __name__ == '__main__':
    l = Livro("Padrões de Projeto", 123, "10/11/2023", 3, 1, 321,  "Erich Gamma", "sla")
    ll = Livro("Padrões de Projeto", 123, "10/11/2023", 3, 1, 321,  "Erich Gamma", "sla")

    print("=========TESTE LIVRO=========")
    #insiro os objetos na base de dados
    print("======INSERIR======")
    l.inserir()
    ll.inserir()
    print(Livro.listar())

    print()
    print(Livro.buscar_por_id(2))
    print()

    print("======EXCLUIR======")
    indice=1 #pode ser feito via input
    l.setId(Livro.buscar_por_id(indice).getId())
    print(l.listar())
    l.excluir()
    print()
    print(l.listar())

    print("======ALTERAR======")
    indice=2 #pode ser feito via input
    ll.setStatus(0) #1: ativo e 0: inativo, pode ser feito via input
    ll.setId(Livro.buscar_por_id(indice).getId())
    ll.alterar()
    print(Livro.listar())

    print()
    t1 = Tablet("Sansung", 456, "11/11/2023", 4, 1, "Ja botei ali", 654)
    t2 = Tablet("Sansung", 456, "11/11/2023", 4, 1, "Ja botei ali", 654)
    
    print("=========TESTE TABLET=========")
    #insiro os objetos na base de dados
    print("======INSERIR======")
    t1.salvar()
    t2.salvar()
    print(Tablet.getTablets())

    print()
    print(Tablet.buscar_por_id(2))
    print()

    print("======EXCLUIR======")
    indice=1 #pode ser feito via input
    t1.setId(Tablet.buscar_por_id(indice).getId())
    print(t1.getTablets())
    t1.detetar()
    print()
    print(t1.getTablets())

    #esse alterar ta diminuindo a quantidade
    print("======ALTERAR======")
    indice=2 #pode ser feito via input
    t2.setId(Tablet.buscar_por_id(indice).getId())
    t2.alterar()
    print(Tablet.getTablets())