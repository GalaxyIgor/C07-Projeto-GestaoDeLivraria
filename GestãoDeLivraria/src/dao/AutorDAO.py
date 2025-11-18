from util.Conexao import Conexao
from model.Autor import Autor
import mysql.connector
from mysql.connector import Error


class AutorDAO:

    def __init__(self):
        self.db = Conexao()

    # --- C (Create): INSERT ---
    def inserir(self, autor: Autor):
        sql = "INSERT INTO Autor (idAutor, nomeAutor, nacionalidadeAutor) VALUES (%s, %s, %s)"
        # Note: O idAutor deve ser único. Se for AUTO_INCREMENT, ajuste a SQL e o método.
        # Estamos usando o ID fornecido como no seu script inicial.
        try:
            conn = self.db.conectar()
            cursor = conn.cursor()
            valores = (autor.idAutor, autor.nomeAutor, autor.nacionalidadeAutor)
            cursor.execute(sql, valores)
            conn.commit()
            print("Autor inserido com sucesso!")
        except Error as e:
            print(f"Erro ao inserir Autor: {e}")
        finally:
            self.db.fechar_conexao()

    # --- R (Read): SELECT ALL ---
    def selecionar_todos(self):
        sql = "SELECT idAutor, nomeAutor, nacionalidadeAutor FROM Autor"
        autores = []
        try:
            conn = self.db.conectar()
            cursor = conn.cursor()
            cursor.execute(sql)
            resultados = cursor.fetchall()

            for (idAutor, nomeAutor, nacionalidadeAutor) in resultados:
                autor = Autor(idAutor, nomeAutor, nacionalidadeAutor)
                autores.append(autor)
            return autores

        except Error as e:
            print(f"Erro ao selecionar todos os Autores: {e}")
            return []
        finally:
            self.db.fechar_conexao()

    # --- U (Update): UPDATE ---
    def atualizar(self, autor: Autor):
        sql = "UPDATE Autor SET nomeAutor = %s, nacionalidadeAutor = %s WHERE idAutor = %s"
        try:
            conn = self.db.conectar()
            cursor = conn.cursor()
            valores = (autor.nomeAutor, autor.nacionalidadeAutor, autor.idAutor)
            cursor.execute(sql, valores)
            conn.commit()
            print(" Autor atualizado com sucesso!")
        except Error as e:
            print(f" Erro ao atualizar Autor: {e}")
        finally:
            self.db.fechar_conexao()

    # --- D (Delete): DELETE ---
    def deletar(self, idAutor):
        sql = "DELETE FROM Autor WHERE idAutor = %s"
        try:
            conn = self.db.conectar()
            cursor = conn.cursor()
            cursor.execute(sql, (idAutor,))
            conn.commit()
            print(f" Autor ID {idAutor} excluído com sucesso!")
        except Error as e:
            print(f" Erro ao deletar Autor: {e}. Verifique se não há Livros associados.")
        finally:
            self.db.fechar_conexao()

    # --- SELECT BY ID (Método auxiliar para UPDATE e detalhes) ---
    def selecionar_por_id(self, idAutor):
        sql = "SELECT idAutor, nomeAutor, nacionalidadeAutor FROM Autor WHERE idAutor = %s"
        try:
            conn = self.db.conectar()
            cursor = conn.cursor()
            cursor.execute(sql, (idAutor,))
            resultado = cursor.fetchone()

            if resultado:
                id, nome, nac = resultado
                return Autor(id, nome, nac)
            return None
        except Error as e:
            print(f" Erro ao buscar Autor por ID: {e}")
            return None
        finally:
            self.db.fechar_conexao()