from src.utils.conection import Conexao
from mysql.connector import Error
from src.models.editora import Editora


class EditoraDAO:

    def __init__(self):
        self.db = Conexao()

    # ---------------- INSERT ----------------
    def insert(self, editora: Editora):
        sql = """
            INSERT INTO Editora (idEditora, nomeEditora, cnpjEditora, LocalEditora)
            VALUES (%s, %s, %s, %s)
        """

        try:
            conn = self.db.conectar()
            cursor = conn.cursor()

            valores = (
                editora.idEditora,
                editora.nomeEditora,
                editora.cnpjEditora,
                editora.LocalEditora
            )

            cursor.execute(sql, valores)
            conn.commit()
            print("Editora inserida com sucesso!")

        except Error as e:
            raise Exception(f"Erro ao inserir editora: {e}")
        finally:
            self.db.fechar()

    # ---------------- SELECT ALL ----------------
    def selecionar_todos(self):
        sql = """
            SELECT idEditora, nomeEditora, cnpjEditora, LocalEditora
            FROM Editora
        """
        editoras = []

        try:
            conn = self.db.conectar()
            cursor = conn.cursor()
            cursor.execute(sql)

            for row in cursor.fetchall():
                editoras.append(Editora(
                    idEditora=row[0],
                    nomeEditora=row[1],
                    cnpjEditora=row[2],
                    LocalEditora=row[3]
                ))

            return editoras

        except Error as e:
            print(f"Erro ao selecionar editoras: {e}")
            return []
        finally:
            self.db.fechar()

    # ---------------- SELECT BY ID ----------------
    def selecionar_por_id(self, idEditora: int):
        sql = """
            SELECT idEditora, nomeEditora, cnpjEditora, LocalEditora
            FROM Editora WHERE idEditora = %s
        """
        try:
            conn = self.db.conectar()
            cursor = conn.cursor()
            cursor.execute(sql, (idEditora,))
            row = cursor.fetchone()

            if row:
                return Editora(
                    idEditora=row[0],
                    nomeEditora=row[1],
                    cnpjEditora=row[2],
                    LocalEditora=row[3]
                )
            return None

        except Error as e:
            print(f"Erro ao buscar editora: {e}")
            return None
        finally:
            self.db.fechar()

    # ---------------- UPDATE ----------------
    def atualizar(self, editora: Editora):
        sql = """
            UPDATE Editora
            SET nomeEditora = %s,
                cnpjEditora = %s,
                LocalEditora = %s
            WHERE idEditora = %s
        """

        try:
            conn = self.db.conectar()
            cursor = conn.cursor()

            valores = (
                editora.nomeEditora,
                editora.cnpjEditora,
                editora.LocalEditora,
                editora.idEditora
            )

            cursor.execute(sql, valores)
            conn.commit()
            print("Editora atualizada com sucesso!")

        except Error as e:
            print(f"Erro ao atualizar editora: {e}")
        finally:
            self.db.fechar()

    # ---------------- DELETE ----------------
    def deletar(self, idEditora: int):
        sql = "DELETE FROM Editora WHERE idEditora = %s"

        try:
            conn = self.db.conectar()
            cursor = conn.cursor()
            cursor.execute(sql, (idEditora,))
            conn.commit()
            print("Editora deletada com sucesso!")

        except Error as e:
            print(f"Erro ao deletar editora: {e} — provavelmente existem livros vinculados.")
        finally:
            self.db.fechar()
