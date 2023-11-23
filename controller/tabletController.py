from model.tabletsModel import Tablet
from bd import _executar

class Adicionar:
    @staticmethod
    def post(nome, data, marca, codigoModelo):
        tablet = Tablet(nome, data, marca, codigoModelo)
        tablet.salvar()

class Atualizar:
    @staticmethod
    def get(id, status):
        tablet = Tablet.buscar_por_id(id)
        tablet.setStatus(status)
        tablet.alterar()
        
class Apagar:
    @staticmethod
    def get(id):
        tablet = Tablet.buscar_por_id(id)
        tablet.detetar()

class Listar:
    @staticmethod
    def get():
        tablets = Tablet.getTablets()
        for tablet in tablets:
            print(tablet)

class Buscar:
    @staticmethod
    def get(id):
        tablet = Tablet.buscar_por_id(id)
        print(tablet)