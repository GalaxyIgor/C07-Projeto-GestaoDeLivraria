from pydantic import BaseModel


class Cliente_has_Pedido(BaseModel):
    Cliente_idCliente: int
    Pedido_idPedido: int