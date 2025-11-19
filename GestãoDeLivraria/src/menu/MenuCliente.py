from src.dao.ClienteDAO import ClienteDAO
from src.model.Cliente import Cliente


class MenuAutor:

    def __init__(self):
        self.cliente_dao = ClienteDAO()

    def exibir_menu(self):
        while True:
            print("\n--- Menu de Gerenciamento de Clientes ---")
            print("1. Inserir Novo Cliente")
            print("2. Listar Todos os Clientes")
            print("3. Atualizar Cliente")
            print("4. Excluir Cliente")
            print("0. Voltar ao Menu Principal")

            opcao = input("Escolha uma opção: ")

            if opcao == '1':
                self.inserir_cliente()
            elif opcao == '2':
                self.listar_clientes()
            elif opcao == '3':
                self.atualizar_clientes()
            elif opcao == '4':
                self.excluir_cliente()
            elif opcao == '0':
                break
            else:
                print("Opção inválida. Tente novamente.")

    def inserir_cliente(self):
        print("\n--- Inserir Cliente ---")
        try:
            # Note: Em um projeto real, você buscaria o próximo ID ou usaria AUTO_INCREMENT.
            # Aqui, seguimos o seu modelo inicial de fornecer o ID.
            id_novo = int(input("ID do Cliente (deve ser único): "))
            nome = input("Nome do Cliente: ")
            nacionalidade = input("Nacionalidade: ")

            novo_cliente = Cliente(id_novo, nome, nacionalidade)
            self.cliente_dao.inserir(novo_cliente)
        except ValueError:
            print("ID deve ser um número inteiro.")

    def listar_clientes(self):
        clientes = self.cliente_dao.selecionar_todos()
        if clientes:
            print("\n--- Lista de Autores ---")
            for autor in clientes:
                print(autor)
        else:
            print("Nenhum autor encontrado.")

    def atualizar_cliente(self):
        self.listar_clientes()  # Ajuda o usuário a ver os IDs
        try:
            id_cliente = int(input("ID do Autor que deseja atualizar: "))
            cliente_existente = self.cliente_dao.selecionar_por_id(id_cliente)

            if cliente_existente:
                print(f"Cliente atual: {cliente_existente}")
                novo_nome = input(f"Novo Nome (atual: {cliente_existente.nomeCliente}): ")
                nova_nacionalidade = input(f"Nova Nacionalidade (atual: {cliente_existente.nacionalidadeCliente}): ")

                # Prepara o objeto para a atualização
                cliente_existente.setNomeCliente(novo_nome or cliente_existente.nomeCliente)
                cliente_existente.nacionalidadeCliente = nova_nacionalidade or cliente_existente.nacionalidadeCliente

                self.cliente_dao.atualizar(cliente_existente)
            else:
                print(f"Cliente com ID {id_cliente} não encontrado.")
        except ValueError:
            print("ID inválido.")

    def excluir_cliente(self):
        self.listar_clientes()  # Ajuda o usuário a ver os IDs
        try:
            id_cliente = int(input("ID do Cliente que deseja EXCLUIR: "))
            self.cliente_dao.deletar(id_cliente)
        except ValueError:
            print("ID inválido.")
