from src.utils.conection import Conexao
from src.models.autor import Autor
from mysql.connector import Error


class AutorDAO:
    
    def __init__(self):
        self.db = Conexao()

    # ---------------- INSERT ----------------
    def insert(self, autor: Autor):
        sql = """
            INSERT INTO Autor (idAutor, nomeAutor, nacionalidadeAutor)
            VALUES (%s, %s, %s)
        """
        try:
            conn = self.db.conectar()
            cursor = conn.cursor()

            valores = (
                autor.idAutor,
                autor.nomeAutor,
                autor.nacionalidadeAutor
            )

            cursor.execute(sql, valores)
            conn.commit()
            print("Autor inserido com sucesso!")

        except Error as e:
            raise Exception(f"Erro ao inserir autor: {e}")
        finally:
            self.db.fechar()

    # ---------------- SELECT ALL ----------------
    def selecionar_todos(self):
        sql = "SELECT idAutor, nomeAutor, nacionalidadeAutor FROM Autor"
        autores = []
        try:
            conn = self.db.conectar()
            cursor = conn.cursor()
            cursor.execute(sql)
            for row in cursor.fetchall():
                autores.append(Autor(
                    idAutor=row[0],
                    nomeAutor=row[1],
                    nacionalidadeAutor=row[2]
                ))
            return autores

        except Error as e:
            print(f"Erro ao selecionar todos os autores: {e}")
            return []
        finally:
            self.db.fechar()

    # ---------------- SELECT BY ID ----------------
    def selecionar_por_id(self, idAutor: int):
        sql = "SELECT idAutor, nomeAutor, nacionalidadeAutor FROM Autor WHERE idAutor = %s"
        try:
            conn = self.db.conectar()
            cursor = conn.cursor()
            cursor.execute(sql, (idAutor,))
            row = cursor.fetchone()
            if row:
                return Autor(
                    idAutor=row[0],
                    nomeAutor=row[1],
                    nacionalidadeAutor=row[2]
                )
            return None

        except Error as e:
            print(f"Erro ao buscar autor por ID: {e}")
            return None
        finally:
            self.db.fechar()

    # ---------------- UPDATE ----------------
    def atualizar(self, autor: Autor):
        sql = """
            UPDATE Autor
            SET nomeAutor = %s, nacionalidadeAutor = %s
            WHERE idAutor = %s
        """
        try:
            conn = self.db.conectar()
            cursor = conn.cursor()
            valores = (autor.nomeAutor, autor.nacionalidadeAutor, autor.idAutor)
            cursor.execute(sql, valores)
            conn.commit()
            print("Autor atualizado com sucesso!")

        except Error as e:
            print(f"Erro ao atualizar autor: {e}")
        finally:
            self.db.fechar()

    # ---------------- DELETE ----------------
    def deletar(self, idAutor: int):
        sql = "DELETE FROM Autor WHERE idAutor = %s"
        try:
            conn = self.db.conectar()
            cursor = conn.cursor()
            cursor.execute(sql, (idAutor,))
            conn.commit()
            print("Autor deletado com sucesso!")

        except Error as e:
            print(f"Erro ao deletar autor: {e}")
        finally:
            self.db.fechar()
