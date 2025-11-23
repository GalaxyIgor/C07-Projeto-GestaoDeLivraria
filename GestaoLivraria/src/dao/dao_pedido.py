from src.utils.conection import Conexao
from mysql.connector import Error
from src.models.pedido import Pedido


class PedidoDAO:

    def __init__(self):
        self.db = Conexao()

    # ---------------- INSERT ----------------
    def insert(self, pedido: Pedido):
        sql = """
            INSERT INTO Pedido (
                idPedido, dataPedido, valorTotal
            )
            VALUES (%s, %s, %s)
        """

        try:
            conn = self.db.conectar()
            cursor = conn.cursor()

            valores = (
                pedido.idPedido,
                pedido.dataPedido,
                pedido.valorTotal 
            )

            cursor.execute(sql, valores)
            conn.commit()
            print("Pedido inserido com sucesso!")

        except Error as e:
            raise Exception(f"Erro ao inserir pedido: {e}")
        finally:
            self.db.fechar()

    # ---------------- SELECT ALL ----------------
    def selecionar_todos(self):
        sql = """
            SELECT idPedido, dataPedido, valorTotal
            FROM Pedido
        """
        pedidos = []

        try:
            conn = self.db.conectar()
            cursor = conn.cursor()
            cursor.execute(sql)

            for row in cursor.fetchall():
                pedidos.append(Pedido(
                    idPedido=row[0],
                    dataPedido=row[1],
                    valorTotal=float(row[2]) 
                ))

            return pedidos

        except Error as e:
            print(f"Erro ao selecionar pedidos: {e}")
            return []
        finally:
            self.db.fechar()

    # ---------------- SELECT BY ID ----------------
    def selecionar_por_id(self, idPedido: int):
        sql = """
            SELECT idPedido, dataPedido, valorTotal
            FROM Pedido WHERE idPedido = %s
        """

        try:
            conn = self.db.conectar()
            cursor = conn.cursor()
            cursor.execute(sql, (idPedido,))
            row = cursor.fetchone()

            if row:
                return Pedido(
                    idPedido=row[0],
                    dataPedido=row[1],
                    valorTotal=float(row[2])
                )
            return None

        except Error as e:
            print(f"Erro ao buscar pedido: {e}")
            return None
        finally:
            self.db.fechar()

    # ---------------- UPDATE ----------------
    def atualizar(self, pedido: Pedido):
        sql = """
            UPDATE Pedido SET
                dataPedido = %s,
                valorTotal = %s
            WHERE idPedido = %s
        """

        try:
            conn = self.db.conectar()
            cursor = conn.cursor()

            valores = (
                pedido.dataPedido,
                pedido.valorTotal,
                pedido.idPedido
            )

            cursor.execute(sql, valores)
            conn.commit()
            print("Pedido atualizado com sucesso!")

        except Error as e:
            print(f"Erro ao atualizar pedido: {e}")
        finally:
            self.db.fechar()

    # ---------------- DELETE ----------------
    def deletar(self, idPedido: int):
        sql = "DELETE FROM Pedido WHERE idPedido = %s"

        try:
            conn = self.db.conectar()
            cursor = conn.cursor()
            cursor.execute(sql, (idPedido,))
            conn.commit()
            print("Pedido deletado com sucesso!")

        except Error as e:
            print(f"Erro ao deletar pedido: {e}")
        finally:
            self.db.fechar()