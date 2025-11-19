import sys
import os

# Adiciona o diretório 'src' ao sys.path1
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from menu.MenuAutor import MenuAutor

def main():
    """
    Função principal que inicia a aplicação.
    """
    while True:
        print("\n--- Menu Principal ---")
        print("1. Gerenciar Autores")
        print("2. Gerenciar Clientes")
        print("3. Gerenciar Editoras")
        print("4. Gerenciar Livros")
        print("5. Gerenciar Pedidos")
        print("0. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            menu_autor = MenuAutor()
            menu_autor.exibir_menu()
        elif opcao == '0':
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
