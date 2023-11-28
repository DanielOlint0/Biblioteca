from model.tabletsModel import Tablet
from bd import _executar

class AdicionarTablet:
    @staticmethod
    def post(nome, data, marca, codigoModelo):
        tablet = Tablet(nome, data, marca, codigoModelo)
        tablet.salvar()

class AtualizarTablet:
    @staticmethod
    def get(id, status):
        tablet = Tablet.buscar_por_id(id)
        tablet.setStatus(status)
        tablet.alterar()
        
class ApagarTablet:
    @staticmethod
    def get(id):
        tablet = Tablet.buscar_por_id(id)
        tablet.detetar()

class ListarTablet:
    @staticmethod
    def get():
        tablets = Tablet.getTablets()
        for tablet in tablets:
            print(tablet)

class BuscarTablet:
    @staticmethod
    def get(id):
        tablet = Tablet.buscar_por_id(id)
        print(tablet)