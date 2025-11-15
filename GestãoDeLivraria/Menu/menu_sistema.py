from menu_autores import MenuAutores
from menu_editoras import MenuEditoras
from menu_livros import MenuLivros
from menu_clientes import MenuClientes
from menu_pedidos import MenuPedidos
from menu_consultas import MenuConsultas


class MenuSistema:
    def __init__(self):
        self.menu_autores = MenuAutores()
        self.menu_editoras = MenuEditoras()
        self.menu_livros = MenuLivros()
        self.menu_clientes = MenuClientes()
        self.menu_pedidos = MenuPedidos()
        self.menu_consultas = MenuConsultas()
        self.opcoes = {
            "1": ("Gerenciar Autores", self.menu_autores.exibir_menu),
            "2": ("Gerenciar Editoras", self.menu_editoras.exibir_menu),
            "3": ("Gerenciar Livros", self.menu_livros.exibir_menu),
            "4": ("Gerenciar Clientes", self.menu_clientes.exibir_menu),
            "5": ("Gerenciar Pedidos", self.menu_pedidos.exibir_menu),
            "6": ("Consultas com JOINs", self.menu_consultas.exibir_menu),
            "0": ("Sair", None)
        }

    def exibir_menu_principal(self):
        while True:
            print("\n" + "=" * 50)
            print("SISTEMA DE GERENCIAMENTO DA LIVRARIA")
            print("=" * 50)

            for key, (descricao, _) in self.opcoes.items():
                print(f"{key}. {descricao}")

            print("=" * 50)
            opcao = input("Escolha uma opção: ")

            if opcao == "0":
                print("Saindo do sistema...")
                break
            elif opcao in self.opcoes:
                if self.opcoes[opcao][1]:
                    self.opcoes[opcao][1]()
            else:
                print("Opção inválida! Tente novamente.")