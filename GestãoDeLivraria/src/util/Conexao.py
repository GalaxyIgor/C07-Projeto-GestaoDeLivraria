# src/util/Conexao.py

import mysql.connector
from mysql.connector import Error


class Conexao:
    """
    Gerencia a conexão com o banco de dados MySQL para a Livraria.
    """
    
    # --- Configurações do Banco de Dados ---
    HOST = 'localhost'
    DATABASE = 'livraria'
    USER = 'root'
    PASSWORD = 'SUA_SENHA_AQUI'
    PORT = 3306

    def __init__(self):
        """Inicializa a conexão como None."""
        self.conexao = None

    def conectar(self):
        """Estabelece e retorna o objeto de conexão."""
        try:
            # Cria a conexão usando as credenciais definidas na classe
            self.conexao = mysql.connector.connect(
                host=self.HOST,
                database=self.DATABASE,
                user=self.USER,
                password=self.PASSWORD,
                port=self.PORT
            )
            if self.conexao.is_connected():
                print("Conexão com o MySQL estabelecida com sucesso!")
                return self.conexao

        except Error as e:
            print(f"Erro ao conectar ao MySQL: {e}")
            return None

    def fechar_conexao(self):
        """Fecha a conexão com o banco de dados, se estiver aberta."""
        if self.conexao and self.conexao.is_connected():
            self.conexao.close()
            print("Conexão MySQL encerrada.")