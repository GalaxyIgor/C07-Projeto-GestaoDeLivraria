import pytest
from unittest.mock import MagicMock
from src.dao.dao_autor import AutorDAO
from src.models.autor import Autor


def test_inserir_autor(mocker):
    dao = AutorDAO()

    # mock da conexão
    conn = MagicMock()
    cursor = MagicMock()

    conn.cursor.return_value = cursor
    dao.db.criar_conexao = MagicMock(return_value=conn)

    autor = Autor(idAutor=1, nomeAutor="Machado", nacionalidadeAutor="Brasileiro")

    dao.insert(autor)

    cursor.execute.assert_called_once()
    conn.commit.assert_called_once()
