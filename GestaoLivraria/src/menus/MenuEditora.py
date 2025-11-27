from src.models.editora import Editora
from src.dao.dao_editora import EditoraDAO


class MenuEditora:

    def __init__(self):
        self.editora_dao = EditoraDAO()

    def exibir_menu(self):
        while True:
            print("\n--- Menu de Gerenciamento de Editoras ---")
            print("1. Inserir Nova Editora")
            print("2. Listar Todas as Editoras")
            print("3. Atualizar Editora")
            print("4. Excluir Editora")
            print("0. Voltar ao Menu Principal")

            opcao = input("Escolha uma opção: ")

            if opcao == '1':
                self.inserir_editora()
            elif opcao == '2':
                self.listar_editoras()
            elif opcao == '3':
                self.atualizar_editora()
            elif opcao == '4':
                self.excluir_editora()
            elif opcao == '0':
                break
            else:
                print("Opção inválida. Tente novamente.")

    def inserir_editora(self):
        print("\n--- Inserir Editora ---")
        try:
            id_editora = int(input("ID da Editora: "))
            nome = input("Nome da Editora: ")
            cnpj = input("CNPJ: ")
            local = input("Local da Editora: ")

            nova = Editora(idEditora=id_editora, nomeEditora=nome,
                           cnpjEditora=cnpj, localEditora=local)

            self.editora_dao.insert(nova)
            print("Editora inserida com sucesso!")

        except ValueError:
            print("ID deve ser um número.")


    def listar_editoras(self):
            editoras = self.editora_dao.selecionar_todos()
            if editoras:
                print("\n--- Lista de Editoras ---")
                print("-" * 80)
                print(f"{'ID':<4} {'NOME DA EDITORA':<30} {'CNPJ':<20} {'LOCAL':<20}")
                print("-" * 80)
                for ed in editoras:
                    nome_curto = ed.nomeEditora[:27] + '...' if len(ed.nomeEditora) > 30 else ed.nomeEditora
                    print(
                        f"{ed.idEditora:<4} "
                        f"{nome_curto:<30} "
                        f"{ed.cnpjEditora:<20} "
                        f"{ed.localEditora:<20}"
                    )
                print("-" * 80)
            else:
                print("Nenhuma editora encontrada.") 
    def atualizar_editora(self):
        self.listar_editoras()
        try:
            id_editora = int(input("ID da Editora a atualizar: "))
            atual = self.editora_dao.selecionar_por_id(id_editora)

            if atual:
                print(f"Editora atual: {atual}")

                novo_nome = input(f"Nome ({atual.nomeEditora}): ") or atual.nomeEditora
                novo_cnpj = input(f"CNPJ ({atual.cnpjEditora}): ") or atual.cnpjEditora
                novo_local = input(f"Local ({atual.localEditora}): ") or atual.localEditora

                atual.nomeEditora = novo_nome
                atual.cnpjEditora = novo_cnpj
                atual.localEditora = novo_local

                self.editora_dao.atualizar(atual)
            else:
                print("Editora não encontrada.")

        except ValueError:
            print("ID inválido.")

    def excluir_editora(self):
        self.listar_editoras()
        try:
            id_editora = int(input("ID da Editora para excluir: "))
            self.editora_dao.deletar(id_editora)
        except ValueError:
            print("ID inválido.")
