from pydantic import BaseModel, Field
from datetime import date


class Livro(BaseModel):
    idLivro: int
    tituloLivro: str = Field(max_length=150) # CORRIGIDO: de 'titulo' para 'tituloLivro'
    DataPublicacaoLivro: date # CORRIGIDO: de 'dataPublicaoLivro' para 'DataPublicacaoLivro'
    precoLivro: float 
    estoqueLivro: int
    PaginasLivro: int
    # Referencias foreign key - CORRIGIDO: alinhamento com os nomes das colunas SQL
    Editora_idEditora: int
    Autor_idAutor: int
    EstoqueLivros_idEstoqueLivros: int