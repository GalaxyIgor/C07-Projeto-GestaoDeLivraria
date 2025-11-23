from src.models.livro import Livro
from src.dao.dao_livro import LivroDAO
from src.dao.dao_autor import AutorDAO
from src.dao.dao_editora import EditoraDAO


class MenuLivro:

    def __init__(self):
        self.livro_dao = LivroDAO()
        self.autor_dao = AutorDAO()
        self.editora_dao = EditoraDAO()

    def exibir_menu(self):
        while True:
            print("\n--- Menu de Livros ---")
            print("1. Inserir Livro")
            print("2. Listar Livros")
            print("3. Atualizar Livro")
            print("4. Excluir Livro")
            print("0. Voltar")

            opcao = input("Escolha: ")

            if opcao == "1":
                self.inserir()
            elif opcao == "2":
                self.listar()
            elif opcao == "3":
                self.atualizar()
            elif opcao == "4":
                self.excluir()
            elif opcao == "0":
                break
            else:
                print("Opção inválida.")

    def inserir(self):
        print("\n--- Inserir Livro ---")

        try:
            id_livro = int(input("ID do Livro: "))
            titulo = input("Título: ")
            data_pub = input("Data de Publicação (YYYY-MM-DD): ")
            preco = float(input("Preço: "))
            estoque = int(input("Quantidade Estoque: "))
            paginas = int(input("Número de páginas: "))

            print("\nSelecione uma Editora:")
            editoras = self.editora_dao.selecionar_todos()
            for e in editoras:
                print(e)

            id_editora = int(input("ID da Editora: "))

            print("\nSelecione um Autor:")
            autores = self.autor_dao.selecionar_todos()
            for a in autores:
                print(a)

            id_autor = int(input("ID do Autor: "))

            livro = Livro(
                idLivro=id_livro,
                tituloLivro=titulo,
                dataPublicacaoLivro=data_pub,
                precoLivro=preco,
                estoqueLivro=estoque,
                paginasLivro=paginas,
                Autor_idAutor=id_autor,
                Editora_idEditora=id_editora
            )

            self.livro_dao.inserir(livro)

        except ValueError:
            print("Valores inválidos.")

    def listar(self):
        livros = self.livro_dao.selecionar_todos()
        if livros:
            for l in livros:
                print(l)
        else:
            print("Nenhum livro encontrado.")

    def atualizar(self):
        self.listar()
        try:
            id_livro = int(input("ID do Livro a atualizar: "))
            livro = self.livro_dao.selecionar_por_id(id_livro)

            if livro:
                novo_titulo = input(f"Título ({livro.tituloLivro}): ") or livro.tituloLivro
                novo_preco = float(input(f"Preço ({livro.precoLivro}): ") or livro.precoLivro)

                livro.tituloLivro = novo_titulo
                livro.precoLivro = novo_preco
                self.livro_dao.atualizar(livro)

            else:
                print("Livro não encontrado.")

        except ValueError:
            print("Erro: valores inválidos.")

    def excluir(self):
        try:
            id_livro = int(input("ID do livro para excluir: "))
            self.livro_dao.deletar(id_livro)
        except ValueError:
            print("ID inválido.")
