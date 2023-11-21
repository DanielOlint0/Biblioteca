
from controller.livroController import AdicionarLivroController, AtualizarLivroController, ApagarLivroController, ListarLivrosController, BuscarLivroController

if __name__ == '__main__':
    #Adicionar
    AdicionarLivroController.post("Livro Teste4", 456, "2023-01-04", 12, 987, "Autor Teste4", "Editora Teste4")
    AdicionarLivroController.post("Livro Teste4", 456, "2023-01-04", 12, 987, "Autor Teste4", "Editora Teste4")
    ListarLivrosController.get()
    
    #Excluir
    #ApagarLivroController.get(1)
    ListarLivrosController.get()
    
    #Buscar
    BuscarLivroController.get(2)
    
    #Atualizar
    AtualizarLivroController.get(2, 0)
    ListarLivrosController.get()
    BuscarLivroController.get(2)