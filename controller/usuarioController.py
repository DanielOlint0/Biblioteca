from model.usuarioModel import Usuario

class Adicionar:
    @staticmethod
    def post(nome, idade, tipoDeUsuario):
        usuario = Usuario(nome, idade, tipoDeUsuario)
        usuario.cadastrarUsuario()

class Atualizar:
    @staticmethod
    def get(id):
        usuario = Usuario.listarUsuarioPorId(id)
        usuario.alterarUsuario()
        print(usuario)

class Devolver:
    @staticmethod
    def get(id):
        usuario = Usuario.listarUsuarioPorId(id)
        usuario.devolver()
        print(usuario)

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
