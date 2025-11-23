from utils.conection import Conexao
from mysql.connector import Error
from models.cliente import Cliente


class ClienteDAO:

    def __init__(self):
        self.db = Conexao()

    # ---------------- INSERT ----------------
    def insert(self, cliente: Cliente):
        sql = """
            INSERT INTO Cliente (idCliente, nomeCliente, emailCliente, telefoneCliente, premiumCliente)
            VALUES (%s, %s, %s, %s, %s)
        """
        try:
            conn = self.db.conectar()
            cursor = conn.cursor()

            valores = (
                cliente.idCliente,
                cliente.nomeCliente,
                cliente.emailCliente,
                cliente.telefoneCliente,
                cliente.premiumCliente
            )

            cursor.execute(sql, valores)
            conn.commit()
            print("Cliente inserido com sucesso!")

        except Error as e:
            raise Exception(f"Erro ao inserir cliente: {e}")
        finally:
            self.db.fechar()

    # ---------------- SELECT ALL ----------------
    def selecionar_todos(self):
        sql = """
            SELECT idCliente, nomeCliente, emailCliente, telefoneCliente, premiumCliente
            FROM Cliente
        """
        clientes = []

        try:
            conn = self.db.conectar()
            cursor = conn.cursor()
            cursor.execute(sql)

            for row in cursor.fetchall():
                cliente = Cliente(
                    idCliente=row[0],
                    nomeCliente=row[1],
                    emailCliente=row[2],
                    telefoneCliente=row[3],
                    premiumCliente=bool(row[4])
                )
                clientes.append(cliente)

            return clientes

        except Error as e:
            print(f"Erro ao selecionar clientes: {e}")
            return []
        finally:
            self.db.fechar()

    # ---------------- SELECT BY ID ----------------
    def selecionar_por_id(self, idCliente: int):
        sql = """
            SELECT idCliente, nomeCliente, emailCliente, telefoneCliente, premiumCliente
            FROM Cliente WHERE idCliente = %s
        """
        try:
            conn = self.db.conectar()
            cursor = conn.cursor()
            cursor.execute(sql, (idCliente,))
            row = cursor.fetchone()

            if row:
                return Cliente(
                    idCliente=row[0],
                    nomeCliente=row[1],
                    emailCliente=row[2],
                    telefoneCliente=row[3],
                    premiumCliente=bool(row[4])
                )
            return None

        except Error as e:
            print(f"Erro ao buscar cliente: {e}")
            return None
        finally:
            self.db.fechar()

    # ---------------- UPDATE ----------------
    def atualizar(self, cliente: Cliente):
        sql = """
            UPDATE Cliente
            SET nomeCliente = %s,
                emailCliente = %s,
                telefoneCliente = %s,
                premiumCliente = %s
            WHERE idCliente = %s
        """
        try:
            conn = self.db.conectar()
            cursor = conn.cursor()

            valores = (
                cliente.nomeCliente,
                cliente.emailCliente,
                cliente.telefoneCliente,
                cliente.premiumCliente,
                cliente.idCliente
            )

            cursor.execute(sql, valores)
            conn.commit()
            print("Cliente atualizado com sucesso!")

        except Error as e:
            print(f"Erro ao atualizar cliente: {e}")
        finally:
            self.db.fechar()

    # ---------------- DELETE ----------------
    def deletar(self, idCliente: int):
        sql = "DELETE FROM Cliente WHERE idCliente = %s"

        try:
            conn = self.db.conectar()
            cursor = conn.cursor()
            cursor.execute(sql, (idCliente,))
            conn.commit()
            print("Cliente deletado com sucesso!")

        except Error as e:
            print(f"Erro ao deletar cliente: {e}")
        finally:
            self.db.fechar()
