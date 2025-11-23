from src.menus.MenuAtor import MenuAutor
from src.menus.MenuEditora import MenuEditora
from src.menus.MenuCliente import MenuCliente
from src.menus.MenuLivro import MenuLivro
from src.menus.MenuPedido import MenuPedido



class MenuPrincipal:

    def __init__(self):
        self.menu_autor = MenuAutor()
        self.menu_editora = MenuEditora()
        self.menu_cliente = MenuCliente()
        self.menu_livro = MenuLivro()
        self.menu_pedido = MenuPedido()

    def exibir(self):
        while True:
            print("\n========== SISTEMA LIVRARIA ==========")
            print("1. Gerenciar Autores")
            print("2. Gerenciar Editoras")
            print("3. Gerenciar Clientes")
            print("4. Gerenciar Livros")
            print("5. Gerenciar Pedidos")
            print("0. Sair")
            print("======================================")

            opcao = input("Escolha uma opção: ")

            if opcao == '1':
                self.menu_autor.exibir_menu()
            elif opcao == '2':
                self.menu_editora.exibir_menu()
            elif opcao == '3':
                self.menu_cliente.exibir_menu()
            elif opcao == '4':
                self.menu_livro.exibir_menu()
            elif opcao == '5':
                self.menu_pedido.exibir_menu()
            elif opcao == '0':
                print("Encerrando o sistema...")
                break
            else:
                print("Opção inválida. Tente novamente.")



if __name__ == "__main__":
    menu = MenuPrincipal()
    menu.exibir()