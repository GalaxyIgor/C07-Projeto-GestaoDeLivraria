from pydantic import BaseModel, Field


class Cliente(BaseModel):
    idCliente: int
    nomeCliente: str = Field(max_length=120)
    emailCliente: str = Field(max_length=120)
    telefoneCliente: str = Field(max_length=45)
    premiumCliente: bool = Field(default=False)
    