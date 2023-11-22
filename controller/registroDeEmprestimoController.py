from model.registroDeEmprestimoModel import RegistroDeEmprestimo

class Adicionar:
    @staticmethod
    def post(codigoUsuario, codigoMaterial, dataInicio, dataFinal):
        registro = RegistroDeEmprestimo(codigoUsuario, codigoMaterial,dataInicio, dataFinal)
        registro.salvar()

class Adicionar_tablet:
    @staticmethod
    def post(codigoUsuario, codigoMaterial, dataInicio, dataFinal):
        registro = RegistroDeEmprestimo(codigoUsuario, codigoMaterial,dataInicio, dataFinal)
        registro.salvar_tablet()

class Atualizar:
    @staticmethod
    def get(id, status):
        registro = RegistroDeEmprestimo.buscar_por_id(id)
        registro.setStatus(status)
        registro.alterar()

class Apagar:
    @staticmethod
    def get(id):
        registro = RegistroDeEmprestimo.buscar_por_id(id)
        registro.excluir()

class Listar:
    @staticmethod
    def get():
        #print(RegistroDeEmprestimo.get_registros())
        print(RegistroDeEmprestimo.get_registros())
class BuscarRegistroPorID():
    @staticmethod
    def get(id):
        registro = RegistroDeEmprestimo.buscar_por_id(id)
        print(registro)

class Busca():
    @staticmethod
    def get():
        registros = RegistroDeEmprestimo.get_registros()
        for registro in registros:
            print(registro)

class Multa():
    @staticmethod
    def get(id, data):
        multaRegistro = RegistroDeEmprestimo.valorMulta(id, data)
        print(multaRegistro)