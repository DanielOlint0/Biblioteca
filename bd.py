import sqlite3

def _executar(query):
    bd_path = './Biblioteca'
    connection = sqlite3.connect(bd_path)
    cursor = connection.cursor()
    resultado = None
    try:
        cursor.execute(query)
        resultado = cursor.fetchall()
        connection.commit()
    except Exception as e:
        print(f'Erro na execuçao da query: {e}')
    finally:
        cursor.close()
        connection.close()
        return resultado