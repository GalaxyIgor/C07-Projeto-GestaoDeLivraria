import mysql.connector
from mysql.connector import Error


class Conexao:
    
    def __init__(self):
        self.conexao = None
        self.HOST = "localhost"
        self.DATABASE = "livraria"
        self.USER = "root"    
        self.PASSWORD = "123123"
        self.PORT = 3306     
    
    def conectar(self):
        try:
            self.conexao = mysql.connector.connect(
                host=self.HOST,
                database=self.DATABASE,
                user=self.USER,
                password=self.PASSWORD,
                port=self.PORT
            )
            print("Conexão estabelecida!")
            return self.conexao
        except Error as e:
            print(f"Erro ao conectar: {e}")
            return None
    
    def fechar(self):
        if self.conexao and self.conexao.is_connected():
            self.conexao.close()
            print("Conexão encerrada.")


if __name__ == "__main__":
    conexao = Conexao()
    conn = conexao.conectar()
    
    if conn:
        print(f"Status da conexão: {conn.is_connected()}")
        conexao.fechar()
