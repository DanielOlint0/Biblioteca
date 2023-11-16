from model.usuarioModel import Usuario

class Adicionar:
    @staticmethod
    def post(nome, idade, multa, tipoDeUsuario):
        usuario = Usuario(nome, idade, multa, tipoDeUsuario)
        usuario.cadastrarUsuario()

class Atualizar:
    @staticmethod
    def get(id, nome, idade):
        usuario = Usuario.listarUsuarioPorId(id)
        usuario.setNome(nome)
        usuario.setIdade(idade)
        usuario.alterarUsuario()

class Apagar:
    @staticmethod
    def get(id):
        usuario = Usuario.listarUsuarioPorId(id)
        usuario.excluirUsuario()

class Listar:
    @staticmethod
    def get():
        print(Usuario.listarUsuarios())

class Buscar:
    @staticmethod
    def get(id):
        print(Usuario.listarUsuarioPorId(id))
