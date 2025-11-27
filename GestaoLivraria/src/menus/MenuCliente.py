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
            self.cliente_dao.insert(cliente)

        except ValueError:
            print("ID deve ser inteiro.")
            

    def listar(self):
            clientes = self.cliente_dao.selecionar_todos()
            if clientes:
                print("\n--- Lista de Clientes ---")
                print("-" * 115)
                print(f"{'ID':<4} {'NOME':<30} {'EMAIL':<40} {'TELEFONE':<15} {'PREMIUM':<10}")
                print("-" * 115)
                for cliente in clientes:
                    email_curto = cliente.emailCliente[:37] + '...' if len(cliente.emailCliente) > 40 else cliente.emailCliente
                    nome_curto = cliente.nomeCliente[:27] + '...' if len(cliente.nomeCliente) > 30 else cliente.nomeCliente
                    
                    print(
                        f"{cliente.idCliente:<4} "
                        f"{nome_curto:<30} "
                        f"{email_curto:<40} "
                        f"{cliente.telefoneCliente:<15} "
                        f"{'SIM' if cliente.premiumCliente else 'NÃO':<10}"
                    )
                print("-" * 115)
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
