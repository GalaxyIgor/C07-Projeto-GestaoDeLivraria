from src.models.pedido import Pedido
from src.dao.dao_pedido import PedidoDAO
from src.dao.dao_cliente import ClienteDAO
from src.dao.dao_livro import LivroDAO
from src.dao.dao_cliente_has_pedido import ClientePedidoDAO 
from src.dao.dao_pedido_has_livro import PedidoLivroDAO
from datetime import datetime



class MenuPedido:

    def __init__(self):
        self.pedido_dao = PedidoDAO()
        self.cliente_dao = ClienteDAO()
        self.livro_dao = LivroDAO()
        self.cliente_pedido_dao = ClientePedidoDAO()
        self.pedido_livro_dao = PedidoLivroDAO()
        
    def exibir_menu(self):
        # ... (Mantido sem alterações)
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

        try:
            # 1. Criação do Pedido (Valor inicial 0.0)
            
            id_pedido = int(input("ID do Pedido (deve ser único): "))
            data = datetime.now().strftime("%Y-%m-%d")
            
            # Inicializa o pedido com valor zero, que será calculado ao adicionar itens
            
            novo_pedido = Pedido(idPedido=id_pedido,
                                 dataPedido=data, 
                                 valorTotal=0.0
                                 )
            
            self.pedido_dao.insert(novo_pedido)
            print(f"Pedido {id_pedido} criado com sucesso!")

            # 2. Vínculo Cliente-Pedido
            clientes = self.cliente_dao.selecionar_todos()
            
            print("\nClientes:")
            for cliente in clientes:
                print(cliente)
                
            id_cliente = int(input("ID do cliente: "))
            self.cliente_pedido_dao.vincular_cliente_pedido(id_cliente, id_pedido)
            print("Cliente vinculado ao pedido.")


            # 3. Adicionar Livro (e calcular valor)
            
            livros = self.livro_dao.selecionar_todos()
            print("\nLivros disponíveis:")
            for livro in livros:
                print(livro)

            id_livro = int(input("ID do livro a adicionar: "))
            qtd = int(input("Quantidade: "))

            livro_selecionado = self.livro_dao.selecionar_por_id(id_livro)

            if livro_selecionado:
                id_editora = livro_selecionado.Editora_idEditora
                
                self.pedido_livro_dao.adicionar_livro_pedido(id_pedido, id_livro, id_editora, qtd)
                
                # Calcula o valor total e atualiza o Pedido
                valor_do_item = float(livro_selecionado.precoLivro) * qtd
                novo_pedido.valorTotal = valor_do_item
                self.pedido_dao.atualizar(novo_pedido) 
                
                print("Livro adicionado ao pedido.")
                print(f"Valor total do pedido atualizado para: R$ {valor_do_item:.2f}")

            else:
                print("Livro não encontrado. Item do pedido não adicionado.")
            
            print("Processo de Pedido finalizado.")

        except ValueError:
            print("Valores de ID, Data ou Quantidade inválidos.")
        except Exception as e:
            print(f"Erro no processo de inserção do pedido: {e}")

    def listar(self):
        # O SELECT ALL do PedidoDAO foi simplificado para listar os dados da tabela Pedido.
        # Para listar o resumo completo (como a VIEW no SQL), seria necessário um JOIN.
        pedidos = self.pedido_dao.selecionar_todos()
        if pedidos:
            for p in pedidos:
                print(p)
        else:
            print("Nenhum pedido encontrado.")

    def atualizar(self):
        # ... (Atualizado para refletir o novo DAO de Pedido)
        self.listar()
        try:
            id_pedido = int(input("ID do pedido a atualizar: "))
            pedido = self.pedido_dao.selecionar_por_id(id_pedido)

            if pedido:
                # Agora só atualizamos campos que estão na tabela Pedido
                novo_valor = float(input(f"Valor Total ({pedido.valorTotal}): ") or pedido.valorTotal)
                # O campo dataPedido também pode ser atualizado se necessário.

                pedido.valorTotal = novo_valor
                self.pedido_dao.atualizar(pedido)
            else:
                print("Pedido não encontrado.")

        except ValueError:
            print("Valores inválidos.")

    def excluir(self):
        # ... (Mantido sem alterações, o DELETE do DAO de Pedido foi mantido simples)
        try:
            id_pedido = int(input("ID do pedido a excluir: "))
            self.pedido_dao.deletar(id_pedido)
        except ValueError:
            print("ID inválido.")