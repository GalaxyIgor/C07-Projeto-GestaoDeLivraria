from pydantic import BaseModel



class cliente_has_Livro(BaseModel):
    Pedido_idPedido: int
    Livro_idLivro: int
    Livro_Editora_idEditora: int
    quantidade: int
