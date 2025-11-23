from src.utils.conection import Conexao
from mysql.connector import Error
from src.models.pedido import Pedido



class ClientePedidoDAO:

    def __init__(self):
        self.db = Conexao()

    def vincular_cliente_pedido(self, idCliente, idPedido):

        sql = """
            INSERT INTO Cliente_has_Pedido (Cliente_idCliente, Pedido_idPedido)
            VALUES (%s, %s)
        """

        try:
            conn = self.db.conectar()
            cursor = conn.cursor()

            cursor.execute(sql, (idCliente, idPedido))
            conn.commit()

        except Error as e:
            raise Exception(f"Erro ao vincular cliente ao pedido: {e}")

        finally:
            self.db.fechar()
