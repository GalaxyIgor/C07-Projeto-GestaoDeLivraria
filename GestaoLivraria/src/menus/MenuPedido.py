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
            while True:
                print("\n--- Menu de Pedidos ---")
                print("1. Criar Pedido")
                print("2. Listar Pedidos (Base)")
                print("3. Atualizar Pedido")
                print("4. Excluir Pedido")
                print("--- Relatórios (JOINs Compostos) ---")
                print("5. Resumo de Todos os Pedidos (Cliente/Valor)")
                print("6. Detalhes de Livros em um Pedido (por ID)")
                print("7. Listar Pedidos de um Cliente (por ID)")
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
                    self.listar_resumo_pedidos() # NOVO
                elif opcao == "6":
                    self.listar_livros_por_pedido() # NOVO
                elif opcao == "7":
                    self.listar_pedidos_por_cliente() # NOVO
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
                
                print("Livro adicionado ao pedgido.")
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
            
    def listar_resumo_pedidos(self):
        print("\n--- Resumo de Todos os Pedidos ---")
        resultados = self.pedido_dao.selecionar_resumo_pedidos()
        if resultados:
            for item in resultados:
                print(f"ID Pedido: {item['ID_Pedido']} | Data: {item['Data']} | Cliente: {item['Cliente']} | Valor: R$ {item['Valor_Total']:.2f}")
        else:
            print("Nenhum pedido encontrado.")

    def listar_livros_por_pedido(self):
        try:
            id_pedido = int(input("ID do Pedido para detalhar os livros: "))
            resultados = self.pedido_dao.selecionar_livros_por_pedido(id_pedido)
            
            if resultados:
                print(f"\n--- Livros no Pedido {id_pedido} ---")
                for item in resultados:
                    subtotal = item['Quantidade'] * item['Preco_Unitario']
                    print(f"Livro: {item['Livro']} | Qtd: {item['Quantidade']} | Preço Un: R$ {item['Preco_Unitario']:.2f} | Subtotal: R$ {subtotal:.2f}")
            else:
                print(f"Pedido {id_pedido} não encontrado ou sem itens.")
        except ValueError:
            print("ID inválido.")

    def listar_pedidos_por_cliente(self):
        try:
            id_cliente = int(input("ID do Cliente para listar os pedidos: "))
            cliente = self.cliente_dao.selecionar_por_id(id_cliente)
            
            if cliente:
                resultados = self.pedido_dao.selecionar_pedidos_por_cliente(id_cliente)
                print(f"\n--- Pedidos do Cliente: {cliente.nomeCliente} ---")
                if resultados:
                    for item in resultados:
                        print(f"ID Pedido: {item['ID_Pedido']} | Data: {item['Data']} | Valor: R$ {item['Valor_Total']:.2f}")
                else:
                    print("Nenhum pedido encontrado para este cliente.")
            else:
                print("Cliente não encontrado.")
        except ValueError:
            print("ID inválido.")