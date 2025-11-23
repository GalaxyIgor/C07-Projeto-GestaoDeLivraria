from src.utils.conection import Conexao
from mysql.connector import Error
from src.models.pedido import Pedido



class PedidoLivroDAO:

    def __init__(self):
        self.db = Conexao()

    def adicionar_livro_pedido(self, idPedido, idLivro, idEditora, quantidade):

        sql = """
            INSERT INTO Pedido_has_Livro 
                (Pedido_idPedido, Livro_idLivro, Livro_Editora_idEditora, quantidade)
            VALUES (%s, %s, %s, %s)
        """

        try:
            conn = self.db.conectar()
            cursor = conn.cursor()

            cursor.execute(sql, (idPedido, idLivro, idEditora, quantidade))
            conn.commit()

        except Error as e:
            raise Exception(f"Erro ao adicionar livro ao pedido: {e}")

        finally:
            self.db.fechar()
