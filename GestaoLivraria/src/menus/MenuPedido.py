from src.models.pedido import Pedido
from src.dao.dao_pedido import PedidoDAO
from src.dao.dao_cliente import ClienteDAO
from src.dao.dao_livro import LivroDAO


class MenuPedido:

    def __init__(self):
        self.pedido_dao = PedidoDAO()
        self.cliente_dao = ClienteDAO()
        self.livro_dao = LivroDAO()

    def exibir_menu(self):
        while True:
            print("\n--- Menu de Pedidos ---")
            print("1. Criar Pedido")
            print("2. Listar Pedidos")
            print("3. Atualizar Pedido")
            print("4. Excluir Pedido")
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
        print("\n--- Criar Pedido ---")

        clientes = self.cliente_dao.selecionar_todos()
        livros = self.livro_dao.selecionar_todos()

        print("\nClientes:")
        for c in clientes:
            print(c)

        id_cliente = int(input("ID do cliente: "))

        print("\nLivros disponíveis:")
        for l in livros:
            print(l)

        id_livro = int(input("ID do livro: "))
        qtd = int(input("Quantidade: "))

        pedido = Pedido(idCliente=id_cliente, idLivro=id_livro, quantidade=qtd)
        self.pedido_dao.inserir(pedido)

    def listar(self):
        pedidos = self.pedido_dao.selecionar_todos()
        if pedidos:
            for p in pedidos:
                print(p)
        else:
            print("Nenhum pedido encontrado.")

    def atualizar(self):
        self.listar()
        try:
            id_pedido = int(input("ID do pedido a atualizar: "))
            pedido = self.pedido_dao.selecionar_por_id(id_pedido)

            if pedido:
                nova_qtd = int(input(f"Quantidade ({pedido.quantidade}): ") or pedido.quantidade)
                pedido.quantidade = nova_qtd
                self.pedido_dao.atualizar(pedido)
            else:
                print("Pedido não encontrado.")

        except ValueError:
            print("Valores inválidos.")

    def excluir(self):
        try:
            id_pedido = int(input("ID do pedido a excluir: "))
            self.pedido_dao.deletar(id_pedido)
        except ValueError:
            print("ID inválido.")
