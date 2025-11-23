from src.models.autor import Autor
from src.dao.dao_autor import AutorDAO


class MenuAutor:

    def __init__(self):
        self.autor_dao = AutorDAO()

    def exibir_menu(self):
        while True:
            print("\n--- Menu de Gerenciamento de Autores ---")
            print("1. Inserir Novo Autor")
            print("2. Listar Todos os Autores")
            print("3. Atualizar Autor")
            print("4. Excluir Autor")
            print("0. Voltar ao Menu Principal")

            opcao = input("Escolha uma opção: ")

            if opcao == '1':
                self.inserir_autor()
            elif opcao == '2':
                self.listar_autores()
            elif opcao == '3':
                self.atualizar_autor()
            elif opcao == '4':
                self.excluir_autor()
            elif opcao == '0':
                break
            else:
                print("Opção inválida. Tente novamente.")

    def inserir_autor(self):
        print("\n--- Inserir Autor ---")
        try:
            id_novo = int(input("ID do Autor (deve ser único): "))
            nome = input("Nome do Autor: ")
            nacionalidade = input("Nacionalidade: ")
            novo_autor = Autor(idAutor=id_novo,nomeAutor=nome, nacionalidadeAutor=nacionalidade)
            
            self.autor_dao.insert(novo_autor)
            
        except ValueError:
            print("ID deve ser um número inteiro.")

    def listar_autores(self):
        autores = self.autor_dao.selecionar_todos()
        if autores:
            print("\n--- Lista de Autores ---")
            for autor in autores:
                print(autor)
        else:
            print("Nenhum autor encontrado.")

    def atualizar_autor(self):
        self.listar_autores()  # Ajuda o usuário a ver os IDs
        try:
            id_autor = int(input("ID do Autor que deseja atualizar: "))
            autor_existente = self.autor_dao.selecionar_por_id(id_autor)

            if autor_existente:
                print(f"Autor atual: {autor_existente}")
                novo_nome = input(f"Novo Nome (atual: {autor_existente.nomeAutor}): ")
                nova_nacionalidade = input(f"Nova Nacionalidade (atual: {autor_existente.nacionalidadeAutor}): ")

                # Prepara o objeto para a atualização
                autor_existente.setNomeAutor(novo_nome or autor_existente.nomeAutor)
                autor_existente.nacionalidadeAutor = nova_nacionalidade or autor_existente.nacionalidadeAutor

                self.autor_dao.atualizar(autor_existente)
            else:
                print(f"Autor com ID {id_autor} não encontrado.")
        except ValueError:
            print("ID inválido.")

    def excluir_autor(self):
        self.listar_autores()  # Ajuda o usuário a ver os IDs
        try:
            id_autor = int(input("ID do Autor que deseja EXCLUIR: "))
            self.autor_dao.deletar(id_autor)
        except ValueError:
            print("ID inválido.")
