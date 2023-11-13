from controller.professorController import Apagar, Listar, Adicionar, Atualizar, Buscar

if __name__ == '__main__':
    #Adicionar produtos na base de dados usando nome e preco
    print('====Adicionar====')
    Adicionar.post("Berg", 82, "DS", 5, 3)
    Adicionar.post("George", 13, "DS", 5, 1)
    #Adicionar.post(nome, preco) pode ser feito via input
    Listar.get()#listo a base de dado
    
    print('====Excluir====')
    Apagar.get(1)
    Listar.get()

    print('====Buscar====')
    Buscar.get(2)

    print('====Atualizar====')
    Atualizar.get(2, 'Regis', 42)
    Listar.get()