from pydantic import BaseModel
from datetime import date


class Pedido(BaseModel):
    idPedido: int
    dataPedido: date
    valorTotal: float
    idCliente: int