from model.materiaisModel import Material
from bd import _executar

class Tablet(Material):
    def __init__(self, nome, codigo, data, quantidade, marca, codigoModelo, status=1, id = None):
        super().__init__(nome, codigo, data, quantidade, status)
        self.__marca = marca
        self.__codigoModelo = codigoModelo
        self.__id = id

        query = """
            CREATE TABLE IF NOT EXISTS tablets(
                id INTEGER PRIMARY KEY AUTOINCREMENT ,
                nome TEXT,
                data TEXT, 
                quantidade REAL, 
                status NUMERIC,
                marca TEXT,
                codigo INTEGER,
                codigoModelo INTEGER
            )
        """

        _executar(query)
    
    def getId (self):
        return self.__id
    def setId (self, valor):
        self.__id = valor

    def getMarca (self):
        return self.__marca
    def setMarca (self, valor):
        self.__marca = valor
    
    def getCodigoModelo(self):
        return self.__codigoModelo
    def setCodigoModelo(self, valor):
        self.__codigoModelo = valor

    def exibir(self):
        # Aqui você pode personalizar a exibição conforme necessário
        return super().exibir()

    def salvar(self):
        query = f"""
            INSERT INTO tablets 
            (nome, data, quantidade, status, marca, codigo, codigoModelo) 
            VALUES 
            ('{self._nome}', '{self._data}', '{int(self._quantidade)}', '{int(self._status)}', '{self.__marca}',' {int(self._codigo)}', '{int(self.__codigoModelo)}')"""
        
        _executar(query)

    def alterar(self):
        query = f"UPDATE tablets SET status='{self._status}' WHERE id={self.getId()}"
        _executar(query)

    def detetar (self):
        query = f"""
            DELETE FROM tablets
            WHERE id = {int(self.__id)} 
        """
        _executar(query)
    
    #Lista todos os tablets
    @classmethod
    def getTablets(self):
        query = """
            SELECT * FROM tablets
        """
        tablets = _executar(query)

        return tablets

     #Consulta todos os tablets com um estatus específico
    @classmethod
    def getTablet(self):
        query = f"""
            SELECT id, nome, marca FROM tablets
            WHERE status = {int(id)}
        """
        _executar(query)
        tablet = Tablet(id = tablet [0])
        tablet = Tablet(nome = tablet [1])
        tablet = Tablet(preco = tablet [2])

        return tablet
    
    @staticmethod
    def buscar_por_id(id):
        query = f"SELECT * FROM tablets WHERE id={int(id)}"
        tablet = _executar(query)[0]
        tablet = Tablet(id = tablet[0], nome = tablet[1], data= tablet[2], quantidade= tablet[3], status= tablet[4], marca = tablet[5],  codigoModelo= tablet[6], codigo = tablet[7])
        return tablet


    #exibe a quantidade de tablets em um status específico
    def getTablet(self): 
        query = f"""
            SELECT count(*) as Quantidade_de_tablets 
            FROM tablets
            WHERE status = {int(self._status)}
        """
        _executar(query)

     #to string
    def __str__(self):
        return f"'{self.__id}', '{self._nome}', '{self.__marca}', '{self._status}'"