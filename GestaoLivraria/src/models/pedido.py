from pydantic import BaseModel
from datetime import date


class Pedido(BaseModel):
    idPedido: int | None = None
    dataPedido: date
    valorTotal: float = 0.0