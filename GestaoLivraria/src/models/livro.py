from pydantic import BaseModel, Field
from datetime import  date




class Livro(BaseModel):
    idLivro: int
    titulo: str = Field(max_length=150)
    dataPublicaoLivro: date
    precoLivro: float 
    estoqueLivro: int
    paginasLivro: int
    # Referencias foreign key
    editoraId: int
    autorId: int
    estoqueIdEstoque: int