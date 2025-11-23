from src.models.cliente import Cliente
from src.dao.dao_cliente import ClienteDAO


class MenuCliente:

    def __init__(self):
        self.cliente_dao = ClienteDAO()

    def exibir_menu(self):
        while True:
            print("\n--- Menu de Clientes ---")
            print("1. Inserir Cliente")
            print("2. Listar Clientes")
            print("3. Atualizar Cliente")
            print("4. Excluir Cliente")
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
        try:
            idc = int(input("ID Cliente: "))
            nome = input("Nome: ")
            email = input("Email: ")
            telefone = input("Telefone: ")

            cliente = Cliente(idCliente=idc, nomeCliente=nome, emailCliente=email, telefoneCliente=telefone)
            self.cliente_dao.inserir(cliente)

        except ValueError:
            print("ID deve ser inteiro.")

    def listar(self):
        clientes = self.cliente_dao.selecionar_todos()
        if clientes:
            for c in clientes:
                print(c)
        else:
            print("Nenhum cliente encontrado.")

    def atualizar(self):
        self.listar()
        try:
            idc = int(input("ID do cliente a atualizar: "))
            cliente = self.cliente_dao.selecionar_por_id(idc)

            if cliente:
                novo_nome = input(f"Nome ({cliente.nomeCliente}): ") or cliente.nomeCliente
                novo_email = input(f"Email ({cliente.emailCliente}): ") or cliente.emailCliente
                novo_tel = input(f"Telefone ({cliente.telefoneCliente}): ") or cliente.telefoneCliente

                cliente.nomeCliente = novo_nome
                cliente.emailCliente = novo_email
                cliente.telefoneCliente = novo_tel

                self.cliente_dao.atualizar(cliente)
            else:
                print("Cliente não encontrado.")

        except ValueError:
            print("ID inválido.")

    def excluir(self):
        try:
            idc = int(input("ID do cliente a excluir: "))
            self.cliente_dao.deletar(idc)
        except ValueError:
            print("ID inválido.")
