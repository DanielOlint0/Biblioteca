from controller.tabletController import Apagar, Listar, Adicionar, Atualizar, Buscar
from bd import _executar

if __name__ == '__main__':
    Adicionar.post("Tablet A", 123, "2023-11-13", 5, 1, "Marca A", 456)
    Adicionar.post("Tablet B", 124, "2023-11-14", 6, 1, "Marca B", 457)
    Adicionar.post("Tablet C", 125, "2023-11-15", 7, 1, "Marca C", 458)
    Listar.get()

    Apagar.get(1)
    Listar.get()

    Buscar.get(2)

    Atualizar.get(3, 0)
    Listar.get()