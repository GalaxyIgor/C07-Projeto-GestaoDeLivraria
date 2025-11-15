import mysql.connector
from mysql.connector import Error


class DatabaseConfig:
    def __init__(self):
        self.host = 'localhost'
        self.database = 'livraria'
        self.user = 'joao'
        self.password = 'Joao@1234'

    def get_connection(self):
        try:
            connection = mysql.connector.connect(
                host=self.host,
                database=self.database,
                user=self.user,
                password=self.password
            )
            if connection.is_connected():
                return connection
        except Error as e:
            print(f"Erro ao conectar ao MySQL: {e}")
            return None