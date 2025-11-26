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
            print("2. Listar Livros (Base)")
            print("3. Atualizar Livro")
            print("4. Excluir Livro")
            print("--- Relatórios (JOINs Simples) ---")
            print("5. Listar Livros com Autores")
            print("6. Listar Livros com Editoras")
            print("7. Listar Livros com Detalhes")
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
            elif opcao == "5":
                self.listar_livros_e_autores() # NOVO
            elif opcao == "6":
                self.listar_livros_e_editoras() # NOVO
            elif opcao == "7":
                self.listar_detalhes_do_livro() # NOVO
            elif opcao == "0":
                break
            else:
                print("Opção inválida.")
    
    # ... (inserir, listar, atualizar, excluir methods)

    # ---------------- NOVOS MÉTODOS DE RELATÓRIO ----------------

    def listar_livros_e_autores(self):
        print("\n--- Listar Livros e Autores ---")
        resultados = self.livro_dao.selecionar_livros_e_autores()
        if resultados:
            for item in resultados:
                print(f"Título: {item['Titulo']} | Autor: {item['Autor']} ({item['Nacionalidade']})")
        else:
            print("Nenhum resultado encontrado.")

    def listar_livros_e_editoras(self):
        print("\n--- Listar Livros e Editoras ---")
        resultados = self.livro_dao.selecionar_livros_e_editoras()
        if resultados:
            for item in resultados:
                print(f"Título: {item['Titulo']} | Publicação: {item['Publicacao']} | Editora: {item['Editora']} ({item['Local']})")
        else:
            print("Nenhum resultado encontrado.")

    def listar_detalhes_do_livro(self):
        print("\n--- Listar Livros e Detalhes ---")
        resultados = self.livro_dao.selecionar_detalhes_do_livro()
        if resultados:
            for item in resultados:
                print(f"Título: {item['Titulo']} | Idioma: {item['Idioma']} | Páginas: {item['Paginas_Detalhe']}")
                print(f"  Sinopse: {item['Sinopse'][:50]}...")
        else:
            print("Nenhum resultado encontrado.")