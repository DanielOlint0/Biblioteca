from controller.usuarioController import Apagar, Listar, Adicionar, Atualizar, Buscar

if __name__ == '__main__':
    #Adicionar produtos na base de dados usando nome e preco
    print('====Adicionar====')
    #Adicionar.post("Berg", 82, 1, 0)
    #Adicionar.post("George", 13, 1, 3)
    Listar.get()#listo a base de dado
    
    #print('====Excluir====')
    #Apagar.get(8)
    #Listar.get()

    #print('====Buscar====')
    #Buscar.get(2)

    #print('====Atualizar====')
    #Atualizar.get(2, 'Craudio', 42)
    #Listar.get()
