import mysql.connector
from src.dao.dao_autor import AutorDAO
from src.models.autor import Autor

def test_inserir_e_listar_autor():
    dao = AutorDAO()

    autor = Autor(idAutor=2, nomeAutor="Teste", nacionalidadeAutor="BR")
    dao.insert(autor)

    autores = dao.selecionar_todos()

    assert any(a.nomeAutor == "Teste" for a in autores)
