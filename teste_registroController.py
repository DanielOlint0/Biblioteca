from controller.registroDeEmprestimoController import Adicionar, BuscarRegistroPorID, Apagar, Atualizar, Listar, Multa
from datetime import date, timedelta

if __name__ == '__main__':
    #Adicionar novo registro
    '''print('====Adicionar====')
    dataInicio = date.today()
    dataFinal = dataInicio + timedelta(7)
    Adicionar.post(1, 3, dataInicio, dataFinal)
    Adicionar.post(2, 7, dataInicio, dataFinal)
    Listar.get()'''
    
    print('====Atualiza====')
    Atualizar.get(1, 0)
    Listar.get()

    print('====Busca por id====')
    BuscarRegistroPorID.get(1)
    Listar.get()
    
    print('====Excluir====')
    #Apagar.get(2)
    Listar.get()

    data1 = date.today()
    data = data1 + timedelta(14)
    Multa.get(1, data)