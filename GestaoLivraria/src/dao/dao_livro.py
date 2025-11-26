from src.utils.conection import Conexao
from mysql.connector import Error
from src.models.livro import Livro


class LivroDAO:

    def __init__(self):
        self.db = Conexao()

    # ---------------- INSERT ----------------
    def insert(self, livro: Livro):
        sql = """
              INSERT INTO Livro (idLivro, títuloLivro, DataPublicacaoLivro, precoLivro, estoqueLivro, \
                                 PaginasLivro, Editora_idEditora, Autor_idAutor, EstoqueLivros_idEstoqueLivros)
              VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s) \
              """

        try:
            conn = self.db.conectar()
            cursor = conn.cursor()

            valores = (
                livro.idLivro,
                livro.tituloLivro,
                livro.DataPublicacaoLivro,
                livro.precoLivro,
                livro.estoqueLivro,
                livro.PaginasLivro,
                livro.Editora_idEditora,
                livro.Autor_idAutor,
                livro.EstoqueLivros_idEstoqueLivros
            )

            cursor.execute(sql, valores)
            conn.commit()
            print("Livro inserido com sucesso!")

        except Error as e:
            raise Exception(f"Erro ao inserir livro: {e}")
        finally:
            self.db.fechar()

    # ---------------- SELECT ALL ----------------
    def selecionar_todos(self):
        sql = """
              SELECT idLivro, \
                     títuloLivro, \
                     DataPublicacaoLivro, \
                     precoLivro, \
                     estoqueLivro,
                     PaginasLivro, \
                     Editora_idEditora, \
                     Autor_idAutor, \
                     EstoqueLivros_idEstoqueLivros
              FROM Livro \
              """
        livros = []

        try:
            conn = self.db.conectar()
            cursor = conn.cursor()
            cursor.execute(sql)

            for row in cursor.fetchall():
                livros.append(Livro(
                    idLivro=row[0],
                    tituloLivro=row[1],
                    DataPublicacaoLivro=row[2],
                    precoLivro=row[3],
                    estoqueLivro=row[4],
                    PaginasLivro=row[5],
                    Editora_idEditora=row[6],
                    Autor_idAutor=row[7],
                    EstoqueLivros_idEstoqueLivros=row[8]
                ))

            return livros

        except Error as e:
            print(f"Erro ao selecionar livros: {e}")
            return []
        finally:
            self.db.fechar()

    # ---------------- SELECT BY ID ----------------
    def selecionar_por_id(self, idLivro: int):
        sql = """
              SELECT idLivro, \
                     títuloLivro, \
                     DataPublicacaoLivro, \
                     precoLivro, \
                     estoqueLivro,
                     PaginasLivro, \
                     Editora_idEditora, \
                     Autor_idAutor, \
                     EstoqueLivros_idEstoqueLivros
              FROM Livro \
              WHERE idLivro = %s \
              """

        try:
            conn = self.db.conectar()
            cursor = conn.cursor()
            cursor.execute(sql, (idLivro,))
            row = cursor.fetchone()

            if row:
                return Livro(
                    idLivro=row[0],
                    tituloLivro=row[1],
                    DataPublicacaoLivro=row[2],
                    precoLivro=row[3],
                    estoqueLivro=row[4],
                    PaginasLivro=row[5],
                    Editora_idEditora=row[6],
                    Autor_idAutor=row[7],
                    EstoqueLivros_idEstoqueLivros=row[8]
                )
            return None

        except Error as e:
            print(f"Erro ao buscar livro: {e}")
            return None
        finally:
            self.db.fechar()

    # ---------------- UPDATE ----------------
    def atualizar(self, livro: Livro):
        sql = """
              UPDATE Livro \
              SET títuloLivro                   = %s, \
                  DataPublicacaoLivro           = %s, \
                  precoLivro                    = %s, \
                  estoqueLivro                  = %s, \
                  PaginasLivro                  = %s, \
                  Editora_idEditora             = %s, \
                  Autor_idAutor                 = %s, \
                  EstoqueLivros_idEstoqueLivros = %s
              WHERE idLivro = %s \
              """

        try:
            conn = self.db.conectar()
            cursor = conn.cursor()

            valores = (
                livro.tituloLivro,
                livro.DataPublicacaoLivro,
                livro.precoLivro,
                livro.estoqueLivro,
                livro.PaginasLivro,
                livro.Editora_idEditora,
                livro.Autor_idAutor,
                livro.EstoqueLivros_idEstoqueLivros,
                livro.idLivro,
            )

            cursor.execute(sql, valores)
            conn.commit()
            print("Livro atualizado com sucesso!")

        except Error as e:
            print(f"Erro ao atualizar livro: {e}")
        finally:
            self.db.fechar()

    # ---------------- DELETE ----------------
    def deletar(self, idLivro: int):
        sql = "DELETE FROM Livro WHERE idLivro = %s"

        try:
            conn = self.db.conectar()
            cursor = conn.cursor()
            cursor.execute(sql, (idLivro,))
            conn.commit()
            print("Livro deletado com sucesso!")

        except Error as e:
            print(f"Erro ao deletar livro: {e}. É possível que haja detalhes associados.")
        finally:
            self.db.fechar()
    # ---------------- SELECT COM JOIN SEM TABELA INTERMEDIÁRIA ----------------
    def selecionar_livros_e_autores(self):
        sql = """
              SELECT l.títuloLivro, a.nomeAutor, a.nacionalidadeAutor
              FROM Livro l
                       JOIN Autor a ON l.Autor_idAutor = a.idAutor \
              """
        resultados = []
        try:
            conn = self.db.conectar()
            cursor = conn.cursor()
            cursor.execute(sql)
            for row in cursor.fetchall():
                resultados.append({
                    "Titulo": row[0],
                    "Autor": row[1],
                    "Nacionalidade": row[2]
                })
            return resultados
        except Error as e:
            print(f"Erro ao buscar livros e autores: {e}")
            return []
        finally:
            self.db.fechar()

    def selecionar_livros_e_editoras(self):
        sql = """
              SELECT l.títuloLivro, l.DataPublicacaoLivro, e.nomeEditora, e.LocalEditora
              FROM Livro l
                       JOIN Editora e ON l.Editora_idEditora = e.idEditora \
              """
        resultados = []
        try:
            conn = self.db.conectar()
            cursor = conn.cursor()
            cursor.execute(sql)
            for row in cursor.fetchall():
                resultados.append({
                    "Titulo": row[0],
                    "Publicacao": row[1],
                    "Editora": row[2],
                    "Local": row[3]
                })
            return resultados
        except Error as e:
            print(f"Erro ao buscar livros e editoras: {e}")
            return []
        finally:
            self.db.fechar()

    def selecionar_detalhes_do_livro(self):
        sql = """
              SELECT l.títuloLivro, d.Idioma, d.sinopseDetalhes, d.numPaginasDetalhes
              FROM Livro l
                       JOIN DetalhesDoLivro d ON l.idLivro = d.Livro_idLivro \
              """
        resultados = []
        try:
            conn = self.db.conectar()
            cursor = conn.cursor()
            cursor.execute(sql)
            for row in cursor.fetchall():
                resultados.append({
                    "Titulo": row[0],
                    "Idioma": row[1],
                    "Sinopse": row[2],
                    "Paginas_Detalhe": row[3]
                })
            return resultados
        except Error as e:
            print(f"Erro ao buscar detalhes do livro: {e}")
            return []
        finally:
            self.db.fechar()