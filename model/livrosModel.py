from materiais import Material
from bd import _executar

class Livro(Material):
    def __init__(self, nome, codigo, data, quantidade, status, codigoTitulo, autor, editora, id=None):
        super().__init__(nome, codigo, data, quantidade, status)
        self.__codigoTitulo = codigoTitulo
        self.__autor = autor
        self.__editora = editora
        self.__id = id

    def getId(self):
        return self.__id
    
    def setId(self, valor):
        self.__id = valor

    def getCodigoTitulo(self):
        return self.__codigoTitulo
    
    def setCodigoTitulo(self, valor):
        self.__codigoTitulo = valor

    def getAutor(self):
        return self.__autor
    
    def setAutor(self, valor):
        self.__autor = valor

    def getEditora(self):
        return self.__editora
    
    def setEditora(self, valor):
        self.__editora = valor

    def exibir(self):
        # Aqui você pode personalizar a exibição conforme necessário
        return super().exibir()

    def inserir(self):
        query = f"INSERT INTO livros (nome, codigo, data, quantidade, status, codigoTitulo, autor, editora) VALUES ('{self.getNome()}', '{self.getCodigo()}', '{self.getData()}', {self.getQuantidade()}, '{self.getStatus()}', '{self.getCodigoTitulo()}', '{self.getAutor()}', '{self.getEditora()}')"
        _executar(query)

    def alterar(self):
        query = f"UPDATE livros SET nome='{self.getNome()}', data='{self.getData()}', quantidade={self.getQuantidade()}, status='{self.getStatus()}', codigoTitulo='{self.getCodigoTitulo()}', autor='{self.getAutor()}', editora='{self.getEditora()}' WHERE id={self.getId()}"
        _executar(query)

    def excluir(self):
        query = f"DELETE FROM livros WHERE id={self.getId()}"
        _executar(query)

    @staticmethod
    def listar():
        query = "SELECT * FROM livros"
        livros = _executar(query)
        return livros

    @staticmethod
    def buscar_por_id(id):
        query = f"SELECT * FROM livros WHERE id={id}"
        resultado = _executar(query)

        if resultado:
            # Criar uma instância de Livro com os dados retornados do banco de dados
            livro = Livro(
                nome=resultado[0],
                codigo=resultado[1],
                data=resultado[2],
                quantidade=resultado[3],
                status=resultado[4],
                codigoTitulo=resultado[5],
                autor=resultado[6],
                editora=resultado[7],
                id=resultado[8]
            )
            return livro
        else:
            return None