from src.models.livro import Livro
from src.dao.dao_livro import LivroDAO
from src.dao.dao_autor import AutorDAO
from src.dao.dao_editora import EditoraDAO
from datetime import date


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

            try:
                if opcao == "1":
                    self.inserir()
                elif opcao == "2":
                    self.listar()
                elif opcao == "3":
                    self.atualizar()
                elif opcao == "4":
                    self.excluir()
                elif opcao == "5":
                    self.listar_livros_e_autores()
                elif opcao == "6":
                    self.listar_livros_e_editoras()
                elif opcao == "7":
                    self.listar_detalhes_do_livro()
                elif opcao == "0":
                    break
                else:
                    print("Opção inválida.")
            except Exception as e:
                print(f"Ocorreu um erro na operação: {e}")

    # ==================== MÉTODOS CRUD ====================

    def inserir(self):
        print("\n--- Inserir Novo Livro ---")
        try:
            # Mostra as FKs disponíveis para facilitar a vida do usuário
            print("\n--- Autores Disponíveis ---")
            for autor in self.autor_dao.selecionar_todos():
                print(f"ID: {autor.idAutor} | Nome: {autor.nomeAutor}")

            print("\n--- Editoras Disponíveis ---")
            for editora in self.editora_dao.selecionar_todos():
                print(f"ID: {editora.idEditora} | Nome: {editora.nomeEditora}")

            # Obter Dados
            id_livro = int(input("ID do Livro (deve ser único): "))
            titulo = input("Título: ")

            # Tratamento de Data
            data_publicacao_str = input("Data de Publicação (AAAA-MM-DD): ")
            data_publicacao = date.fromisoformat(data_publicacao_str)

            preco = float(input("Preço: "))
            estoque = int(input("Estoque: "))
            paginas = int(input("Número de Páginas: "))

            # Obter FKs
            id_autor = int(input("ID do Autor: "))
            id_editora = int(input("ID da Editora: "))

            # Usando ID de Estoque fixo (ajuste se a lógica de estoque for mais complexa)
            id_estoque = 1

            # Criar e Inserir o Objeto Livro
            novo_livro = Livro(
                idLivro=id_livro,
                tituloLivro=titulo,
                DataPublicacaoLivro=data_publicacao,
                precoLivro=preco,
                estoqueLivro=estoque,
                PaginasLivro=paginas,
                Editora_idEditora=id_editora,
                Autor_idAutor=id_autor,
                EstoqueLivros_idEstoqueLivros=id_estoque
            )
            self.livro_dao.insert(novo_livro)

        except ValueError:
            print("Erro de Valor: IDs, Preço, Estoque e Páginas devem ser numéricos e a Data em AAAA-MM-DD.")
        except Exception as e:
            print(f"Erro ao inserir Livro: {e}")

    def listar(self):
        print("\n--- Listar Livros (Base) ---")
        livros = self.livro_dao.selecionar_todos()
        if livros:
            for livro in livros:
                print(livro)
        else:
            print("Nenhum livro encontrado na base de dados.")

    def atualizar(self):
        self.listar()
        print("\n--- Atualizar Livro ---")
        try:
            id_livro = int(input("ID do Livro para atualizar: "))
            livro_existente = self.livro_dao.selecionar_por_id(id_livro)

            if livro_existente:
                print(f"Livro atual: {livro_existente}")

                # Campos de texto (manter valor se input vazio)
                livro_existente.tituloLivro = input(
                    f"Novo Título ({livro_existente.tituloLivro}): ") or livro_existente.tituloLivro

                # Campos numéricos (converter se input não for vazio)
                novo_preco = input(f"Novo Preço ({livro_existente.precoLivro:.2f}): ")
                if novo_preco:
                    livro_existente.precoLivro = float(novo_preco)

                novo_estoque = input(f"Novo Estoque ({livro_existente.estoqueLivro}): ")
                if novo_estoque:
                    livro_existente.estoqueLivro = int(novo_estoque)

                nova_paginas = input(f"Novas Páginas ({livro_existente.PaginasLivro}): ")
                if nova_paginas:
                    livro_existente.PaginasLivro = int(nova_paginas)

                self.livro_dao.atualizar(livro_existente)
            else:
                print(f"Livro com ID {id_livro} não encontrado.")
        except ValueError:
            print("Erro de Valor: IDs e valores numéricos devem ser válidos.")
        except Exception as e:
            print(f"Erro ao atualizar Livro: {e}")

    def excluir(self):
        self.listar()
        print("\n--- Excluir Livro ---")
        try:
            id_livro = int(input("ID do Livro para excluir: "))
            self.livro_dao.deletar(id_livro)
        except ValueError:
            print("Erro: ID inválido.")
        except Exception as e:
            print(f"Erro ao excluir: {e}. (Verifique se o livro não está em um pedido).")

    # ==================== MÉTODOS DE RELATÓRIO (JOINs) ====================

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
                print(
                    f"Título: {item['Titulo']} | Publicação: {item['Publicacao']} | Editora: {item['Editora']} ({item['Local']})")
        else:
            print("Nenhum resultado encontrado.")

    def listar_detalhes_do_livro(self):
        print("\n--- Listar Livros e Detalhes ---")
        resultados = self.livro_dao.selecionar_detalhes_do_livro()
        if resultados:
            for item in resultados:
                print(
                    f"Título: {item['Titulo']} | Idioma: {item['Idioma']} | Páginas: {item['Paginas_Detalhe']} | Sinopse: {item['Sinopse']}")
        else:
            print("Nenhum resultado encontrado.")