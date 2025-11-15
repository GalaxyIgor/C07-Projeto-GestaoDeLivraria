from menu_sistema import MenuSistema

def main():
    print("Iniciando Sistema de Gerenciamento da Livraria...")
    sistema = MenuSistema()
    sistema.exibir_menu_principal()

if __name__ == "__main__":
    main()